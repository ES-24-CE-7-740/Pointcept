#!/bin/bash
echo 'Starting oacnn combined dataset training!'

mkdir -p exp/oacnn_combined_logs

run_training() {
    echo "Running: $1"
    eval "$2 >> exp/oacnn_combined_logs/$3.log 2>&1"
    if [ $? -ne 0 ]; then
        echo "Error: Training step failed: $1 (check exp/oacnn_combined_logs/$3.log for details)"
        echo "Continuing with the next training job..."
        #exit 1  # Stop script on failure
    fi
    echo "Completed: $1 (logs saved to exp/oacnn_combined_logs/$3.log)"
}

run_training "Training using 200 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sh scripts/train.sh -p python -g 6 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-200 -n OACNN_200" \
    "training_200"

run_training "Training using 400 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sh scripts/train.sh -p python -g 6 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-400 -n OACNN_400" \
    "training_400"

run_training "Training using 600 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sh scripts/train.sh -p python -g 6 -d tractors_and_combines_combined -c semseg-oacnns-v1m1-0-base-600 -n OACNN_600" \
    "training_600"

echo 'Training completed!'
