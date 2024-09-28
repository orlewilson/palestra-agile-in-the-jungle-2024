#!/bin/bash
mkdir quality/reports/

mkdir quality/reports/security_analysis

bandit \
    --recursive project \
    --format html --output security_report.html

mv security_report.html quality/reports/security_analysis/security_report.html
