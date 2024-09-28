#!/bin/bash

mkdir quality/reports/
mkdir quality/reports/integration_analysis

cd project && ./run_server.sh

cd ..

# Teste de integração usando Postman/Newmam
newman run quality/Calculadora_Teste_Integracao.postman_collection.json  -r htmlextra

mv newman  quality/reports/integration_analysis/
