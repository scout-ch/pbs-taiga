FROM node:24.11.1@sha256:9a2ed90cd91b1f3412affe080b62e69b057ba8661d9844e143a6bbd76a23260f AS builder

RUN git clone https://github.com/taigaio/taiga-contrib-oidc-auth.git /app && cd /app && git checkout c623b753047ce9923f3e38614d86e81fc5eb2bb1

WORKDIR /app/front

RUN npm install && npm install gulp

RUN ./node_modules/.bin/gulp build

FROM taigaio/taiga-front:6.9.0@sha256:35e3345e2a0152e777543b1f5565fd4578804d39b57a4848fe41b723bcce5885 AS final

COPY --from=builder /app/front/dist/ /usr/share/nginx/html/plugins/oidc-auth/

COPY pbs-logo.svg /usr/share/nginx/html/plugins/oidc-auth/images/contrib/

RUN sed -i "s/contribs=()/contribs=('\"plugins\/oidc-auth\/oidc-auth.json\"')/" /docker-entrypoint.d/30_config_env_subst.sh

RUN sed -i '$ s/}$/,\n  "oidcButtonText": "MiData",\n  "oidcButtonImage": "pbs-logo.svg",\n  "oidcMountPoint": "\/api\/oidc"\n}/' /usr/share/nginx/html/conf.json.template
