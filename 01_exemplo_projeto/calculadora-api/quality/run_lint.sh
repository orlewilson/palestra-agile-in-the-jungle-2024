#!/bin/bash

mkdir quality/reports/
mkdir quality/reports/static_analysis

# Verificação de erros estático no código, além de incentiva bons padrões de codificação
pylint project/*.py --reports=y --output-format=json | pylint-json2html -o static_analysis_report.html

mv static_analysis_report.html quality/reports/static_analysis/static_analysis_report.html
