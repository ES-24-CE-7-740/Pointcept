#!/bin/bash
echo 'Starting reduced more real dataset training!'

mkdir -p exp/ptv3_reduced_more_logs

run_training() {
    echo "Running: $1"
    eval "$2 >> exp/ptv3_reduced_more_logs/$3.log 2>&1"
    if [ $? -ne 0 ]; then
        echo "Error: Training step failed: $1 (check exp/ptv3_reduced_more_logs/$3.log for details)"
        echo "Continuing with the next training job..."
        #exit 1  # Stop script on failure
    fi
    echo "Completed: $1 (logs saved to exp/ptv3_reduced_more_logs/$3.log)"
}

run_training "Training on 200 pcs for 300 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-pt-v3m1-0-base-200 -n PTv3_200_300_more" \
    "training_200_300"

run_training "Training on 400 pcs for 150 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-pt-v3m1-0-base-400 -n PTv3_400_150_more" \
    "training_400_150"

run_training "Training on 600 pcs for 100 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-pt-v3m1-0-base-600 -n PTv3_600_100_more" \
    "training_600_100"

run_training "Training on 800 pcs for 75 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-pt-v3m1-0-base-800 -n PTv3_800_75_more" \
    "training_800_75"

run_training "Training on 1000 pcs for 60 epochs..." \
    "CUDA_VISIBLE_DEVICES=0,1 sh scripts/train.sh -p python -g 2 -d tractors_and_combines_real -c semseg-pt-v3m1-0-base-1000 -n PTv3_1000_60_more" \
    "training_1000_60"

echo 'Training completed!'
