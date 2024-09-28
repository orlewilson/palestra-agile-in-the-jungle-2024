#!/bin/bash

# Criar imagem
docker build -t proforlewilson/dev-environment-palestra-agile-in-the-jungle .

# Publicar imagem
docker push proforlewilson/dev-environment-palestra-agile-in-the-jungle

# --tag , -t		Nome da imagem a ser criada

# Fonte: https://docs.docker.com/engine/reference/commandline/build/