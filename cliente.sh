#!/bin/bash

# Check if there are added, deleted, or modified client files
added_files=$(git diff --name-status --diff-filter=A | grep '^A' | grep 'client_')
deleted_files=$(git diff --name-status --diff-filter=D | grep '^D' | grep 'client_')
modified_files=$(git diff --name-status --diff-filter=M | grep '^M' | grep 'client_')

# If there are added, deleted, or modified client files, proceed with additional actions
if [ -n "$added_files" ]; then
    git pull
    git add .

    git commit -m "New Client"

    git push
    echo "Cliente agregado, mandando notificación"
else
    echo "No se ha agregado ningún cliente"
fi

if [ -n "$deleted_files" ]; then
    git pull
    git add .

    git commit -m "Deleted Client"

    git push
    echo "Cliente borrado, mandando notificación"
else
    echo "No se ha borrado ningún cliente"
fi

if [ -n "$modified_files" ]; then
    git pull
    git add .

    git commit -m "Edited Client"

    git push
    echo "Cliente editado, mandando notificación a grupo"
else
    echo "No se ha editado ningún cliente"
fi
