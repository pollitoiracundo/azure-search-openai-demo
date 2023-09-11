FROM python:latest
RUN apk --no-cache add curl
RUN apk --no-cache add bash
RUN curl -fsSL https://aka.ms/install-azd.sh | bash
RUN python3 --version
FROM node:7-alpine
RUN node --version
