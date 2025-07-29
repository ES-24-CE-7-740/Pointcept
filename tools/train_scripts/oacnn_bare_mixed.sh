#!/bin/bash

# Trained using even sampling and mixed dataset

echo 'Starting OACNN no augmentations training test'

echo "Testing 200 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-200 -n OACNN_bare_mixed_200

echo "Testing 600 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-600 -n OACNN_bare_mixed_600

echo "Testing 1000 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-1000 -n OACNN_bare_mixed_1000


echo "Testing 400 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-400 -n OACNN_bare_mixed_400

echo "Testing 800 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-800 -n OACNN_bare_mixed_800

echo "Testing 1200 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-1200 -n OACNN_bare_mixed_1200