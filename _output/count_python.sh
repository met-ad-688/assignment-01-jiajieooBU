#!/bin/bash

count=0
for file in data/*.csv; do
    if [[ -f "$file" ]]; then
        count=$((count + $(grep -i "python" "$file" | wc -l)))
    fi
done

echo "Number of lines containing 'python' in CSV files: $count"

