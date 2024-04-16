FROM node:18.12.0-alpine

RUN mkdir -p /home/nuxt_ecommerce
WORKDIR /home/nuxt_ecommerce
COPY . /home/nuxt_ecommerce

RUN npm install
RUN npm run build

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

EXPOSE 3000 

ENTRYPOINT ["node", ".output/server/index.mjs"]

# docker run -p 4200:3000 --name nuxt-demo nuxt-app
# This Docker file was a success