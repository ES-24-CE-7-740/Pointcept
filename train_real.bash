export PYTHONPATH=./

python tools/train.py --config-file ./configs/tractors_and_combines/real-semseg-oaccns.py --num-gpus 2 --options save_path=exp/tgc_real_oacnns_from_synth_pretrain2  
