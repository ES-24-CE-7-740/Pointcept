#!/bin/bash
#SBATCH --job-name=sonata-scannet
#SBATCH --output=logs/sonata-scannet_%j.log
#SBATCH --error=logs/sonata-scannet_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --gres=gpu:4
#SBATCH --time=1:00:00
#SBATCH --mem=128G

# Load environment modules if needed
# module load cuda/12.2 or similar (depends on your cluster)

# Activate conda
source ~/miniforge3/bin/activate pointcept-torch2.5.0-cu12.4

# Run training
sh scripts/train.sh -p python -g 4 -d sonata -c semseg-sonata-v1m1-0a-scannet-lin -n sonata-scannet-lin -w exp/sonata/pretrain-sonata-v1m1-0-base.pth
