export PYTHONPATH=./

python tools/train.py --config-file ./configs/simulation_ablation/semseg_oa_base.py --num-gpus 2 --options save_path=exp/simulation_ablation_full2
