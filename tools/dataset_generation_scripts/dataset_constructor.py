import os
from pathlib import Path
import numpy as np
from tqdm import tqdm


# NOTE: CURRENT IMPLEMENTATION DOES NOT ALLOW SEQS WITH SAME NAME WITHIN EACH SPLIT
#       eg. this is not allowed:
#           train_data = {
#               Path("data/tractors_and_combines_synth"): ['04', '05',],
#               Path("data/dec_both_cfg_wml"): ['04', '05',],
#           }

### Config ######################################
save_dir = Path("data").absolute()
dataset_name = "tractors_and_combines_ablation"

train_data = { # [003] -> [015]
    Path("data/agco_all_synth"): ['003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015',],
}

validation_data = { # [001] [002]
    Path("data/agco_all_synth"): ['001', '002'],
}

# oct000, oct002, dec005, dec001
# oct000, oct002, dec005, dec001, dec007
test_data = { 
    Path("data/october_wml"): ['000', '002'],
    Path("data/dec_both_cfg_wml"): ['001', '005', '007',],
}

#################################################




# Initialize lists for points and labels
train_points = []
train_labels = []
val_points = []
val_labels = []
test_points = []
test_labels = []

# Go through train seqs
for train_root, train_seqs in train_data.items():
    for seq in train_seqs:
        sequence_path = train_root / 'dataset' / 'sets' / seq
        points_path = sequence_path / 'points'
        labels_path = sequence_path / 'labels'
        
        train_points.append(points_path.iterdir())
        train_labels.append(labels_path.iterdir())

for idx in range(len(train_points)):
    train_points[idx] = sorted(train_points[idx])
    train_labels[idx] = sorted(train_labels[idx])


# Go through validatation seqs
for val_root, val_seqs in validation_data.items():
    for seq in val_seqs:
        sequence_path = val_root / 'dataset' / 'sets' / seq
        points_path = sequence_path / 'points'
        labels_path = sequence_path / 'labels'

        # Add points and labels to the respective lists
        val_points.append(points_path.iterdir())
        val_labels.append(labels_path.iterdir())
    
for idx in range(len(val_points)):
    val_points[idx] = sorted(val_points[idx])
    val_labels[idx] = sorted(val_labels[idx])
    
    
# Go through test seqs
for test_root, test_seqs in test_data.items():
    for seq in test_seqs:
        sequence_path = test_root / 'dataset' / 'sets' / seq
        points_path = sequence_path / 'points'
        labels_path = sequence_path / 'labels'

        # Add points and labels to the respective lists
        test_points.append(points_path.iterdir())
        test_labels.append(labels_path.iterdir())
    
for idx in range(len(test_points)):
    test_points[idx] = sorted(test_points[idx])
    test_labels[idx] = sorted(test_labels[idx])


def symlinker(path_list, new_seq_path, prefix = None, length = 3): # length is without prefix
    for path in path_list:
        
        # Define save path
        save_path_parts = list(path.parts)
        
        # If sequence name is longer than max_length characters, it is cropped
        if len(save_path_parts[-3]) > length:
            new_seq_name = save_path_parts[-3][:length]
            save_path_parts[-3] = new_seq_name
        
        elif len(save_path_parts[-3]) < length:
            new_seq_name = save_path_parts[-3].zfill(length)
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



print(f"Processing dataset...")

#save_root = save_dir / "tractors_and_combines_zeroshot" / "dataset" / "sets"
save_root = save_dir / f"{dataset_name}" / "dataset" / "sets"

# Symlink the train sequences
for synth_seq in tqdm(zip(train_points, train_labels), desc="Symlinking the train sequences...", total=len(train_points)):
    symlinker(path_list=synth_seq[0], new_seq_path=save_root, prefix=1)
    symlinker(path_list=synth_seq[1], new_seq_path=save_root, prefix=1)

# Symlink validation sequences
for val_seq in tqdm(zip(val_points, val_labels), desc="Symlinking the validation sequences...", total=len(val_points)):
    symlinker(path_list=val_seq[0], new_seq_path=save_root, prefix=2)
    symlinker(path_list=val_seq[1], new_seq_path=save_root, prefix=2)

# Symlink testing sequences
for test_seq in tqdm(zip(test_points, test_labels), desc="Symlinking the test sequences...", total=len(test_points)):
    symlinker(path_list=test_seq[0], new_seq_path=save_root, prefix=3)
    symlinker(path_list=test_seq[1], new_seq_path=save_root, prefix=3)