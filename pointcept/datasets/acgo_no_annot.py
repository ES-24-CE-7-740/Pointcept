"""
tractors and combines real dataset

Author: Xiaoyang Wu (xiaoyang.wu.cs@gmail.com) (edited)
Please cite our work if the code is helpful to you.
"""

import os
import numpy as np
from .builder import DATASETS
from .defaults import DefaultDataset

@DATASETS.register_module()
class AGCORawDataset(DefaultDataset):
    def __init__(self, ignore_index=-1, **kwargs):
        super().__init__(ignore_index=ignore_index, **kwargs)

    def get_data_list(self):
        split2seq = dict(
            train=[0],
            val=[0],
            test=[0,1,2,3,4,5,6,7],
        )
        if isinstance(self.split, str):
            seq_list = split2seq[self.split]
        elif isinstance(self.split, list):
            seq_list = []
            for split in self.split:
                seq_list += split2seq[split]
        else:
            raise NotImplementedError

        data_list = []
        all_seq_dirs = sorted(os.listdir(os.path.join(self.data_root, "dataset","seqs_raw")))
        
        for seq in seq_list:
            # seq = str(seq).zfill(2)
            seq = all_seq_dirs[seq]
            seq_folder = os.path.join(self.data_root, "dataset", "seqs_raw", seq)
            seq_files = sorted(os.listdir(os.path.join(seq_folder, "points_npy")))
            data_list += [
                os.path.join(seq_folder, "points_npy", file) for file in seq_files
            ]
        return data_list

    def get_data(self, idx):
        data_path = self.data_list[idx % len(self.data_list)]
        with open(data_path, "rb") as b:
            scan = np.load(b).astype(np.float32)
        coord = scan[:, :3]
        segment = np.zeros_like(coord[:,1]).astype(np.int32)

        data_dict = dict(
            coord=coord,
            segment=segment,
            name=self.get_data_name(idx),
            fragment_list=[1,2],
        )
        return data_dict

    def get_data_name(self, idx):
        file_path = self.data_list[idx % len(self.data_list)]
        dir_path, file_name = os.path.split(file_path)
        sequence_name = os.path.basename(os.path.dirname(dir_path))
        frame_name = os.path.splitext(file_name)[0]
        data_name = f"{sequence_name}_{frame_name}"
        return data_name


