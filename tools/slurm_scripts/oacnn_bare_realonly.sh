#!/bin/bash
#SBATCH --job-name=bare_real
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --time=100:00:00
#SBATCH --output=oacnn_bare_realonly_%j.out
#SBATCH --error=oacnn_bare_realonly_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh tools/train_scripts/oacnn_bare_realonly.sh
