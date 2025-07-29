export PYTHONPATH=./

python tools/train.py --config-file ./configs/tractors_and_combines_synth/semseg-oacnns-v1m1-0-base.py --num-gpus 2 --options save_path=exp/tgc_synth_oacnns
