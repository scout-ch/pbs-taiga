FROM taigaio/taiga-back:6.9.0@sha256:70ee08e4416c282437f55b5a5f48e8c3c10390022eac275999366728e227e961 AS base

FROM alpine/git@sha256:d453f54c83320412aa89c391b076930bd8569bc1012285e8c68ce2d4435826a3 AS cloner

RUN git clone https://github.com/taigaio/taiga-contrib-oidc-auth.git && cd taiga-contrib-oidc-auth && git checkout c623b753047ce9923f3e38614d86e81fc5eb2bb1

FROM base AS builder

COPY ./config-extension.py /tmp/config-extension.py

RUN cat /tmp/config-extension.py >> /taiga-back/settings/config.py

COPY --from=cloner /git/taiga-contrib-oidc-auth /taiga-contrib-oidc-auth

RUN cd /taiga-contrib-oidc-auth/back && python setup.py sdist

FROM base AS final

COPY ./urls.py /taiga-back/settings/urls.py

COPY ./custom_entrypoint.sh /taiga-back/docker/custom_entrypoint.sh

COPY ./migration.sh /taiga-back/docker/migration.sh

COPY --from=builder /taiga-back/settings/config.py /taiga-back/settings/config.py

COPY --from=builder /taiga-contrib-oidc-auth/back/dist/taiga_contrib_oidc_auth-0.3.tar.gz /tmp/taiga_contrib_oidc_auth.tar.gz

RUN pip install /tmp/taiga_contrib_oidc_auth.tar.gz && rm /tmp/taiga_contrib_oidc_auth.tar.gz