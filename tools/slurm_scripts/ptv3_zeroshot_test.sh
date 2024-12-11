#!/bin/bash
#SBATCH --job-name=ptv3_zeroshot_test
#SBATCH --cpus-per-task=24
#SBATCH --mem=60G
#SBATCH --time=12:00:00
#SBATCH --output=ptv3_zeroshot_test_%j.out
#SBATCH --error=ptv3_zeroshot_test_%j.err

# Set the number of tasks and GPUs directly
#SBATCH --ntasks=1
#SBATCH --chdir=/home/andreas/Github/Pointcept

# Execute the job using Singularity
export CUDA_VISIBLE_DEVICES=0,1

srun singularity exec --nv --bind /home:/home containers/ptv3-container.sif \
	sh scripts/test.sh \
	-p python \
	-g 2 \
	-d tractors_and_combines_combined \
	-n PTv3_zeroshot \
	-w model_best
