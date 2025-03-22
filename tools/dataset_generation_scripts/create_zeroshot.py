import os
from pathlib import Path
import numpy as np


# NOTE: CURRENT IMPLEMENTATION DOES NOT ALLOW SYNTH AND TRAIN SEQS WITH SAME NAME
#       eg. this is not allowed:
#           synth_train_seqs = ['01']
#           real_train_seqs = ['00', '01']

### Config ######################################
save_dir = Path("data").absolute()

root_synth = Path("data/tractors_and_combines_synth")
synth_train_seqs = ['02', '03', '04', '05', '06', '07', '08', '09', '10']
synth_val_seqs = ['00'] # max 00->09

root_real = Path("data/dec_both_cfg_wml")
real_test_seqs = ['005', '104', '001', '007', '103', '106',] # max 00->09

#################################################




# Initialize lists for points and labels
synth_train_points = []
synth_train_labels = []
val_points = []
val_labels = []
test_points = []
test_labels = []

# Go through synth seqs
for seq in synth_train_seqs:
    sequence_path = root_synth / 'dataset' / 'sets' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'
    
    synth_train_points.append(points_path.iterdir())
    synth_train_labels.append(labels_path.iterdir())

for idx in range(len(synth_train_points)):
    synth_train_points[idx] = sorted(synth_train_points[idx])
    synth_train_labels[idx] = sorted(synth_train_labels[idx])


# Go through validatation seqs
for seq in synth_val_seqs:
    sequence_path = root_synth / 'dataset' / 'sets' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    val_points.append(points_path.iterdir())
    val_labels.append(labels_path.iterdir())
    
for idx in range(len(val_points)):
    val_points[idx] = sorted(val_points[idx])
    val_labels[idx] = sorted(val_labels[idx])
    
    
# Go through test seqs
for seq in real_test_seqs:
    sequence_path = root_real / 'dataset' / 'Sequences' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    test_points.append(points_path.iterdir())
    test_labels.append(labels_path.iterdir())
    
for idx in range(len(test_points)):
    test_points[idx] = sorted(test_points[idx])
    test_labels[idx] = sorted(test_labels[idx])


def symlinker(path_list, new_seq_path, prefix = None, max_length = 3):
    for path in path_list:
        
        # Define save path
        save_path_parts = list(path.parts)
        
        # If sequence name is longer than max_length characters, it is cropped
        if len(save_path_parts[-3]) > max_length:
            new_seq_name = save_path_parts[-3][:max_length]
            save_path_parts[-3] = new_seq_name

        if prefix is not None:
            new_seq_name = str(prefix) + save_path_parts[-3][0:]
            save_path_parts[-3] = new_seq_name

        
        # Get the defining part containing the sequence, point/label, filename
        file_path = Path(*save_path_parts[-3:])
        
        # Add prefix
        if prefix is not None:
            new_filename = str(prefix) + file_path.name[0:]
            file_path = file_path.parent / new_filename
        
        # Define the new save path
        save_path = new_seq_path / file_path
        
        # Create dir
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create symlink to file path
        save_path.symlink_to(path.absolute())



print(f"Processing zeroshot dataset...")

#save_root = save_dir / "tractors_and_combines_zeroshot" / "dataset" / "sets"
save_root = save_dir / "tractors_and_combines_ablation" / "dataset" / "sets"

# Symlink the synthetic sequences
for synth_seq in zip(synth_train_points, synth_train_labels):
    symlinker(path_list=synth_seq[0], new_seq_path=save_root, prefix=1)
    symlinker(path_list=synth_seq[1], new_seq_path=save_root, prefix=1)

# Symlink validation sequences
for val_seq in zip(val_points, val_labels):
    symlinker(path_list=val_seq[0], new_seq_path=save_root, prefix=2)
    symlinker(path_list=val_seq[1], new_seq_path=save_root, prefix=2)

# Symlink testing sequences
for test_seq in zip(test_points, test_labels):
    symlinker(path_list=test_seq[0], new_seq_path=save_root, prefix=3)
    symlinker(path_list=test_seq[1], new_seq_path=save_root, prefix=3)