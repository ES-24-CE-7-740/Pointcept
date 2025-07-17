#!/bin/bash
echo 'Starting PTv3 combined real only even sampling dataset training!'


echo "Training using 200 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-200 -n PTv3_200


echo "Training using 400 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-400 -n PTv3_400


echo "Training using 600 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-600 -n PTv3_600


echo "Training using 800 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-800 -n PTv3_800


echo "Training using 1000 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-1000 -n PTv3_1000


echo "Training using 1200 real pcs for 10 epochs..."
sh scripts/train.sh -p python -g 2 -d tractors_and_combines_combined -c semseg-pt-v3m1-0-base-1200 -n PTv3_1200
