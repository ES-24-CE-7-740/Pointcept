#!/bin/bash
#SBATCH --job-name=ptv3-scannet
#SBATCH --output=logs/ptv3-scannet_%j.log
#SBATCH --error=logs/ptv3-scannet_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --gres=gpu:2
#SBATCH --time=1:00:00
#SBATCH --mem=64G

# Load environment modules if needed
# module load cuda/12.2 or similar (depends on your cluster)

# Activate conda
source ~/miniforge3/bin/activate pointcept-torch2.5.0-cu12.4

# Run training
sh scripts/train.sh -p python -g 2 -d scannet -c semseg-pt-v3m1-0-base -n ptv3-scannet
