export PYTHONPATH=./

python tools/train.py --config-file ./configs/tractors_and_combines/semseg-oacnns-base.py --num-gpus 2 --options save_path=exp/tgc_synth_oacnns_pretrain
