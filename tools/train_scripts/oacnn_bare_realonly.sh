#!/bin/bash

# Trained using even sampling and real only dataset (using the combined dataset still)

echo 'Starting OACNN no augmentations training test'

echo "Testing 200 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-200 -n OACNN_bare_realonly_200

echo "Testing 600 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-600 -n OACNN_bare_realonly_600

echo "Testing 1000 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-1000 -n OACNN_bare_realonly_1000


echo "Testing 400 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-400 -n OACNN_bare_realonly_400

echo "Testing 800 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-800 -n OACNN_bare_realonly_800

echo "Testing 1200 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-1200 -n OACNN_bare_realonly_1200