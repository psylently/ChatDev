# BASIC ########################################################
FROM python:3.11-bookworm as build
ENV PYTHONUNBUFFERED: "true"
ENV PYTHONIOENCODING: UTF-8
RUN apt update
WORKDIR /app


# DEVELOPMENT ########################################################
FROM build as dev
WORKDIR /app
# Dev dependencies
RUN apt install -y libyaml-dev wget vim curl 
# Install pip dev dependencies
# Python watchdog library dependencies
RUN pip install pyyaml argh
# Install dev dependencies.
COPY requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "sleep","infinity" ]
