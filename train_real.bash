export PYTHONPATH=./

python tools/train.py --config-file ./configs/ttgch_with_model_labels/real/semseg-oacnns-v1m1-0-base.py --num-gpus 2 --options save_path=exp/tgc_real_oacnns_from_synth_pretrain2  
