#!/bin/bash

# Define the list of user numbers
user_numbers=(15 16 4 44 50 8)

# Define the common password
password="abc123abc!"

# Iterate over each user number
for number in "${user_numbers[@]}"
do
    # Construct the username
    username="user${number}"
    
    # Construct the curl command to delete the file
    curl_command="curl -X DELETE -u ${username}:${password} \"http://localhost:8080/remote.php/dav/files/${username}/train_mini.csv\""
    
    # Execute the curl command
    echo "Deleting train_mini.csv for ${username}..."
    eval ${curl_command}
    
    # Check if the deletion was successful
    if [ $? -eq 0 ]; then
        echo "File deleted successfully for ${username}"
    else
        echo "Failed to delete file for ${username}"
    fi
done
