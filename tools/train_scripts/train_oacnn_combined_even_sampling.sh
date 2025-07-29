#!/bin/bash
echo 'Starting OACNN combined real only even sampling dataset training!'


echo "Training using 200 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-200 -n OACNN_200


echo "Training using 400 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-400 -n OACNN_400


echo "Training using 600 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-600 -n OACNN_600


echo "Training using 800 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-800 -n OACNN_800


echo "Training using 1000 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-1000 -n OACNN_1000


echo "Training using 1200 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-1200 -n OACNN_1200
