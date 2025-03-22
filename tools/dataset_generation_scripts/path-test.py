import os
from pathlib import Path
import numpy as np


# NOTE: CURRENT IMPLEMENTATION DOES NOT ALLOW SYNTH AND TRAIN SEQS WITH SAME NAME
#       eg. this is not allowed:
#           synth_train_seqs = [01]
#           real_train_seqs = [00, 01]

### Config ######################################
save_dir = Path("data").absolute()

root_synth = Path("data/tractors_and_combines_synth")
synth_train_seqs = ['10']

root_real = Path("data/tractors_and_combines_real")
real_train_seqs = ['00', '01']
real_val_seqs = ['03_val']
real_test_seqs = ['02_test']

n_datapoints_list = [
    200,
    400,
    600,
    800,
    1000,
    1200,
]
#################################################

print(save_dir)
print(root_synth.absolute())
print(root_real.absolute())
