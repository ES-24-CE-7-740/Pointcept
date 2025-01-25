#!/bin/bash
export PYTHONPATH=./
python tools/test.py --config-file ./configs/agco_real_no_annot/semseg-oacnn-base-gen-preds.py --options save_path=/workspace/Pointcept/exp/pseudo_labeling_test 
