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
class TractorsAndCombinesRealDataset(DefaultDataset):
    def __init__(self, ignore_index=-1, **kwargs):
        self.ignore_index = ignore_index
        self.learning_map = self.get_learning_map(ignore_index)
        self.learning_map_inv = self.get_learning_map_inv(ignore_index)
        super().__init__(ignore_index=ignore_index, **kwargs)

    def get_data_list(self):
        split2seq = dict(
            train=[0,1],
            val=[3],
            test=[2],
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
        all_seq_dirs = sorted(os.listdir(os.path.join(self.data_root, "dataset", "Sequences")))
        
        for seq in seq_list:
            # seq = str(seq).zfill(2)
            seq = all_seq_dirs[seq]
            seq_folder = os.path.join(self.data_root, "dataset", "Sequences", seq)
            seq_files = sorted(os.listdir(os.path.join(seq_folder, "points")))
            data_list += [
                os.path.join(seq_folder, "points", file) for file in seq_files
            ]
        return data_list

    def get_data(self, idx):
        data_path = self.data_list[idx % len(self.data_list)]
        with open(data_path, "rb") as b:
            scan = np.load(b).astype(np.float32)
        coord = scan[:, :3]
        strength = np.zeros_like(scan[:, -1]).reshape([-1, 1])

        label_file = data_path.replace("points", "labels")
        if os.path.exists(label_file):
            with open(label_file, "rb") as a:
                segment = np.round(np.load(a)).astype(np.uint32)#.reshape(-1).astype(np.int32)
                segment = np.vectorize(self.learning_map.__getitem__)(
                    segment & 0xFFFF
                ).astype(np.int32)
        else:
            raise Exception("no labels found") 
            segment = np.zeros(scan.shape[0]).astype(np.int32)
        
        # if np.sum(segment) != 0:
        #     raise Exception(f"2 in labels {label_file}, {np.sum(segment == 2)}")

        data_dict = dict(
            coord=coord,
            # strength=strength,
            segment=segment,
            name=self.get_data_name(idx),
        )
        return data_dict

    def get_data_name(self, idx):
        file_path = self.data_list[idx % len(self.data_list)]
        dir_path, file_name = os.path.split(file_path)
        sequence_name = os.path.basename(os.path.dirname(dir_path))
        frame_name = os.path.splitext(file_name)[0]
        data_name = f"{sequence_name}_{frame_name}"
        return data_name

    @staticmethod
    def get_learning_map(ignore_index):
        learning_map = {
            ignore_index: ignore_index,
            0: 0,  # "unlabeled"
            1: 1, # "tractor"
            2: 2, # "combine"
            3: 0, # "trailer"
        }
        return learning_map

    @staticmethod
    def get_learning_map_inv(ignore_index):
        learning_map_inv = {
            ignore_index: ignore_index,
            0: 0,  # "unlabeled"
            1: 1, # "tractor"
            2: 2, # "combine"
            -1: 0,

        }
        return learning_map_inv
