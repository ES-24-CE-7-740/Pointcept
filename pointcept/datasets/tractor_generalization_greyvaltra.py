"""
tractors and combines synth dataset

Author: Xiaoyang Wu (xiaoyang.wu.cs@gmail.com) (edited)
Please cite our work if the code is helpful to you.
"""

import os
import numpy as np

from .builder import DATASETS
from .defaults import DefaultDataset


@DATASETS.register_module()
class TractorGeneralizationGreyValtraDataset(DefaultDataset):
    def __init__(self, ignore_index=-1, **kwargs):
        self.ignore_index = ignore_index
        self.learning_map = self.get_learning_map(ignore_index)
        self.learning_map_inv = self.get_learning_map_inv(ignore_index)
        super().__init__(ignore_index=ignore_index, **kwargs)

    def get_data_list(self):
        split2seq = dict(
            train=['012',],
            val=['112',],
            test=['3000', '3001', '3002', '3005', '3007',],
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
        for seq in seq_list:
            seq = str(seq).zfill(3)
            seq_folder = os.path.join(self.data_root, "dataset", "sets", seq)
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
        strength = scan[:, -1].reshape([-1, 1])

        label_file = data_path.replace("points", "labels")
        if os.path.exists(label_file):
            with open(label_file, "rb") as a:
                segment = np.round(np.load(a)).astype(np.uint32).reshape(-1).astype(np.int32)
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
            41:2,
            20:2,
            21:2,
            22:2,
            23:2,
            10:2,
            11:1,
            12:1,
            13:1,
            14:1,
            15:1,
            16:1,
            17:1,
            18:1,
            19:1,
            30:0,
            0:0,
            1:0,
        }
        return learning_map

    @staticmethod
    def get_learning_map_inv(ignore_index):
        learning_map_inv = {
            ignore_index: ignore_index,
            2:20,
            1:10,
            0:0,
        }
        return learning_map_inv





# @staticmethod
# def get_learning_map(ignore_index):
#     learning_map = {
#         ignore_index: ignore_index,
#         41:3,
#         20:3,
#         21:3,
#         22:3,
#         23:3,
#         10:3,
#         11:2,
#         12:2,
#         13:2,
#         14:2,
#         15:2,
#         16:2,
#         17:2,
#         18:2,
#         19:2,
#         30:1,
#         0:0,
#         1:0,
#     }
#     return learning_map

# @staticmethod
# def get_learning_map_inv(ignore_index):
#     learning_map_inv = {
#         ignore_index: ignore_index,
#         3:20,
#         2:10,
#         1:30,
#         0:0,
#     }
#     return learning_map_inv