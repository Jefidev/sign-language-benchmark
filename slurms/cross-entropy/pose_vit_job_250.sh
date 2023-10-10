#!/bin/bash
# Submission script for Lucia
#SBATCH --job-name=ViTPose
#SBATCH --time=20:00:00 # hh:mm:ss
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres="gpu:1"
#SBATCH --mem-per-cpu=4096 
#SBATCH --partition=gpu
#
#SBATCH --mail-user=jerome.fink@unamur.be
#SBATCH --mail-type=ALL
#
#SBATCH --account=lsfb
#
#SBATCH --output=./output/ViTPose_250.out

module purge
module load PyTorch

source ./venv/bin/activate
pip install -r requirements.txt
nvidia-smi
python poseVIT_classification.py \
 -l 250\
 -e Pose-VIT-250\
 -d /gpfs/projects/acad/lsfb/datasets/lsfb_v2/isol