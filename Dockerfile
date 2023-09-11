FROM python:latest
FROM node:7-alpine
RUN apk --no-cache add curl
RUN curl -fsSL https://aka.ms/install-azd.sh | sh
