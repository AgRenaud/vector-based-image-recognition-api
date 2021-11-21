#!/bin/bash

# Go to https://qdrant.tech/documentation/collections/#delete-collection

echo -e "\033[0;33m# Clean Qdrant's collections \033[0m"
response=$(curl -sb -X GET http://localhost:6333/collections | jq ".result.collections[].name")
echo -e "Do you want to delete all the following collections:\n$response"
while true; do
    read -e -p "[y/N]: " yn
    case $yn in
        [Yy]* ) rm -rf ../docker/qdrant/data/collections/*; break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done
