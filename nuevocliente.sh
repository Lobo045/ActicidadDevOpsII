#!/bin/bash

added_files=$(git diff --name-status --diff-filter=A | grep '^A' | grep 'client_')

if [ -n "$added_files" ]; then
    git add .
    
    git commit -m "New Client"

    git push 

    echo "Se ha agregado un nuevo cliente, la notificacion esta siendo mandada a el equipo."

else
    echo "No se ha agregado a nigun cliente"

fi
