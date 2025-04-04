#!/bin/bash
#SBATCH --job-name=oacnn_combined_train
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --time=12:00:00
#SBATCH --output=ptv3_combined_train_%j.out
#SBATCH --error=ptv3_combined_train_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh tools/train_scripts/train_oacnn_combined_even_sampling_extended.sh
