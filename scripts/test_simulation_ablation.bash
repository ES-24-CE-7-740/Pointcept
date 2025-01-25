#!/bin/bash
export PYTHONPATH=./
#python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/simulation_ablation_base weight=/workspace/Pointcept/exp/simulation_ablation_base/model/model_last.pth & 
#python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/simulation_ablation_grass weight=/workspace/Pointcept/exp/simulation_ablation_grass/model/model_last.pth &
#python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/simulation_ablation_occlusion weight=/workspace/Pointcept/exp/simulation_ablation_occlusion/model/model_last.pth &
#python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/simulation_ablation_ublobs weight=/workspace/Pointcept/exp/simulation_ablation_ublobs/model/model_last.pth &
python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/simulation_ablation_full2 weight=/workspace/Pointcept/exp/simulation_ablation_full2/model/model_last.pth &

