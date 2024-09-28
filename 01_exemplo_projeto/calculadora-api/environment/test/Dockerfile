# Imagem Base
FROM debian:11

# Mantenedor
LABEL version="1.0"
LABEL author="Orlewilson Maia (orlewilson.maia@gmail.com)"
LABEL description="Debian 11 + Python3 + FastAPI + QA"

# Atualização dos Pacotes
RUN apt update

# Instalação das Dependências

# Python
RUN apt install -y python3
RUN apt install -y pip

# FastAPI
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install httpx

# Qualidade de Software (QA)
RUN pip install pytest
RUN pip install pytest-cov
RUN pip install pylint
RUN pip install pylint-json2html
RUN pip install bandit

RUN apt install -y curl

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -

RUN apt install nodejs -y
RUN npm install -g newman
RUN npm install -g newman-reporter-htmlextra


# Diretório Padrão
WORKDIR /apps