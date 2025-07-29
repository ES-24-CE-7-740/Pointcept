#!/bin/bash

# Trained using even sampling and mixed dataset

echo 'Starting OACNN no augmentations extended training test'

#echo "Testing 2 real point clouds"
#sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-2 -n OACNN_bare_mixed_2

#echo "Testing 4 real point clouds"
#sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-4 -n OACNN_bare_mixed_4

#echo "Testing 6 real point clouds"
#sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-6 -n OACNN_bare_mixed_6

#echo "Testing 8 real point clouds"
#sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-8 -n OACNN_bare_mixed_8

echo "Testing 10 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-10 -n OACNN_bare_mixed_10

echo "Testing 15 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-15 -n OACNN_bare_mixed_15

echo "Testing 20 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-20 -n OACNN_bare_mixed_20

echo "Testing 30 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-30 -n OACNN_bare_mixed_30

echo "Testing 50 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-50 -n OACNN_bare_mixed_50

echo "Testing 100 real point clouds"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-100 -n OACNN_bare_mixed_100

#echo "Testing 150 real point clouds"
#sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c bare-mixed/oacnns-bare-150 -n OACNN_bare_mixed_150