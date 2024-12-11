#!/bin/bash
#SBATCH --job-name=oacnn_zeroshot_train
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --output=oacnn_zeroshot_train_%j.out
#SBATCH --error=oacnn_zeroshot_train_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh scripts/train.sh \
	-p python \
	-g 2 \
	-d tractors_and_combines_combined \
	-c semseg-oacnns-v1m1-0-base \
	-n OACNN_zeroshot
