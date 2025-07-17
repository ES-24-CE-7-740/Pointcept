import os 
import numpy as np 
from tqdm import tqdm


dataset_root = "/work/3dgs-drive/data/agco_all_synth/dataset/sets"

seqs = sorted(os.listdir(dataset_root))

rm_cnt = 0

for seq in tqdm(seqs):
    for label_fn in sorted(os.listdir(os.path.join(dataset_root, seq, "labels"))):
        label_path = os.path.join(dataset_root, seq, "labels",label_fn)
      
        point_path = label_path.replace("labels","points")
        label_vec = np.load(label_path)
        

        if label_vec.shape[0] < 100 or label_vec.shape[0] > 100000:
            os.remove(label_path)
            os.remove(point_path)
            rm_cnt += 1

print(rm_cnt)