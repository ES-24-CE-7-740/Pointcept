#!/bin/bash

# Trained using even sampling and real only dataset

echo 'Starting OACNN augmentation training test'

echo "Testing no augmentations"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-bare -n OACNN_bare_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-bare -n OACNN_bare_2


echo "Testing scale augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-scale -n OACNN_scale_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-scale -n OACNN_scale_2


echo "Testing rotate augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate -n OACNN_rotate_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate -n OACNN_rotate_2


echo "Testing flip augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-flip -n OACNN_flip_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-flip -n OACNN_flip_2


echo "Testing jitter augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-jitter -n OACNN_jitter_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-jitter -n OACNN_jitter_2


echo "Testing rotate and scale augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate-scale -n OACNN_rotate_scale_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate-scale -n OACNN_rotate_scale_2


echo "Testing rotate, scale and flip augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate-scale-flip -n OACNN_rotate_scale_flip_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10-rotate-scale-flip -n OACNN_rotate_scale_flip_2


echo "Testing full augmentation"
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10 -n OACNN_all_1
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c augmentations/oacnns-base-10 -n OACNN_all_2