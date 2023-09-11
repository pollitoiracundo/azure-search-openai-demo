FROM node:7-alpine
# Update the package list and install Python 3
RUN apk update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    rm -rf /var/cache/apk/*
# get curl and bash
RUN apk --no-cache add curl
RUN apk --no-cache add bash
# get azd
RUN curl -fsSL https://aka.ms/install-azd.sh | bash
# test 
RUN python3 --version
RUN node --version
RUN azd --help