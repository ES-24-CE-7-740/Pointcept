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




# Initialize lists for points and labels
synth_train_points = []
synth_train_labels = []
real_train_points = []
real_train_labels = []
test_val_points = []
test_val_labels = []

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


# Go through real seqs
for seq in real_train_seqs:
    sequence_path = root_real / 'dataset' / 'Sequences' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    real_train_points.append(points_path.iterdir())
    real_train_labels.append(labels_path.iterdir())
    
for idx in range(len(real_train_points)):
    real_train_points[idx] = sorted(real_train_points[idx])
    real_train_labels[idx] = sorted(real_train_labels[idx])


# Go through validatation and test seqs
for seq in (real_val_seqs + real_test_seqs):
    sequence_path = root_real / 'dataset' / 'Sequences' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    test_val_points.append(points_path.iterdir())
    test_val_labels.append(labels_path.iterdir())
    
for idx in range(len(test_val_points)):
    test_val_points[idx] = sorted(test_val_points[idx])
    test_val_labels[idx] = sorted(test_val_labels[idx])


def symlinker(path_list, new_seq_path, prefix = None):
    for path in path_list:
        
        # Define save path
        save_path_parts = list(path.parts)
        
        # If sequence name is longer than two characters, it is cropped
        if len(save_path_parts[-3]) > 2:
            new_seq_name = save_path_parts[-3][:2]
            save_path_parts[-3] = new_seq_name

        
        # Get the defining part containing the sequence, point/label, filename
        file_path = Path(*save_path_parts[-3:])
        
        # Add prefix
        if prefix is not None:
            new_filename = str(prefix) + file_path.name[1:]
            file_path = file_path.parent / new_filename
        
        # Define the new save path
        save_path = new_seq_path / file_path
        
        # Create dir
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create symlink to file path
        save_path.symlink_to(path.absolute())



# Create reduced dataset for each amount in n_datapoints_list
for n_datapoints in n_datapoints_list:
    print(f"Processing combined dataset using {n_datapoints} real point clouds...")
    
    save_root = save_dir / "tractors_and_combines_combined" / f"{n_datapoints}" / "dataset" / "sets"
    upsample_ratio = round(sum([len(seq) for seq in synth_train_points]) / n_datapoints, 2)
    
    for train_seq in zip(real_train_points, real_train_labels):
        
        cropped_train_seq_points = train_seq[0][:n_datapoints//len(real_train_seqs)]
        cropped_train_seq_labels = train_seq[1][:n_datapoints//len(real_train_seqs)]
        
        # Match amount of real to amount of synth
        for prefix in range(int(upsample_ratio)):
            symlinker(path_list=cropped_train_seq_points, new_seq_path=save_root, prefix=prefix)
            symlinker(path_list=cropped_train_seq_labels, new_seq_path=save_root, prefix=prefix)
        
        # Match it to sub real set length precision
        if round(upsample_ratio % 1, 2) >= 0.01:
            # Calculate missing amount
            n_points_missing = int((n_datapoints//len(real_train_seqs)) * round(upsample_ratio % 1, 2))
            
            # Symlink missing amount
            symlinker(path_list=train_seq[0][:n_points_missing], new_seq_path=save_root, prefix=prefix + 1)
            symlinker(path_list=train_seq[1][:n_points_missing], new_seq_path=save_root, prefix=prefix + 1)
            
    
    # Symlink the synthetic sequences
    for synth_seq in zip(synth_train_points, synth_train_labels):
        symlinker(path_list=synth_seq[0], new_seq_path=save_root)
        symlinker(path_list=synth_seq[1], new_seq_path=save_root)
    
    # Symlink validation and testing sequences
    for test_val_seq in zip(test_val_points, test_val_labels):
        symlinker(path_list=test_val_seq[0], new_seq_path=save_root)
        symlinker(path_list=test_val_seq[1], new_seq_path=save_root)
    