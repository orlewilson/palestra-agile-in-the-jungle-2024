#!/bin/bash

mkdir quality/reports/
mkdir quality/reports/coverage_analysis

# Teste de cobertura de código
coverage erase

coverage run -m pytest

coverage report

coverage xml -o quality/reports/coverage_analysis/coverage_xml_report.xml

coverage html -d quality/reports/coverage_analysis/converage_html_report
