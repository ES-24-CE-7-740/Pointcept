#!/bin/bash
echo 'Starting combined dataset training!'

mkdir -p exp/ptv3_combined_logs

run_training() {
    echo "Running: $1"
    eval "$2 >> exp/ptv3_combined_logs/$3.log 2>&1"
    if [ $? -ne 0 ]; then
        echo "Error: Training step failed: $1 (check exp/ptv3_combined_logs/$3.log for details)"
        echo "Continuing with the next training job..."
        #exit 1  # Stop script on failure
    fi
    echo "Completed: $1 (logs saved to ptv3_combined_logs/$3.log)"
}

run_training "Training using 200 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-200 -n PTv3_200" \
    "training_200"

run_training "Training using 400 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-400 -n PTv3_400" \
    "training_400"

run_training "Training using 600 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-600 -n PTv3_600" \
    "training_600"

run_training "Training using 800 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-800 -n PTv3_800" \
    "training_800"

run_training "Training using 1000 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-1000 -n PTv3_1000" \
    "training_1000"

run_training "Training using 1200 real pcs for 10 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-1200 -n PTv3_1200" \
    "training_1200"

echo 'Training completed!'
