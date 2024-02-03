#!/bin/bash

file_to_monitor="\Users\lopez\.spyder-py3"

while inotifywait -e delete "$file_to_monitor"; do
    echo "File $file_to_monitor has been deleted."
done
