#!/bin/bash

aws-cert-checker example.com 84600

if [ $? -eq 0 ]; then
    echo "SKIP"
    exit 0
else
    echo "LETSENCRYPT"
    exit 1
fi
