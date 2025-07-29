#!/bin/bash
#SBATCH --job-name=oacnn_augmentations
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --time=100:00:00
#SBATCH --output=oacnn_augmentations_%j.out
#SBATCH --error=oacnn_augmentations_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh tools/train_scripts/oacnn_bare_mixed.sh
