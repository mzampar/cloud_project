#!/bin/bash

URL="http://localhost:8080/ocs/v1.php/cloud/users"
USERNAME="admin"
PASSWORD="password"
PASSWORD_ENCODED="abc123abc!" 


for i in {1..40}; do
    USERID="user$i"
    curl -X POST -u "$USERNAME:$PASSWORD" -H "OCS-APIRequest: true" "$URL" \
        -d "userid=$USERID" -d "password=$PASSWORD_ENCODED"
done
