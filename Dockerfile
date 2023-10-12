# BASIC ########################################################
FROM python:3.11-bookworm as build
ENV PYTHONUNBUFFERED: "true"
ENV PYTHONIOENCODING: UTF-8
#ENV PYTHONPATH "${PYTHONPATH}:/app/submodules/microservices_shared"
RUN apt update
WORKDIR /app


# DEVELOPMENT ########################################################
FROM build as dev
WORKDIR /app
# Dev dependencies
# LibYAML for watchdog watchmedo script
RUN apt install -y libyaml-dev wget vim curl 
#libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
#RUN cd external_deps/ && chmod +x Anaconda3-2023.09-0-Linux-x86_64.sh &&  bash ./Anaconda3-2023.09-0-Linux-x86_64.sh -b
# Install pip dev dependencies
# Python watchdog library dependencies
RUN pip install pyyaml argh
# Install dev dependencies.
COPY requirements.txt /app
RUN pip install -r requirements.txt
#RUN useradd -ms /bin/bash vscode && chown -R vscode:vscode /app && chmod 755 -R /app
#USER vscode
# Start consumer with watchdog
#ENTRYPOINT watchmedo auto-restart --directory=/app/src --pattern="*.py" --recursive -- python -u /app/src/app.py
ENTRYPOINT [ "sleep","infinity" ]
