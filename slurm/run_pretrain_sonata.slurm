#!/bin/bash
#SBATCH --job-name=sonata-pretrain
#SBATCH --output=logs/sonata-pretrain_%j.log
#SBATCH --error=logs/sonata-pretrain_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=48
#SBATCH --gres=gpu:4
#SBATCH --time=1:00:00
#SBATCH --mem=128G

# Load environment modules if needed
# module load cuda/12.2 or similar (depends on your cluster)

# Activate conda
source ~/miniforge3/bin/activate pointcept-torch2.5.0-cu12.4

# Run training
sh scripts/train.sh -p python -m 1 -g 4 -d agco -c pretrain-sonata-coord-base -n sonata-coord-pretrain-base
