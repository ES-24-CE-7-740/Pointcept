#!/bin/bash
export PYTHONPATH=./
# python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_200 weight=/workspace/oa_cnn_real_only_weights/OACNN_200/model/model_best.pth & 
# python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_400 weight=/workspace/oa_cnn_real_only_weights/OACNN_400/model/model_best.pth & 
# python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_600 weight=/workspace/oa_cnn_real_only_weights/OACNN_600/model/model_best.pth &
# python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_800 weight=/workspace/oa_cnn_real_only_weights/OACNN_800/model/model_best.pth &
python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_1000 weight=/workspace/oa_cnn_real_only_weights/OACNN_1000/model/model_best.pth &
python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_real_only/OACNN_1200 weight=/workspace/oa_cnn_real_only_weights/OACNN_1200/model/model_best.pth & 
python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_mixed/OACNN_1000 weight=/workspace/oa_cnn_mixed_weights/OACNN_1000/model/model_best.pth &
python tools/test.py --config-file ./configs/agco_real_testing/semseg-oa-real-test.py --options save_path=/workspace/Pointcept/exp/oacnn_mixed/OACNN_1200 weight=/workspace/oa_cnn_mixed_weights/OACNN_1200/model/model_best.pth
