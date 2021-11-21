 #!/bin/bash

qdrant_url=$1
collection_name=$2
points_folder=$3
distance=${4:-Cosine}
vector_size=${5:-300}

python3 ./pyscripts/create_collection.py $qdrant_url $collection_name $distance $vector_size

python3 ./pyscripts/feed_collection.py $qdrant_url $collection_name $points_folder

python3 ./pyscripts/check_collection.py $qdrant_url $collection_name $points_folder
