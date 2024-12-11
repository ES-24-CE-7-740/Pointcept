#!/bin/bash
echo 'Starting OACNN reduced real dataset training!'

mkdir -p exp/oacnn_reduced_logs

run_training() {
    echo "Running: $1"
    eval "$2 >> exp/oacnn_reduced_logs/$3.log 2>&1"
    if [ $? -ne 0 ]; then
        echo "Error: Training step failed: $1 (check exp/oacnn_reduced_logs/$3.log for details)"
        echo "Continuing with the next training job..."
    fi
    echo "Completed: $1 (logs saved to exp/oacnn_reduced_logs/$3.log)"
}

run_training "Training on 200 pcs for 300 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-oacnns-v1m1-0-base-200 -n OACNNs_200_300" \
    "training_200_300"

run_training "Training on 400 pcs for 150 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-oacnns-v1m1-0-base-400 -n OACNNs_400_150" \
    "training_400_150"

run_training "Training on 600 pcs for 100 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-oacnns-v1m1-0-base-600 -n OACNNs_600_100" \
    "training_600_100"

run_training "Training on 800 pcs for 75 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-oacnns-v1m1-0-base-800 -n OACNNs_800_75" \
    "training_800_75"

run_training "Training on 1000 pcs for 60 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-oacnns-v1m1-0-base-1000 -n OACNNs_1000_60" \
    "training_1000_60"


echo 'Training completed!'
