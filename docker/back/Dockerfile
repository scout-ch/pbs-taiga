FROM taigaio/taiga-back:6.10.1@sha256:627d77e43e1d83d6e75bd6556d2244c9366f4518a077f7d63d76188b51f86713 AS base

FROM alpine/git@sha256:3136372ed3c9e112d5a2620c66a6803e1b0b7f14a428fcbd0c5028bec4256430 AS cloner

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