FROM python:latest
FROM node:7-alpine
RUN apt-get update && apt-get install -y curl 
RUN curl -fsSL https://aka.ms/install-azd.sh | bash
