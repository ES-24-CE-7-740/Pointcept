#!/bin/bash

# Trained using even sampling and real only dataset

echo 'Starting OACNN downsampling training test'

echo "Testing 60k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-60k -n OACNN_downsampling_60k

echo "Testing 50k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-50k -n OACNN_downsampling_50k

echo "Testing 40k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-40k -n OACNN_downsampling_40k

echo "Testing 30k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-30k -n OACNN_downsampling_30k

echo "Testing 20k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-20k -n OACNN_downsampling_20k

echo "Testing 10k downsampling"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c downsampling/oacnn-base-1200-10k -n OACNN_downsampling_10k