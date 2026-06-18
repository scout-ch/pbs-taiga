FROM node:24.17.0@sha256:032e78d7e54e352129831743737e3a83171d9cc5b5896f411649c597ce0b11ea AS builder

RUN git clone https://github.com/taigaio/taiga-contrib-oidc-auth.git /app && cd /app && git checkout c623b753047ce9923f3e38614d86e81fc5eb2bb1

WORKDIR /app/front

RUN npm install && npm install gulp

RUN ./node_modules/.bin/gulp build

FROM taigaio/taiga-front:6.10.3@sha256:570c8792ce802ff803a2275967e1d593cdd7c748e2d63163c4dab35fe2d2d646 AS final

COPY --from=builder /app/front/dist/ /usr/share/nginx/html/plugins/oidc-auth/

COPY pbs-logo.svg /usr/share/nginx/html/plugins/oidc-auth/images/contrib/

RUN sed -i "s/contribs=()/contribs=('\"plugins\/oidc-auth\/oidc-auth.json\"')/" /docker-entrypoint.d/30_config_env_subst.sh

RUN sed -i '$ s/}$/,\n  "oidcButtonText": "MiData",\n  "oidcButtonImage": "pbs-logo.svg",\n  "oidcMountPoint": "\/api\/oidc"\n}/' /usr/share/nginx/html/conf.json.template
