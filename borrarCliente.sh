#!/bin/bash

# Check if there are deleted client files
deleted_files=$(git diff --name-status --diff-filter=D | grep '^D' | grep 'client_')

if [ -n "$deleted_files" ]; then
        git add .
        git commit -m "Deleted Client"
        git push
        echo "Cliente borrado, mandando notificación"
    else
        echo "No se ha borrado ningún cliente"
fi

