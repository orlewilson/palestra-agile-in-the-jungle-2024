#!/bin/bash

sudo mkdir /usr/local/bin

sudo curl -L "https://github.com/docker/compose/releases/download/v2.29.6/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
