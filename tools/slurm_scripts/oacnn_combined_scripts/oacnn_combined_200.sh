#!/bin/bash
#SBATCH --job-name=200_oacnn
#SBATCH --cpus-per-task=80
#SBATCH --mem=128G
#SBATCH --time=12:00:00
#SBATCH --output=oacnn_combined_200_%j.out
#SBATCH --error=oacnn_combined_200_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --gres=gpu:6

#SBATCH --chdir=/ceph/project/ce-7-740/project/repos/Pointcept

# Execute the job using Singularity
srun singularity exec --nv --bind \
	/ceph:/ceph /ceph/project/ce-7-740/project/repos/Pointcept/containers/ptv3-container.sif \
	sh scripts/train.sh \
	-p python \
	-g 6 \
	-d tractors_and_combines_combined \
	-c semseg-oacnns-v1m1-0-base-200 \
	-n OACNN_200