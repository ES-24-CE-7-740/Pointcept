#!/bin/bash
echo 'Starting OACNN combined real only even sampling extended 2 dataset training!'


echo "Training using 4 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-4 -n OACNN_4


echo "Training using 6 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-6 -n OACNN_6


echo "Training using 8 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-8 -n OACNN_8


echo "Training using 15 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-15 -n OACNN_15


echo "Training using 20 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-20 -n OACNN_20


echo "Training using 30 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-30 -n OACNN_30


echo "Training using 40 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-40 -n OACNN_40