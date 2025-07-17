#!/bin/bash
echo 'Starting OACNN combined real only even sampling extended dataset training!'


echo "Training using 2 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-2 -n OACNN_2


echo "Training using 10 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-10 -n OACNN_10


echo "Training using 50 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-50 -n OACNN_50


echo "Training using 100 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-100 -n OACNN_100


echo "Training using 150 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-150 -n OACNN_150