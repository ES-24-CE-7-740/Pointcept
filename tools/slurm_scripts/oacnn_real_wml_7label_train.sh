#!/bin/bash
#SBATCH --job-name=oacnn_7label_train
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --output=oacnn_7label_train_%j.out
#SBATCH --error=oacnn_7label_train_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh scripts/train.sh \
	-p python \
	-g 2 \
	-d ttgch_with_model_labels \
	-c real/semseg-oacnns-v1m1-0-base-7label \
	-n OACNN_real_7label_500epochs
