FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install ansible-base paramiko

ENV ANSIBLE_GATHERING smart
ENV ANSIBLE_HOST_KEY_CHECKING false
ENV ANSIBLE_RETRY_FILES_ENABLED false
ENV ANSIBLE_ROLES_PATH /app/roles
ENV ANSIBLE_SSH_PIPELINING True

COPY . .

CMD [ "python3", "-u", "-m" , "flask", "run", "--host=0.0.0.0"]