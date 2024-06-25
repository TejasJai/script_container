#!/bin/bash

# Define the directory containing the <ns>_pods.txt files
directory="/root/container"

# Loop through each <ns>_pods.txt file in the directory
for file in "$directory"/*_pods.txt; do
    # Print the filename
    echo "Pods under namespace: $(basename "$file")"

    # Print the contents of the file
    cat "$file"

    # Add a separator for clarity
    echo "----------------------------------------"
done
