import os
from pathlib import Path
import numpy as np
from tqdm import tqdm

### Config ######################################
save_dir = Path("data").absolute()
dataset_name =  "agco_all_real_only"

root_synth = Path("data/agco_all_synth")
synth_train_seqs = ['010']

root_real = Path("data/agco_all_real_only")
real_train_seqs = ['1001', '1003', '1102', '1103', '1104', '1105', '1106', '1107',] # '1109'
real_val_seqs = ['2101', '2108',]
real_test_seqs = ['3000', '3001', '3002', '3005', '3007',]

n_datapoints_list = [
    1000,
    2000,
    3000,
    4000,
    5000,
]
#################################################




# Initialize lists for points and labels
synth_train_points = []
synth_train_labels = []
real_train_points = []
real_train_labels = []
test_val_points = []
test_val_labels = []
#filecnt = 0

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
    sequence_path = root_real / 'dataset' / 'sets' / seq
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
    sequence_path = root_real / 'dataset' / 'sets' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    test_val_points.append(points_path.iterdir())
    test_val_labels.append(labels_path.iterdir())
    
for idx in range(len(test_val_points)):
    test_val_points[idx] = sorted(test_val_points[idx])
    test_val_labels[idx] = sorted(test_val_labels[idx])



def symlinker(path_list, new_seq_path, prefix = None, length=4):
    # global filecnt
    filecnt = 0
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

        
        # Get the defining part containing the sequence, point/label, filename
        file_path = Path(*save_path_parts[-3:])
        
        # Add prefix
        # if prefix is not None:
        #     new_filename = str(prefix) + file_path.name[1:]
        #     file_path = file_path.parent / new_filename
        
        if prefix is not None:
            new_filename = f"{prefix:03d}_" + f"{filecnt:05d}.npy"  # Adds a zero-padded prefix
            file_path = file_path.parent / new_filename
            filecnt += 1
        
        # Define the new save path
        save_path = new_seq_path / file_path
        
        # Create dir
        save_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create symlink to file path
        save_path.symlink_to(path.absolute())



# Create reduced dataset for each amount in n_datapoints_list
#pre = 0
for n_datapoints in tqdm(n_datapoints_list, desc=f"Symlinking..."):
    print(f"Processing combined dataset using {n_datapoints} real point clouds...")
    
    save_root = save_dir / dataset_name / f"{n_datapoints}" / "dataset" / "sets"
    upsample_ratio = round(sum([len(seq) for seq in synth_train_points]) / n_datapoints, 2)
    
    
    for train_seq in zip(real_train_points, real_train_labels):
        
        cropped_train_seq_points = train_seq[0][:n_datapoints//len(real_train_seqs)]
        cropped_train_seq_labels = train_seq[1][:n_datapoints//len(real_train_seqs)]
        
        # Match amount of real to amount of synth
        for prefix in range(int(upsample_ratio)):
            symlinker(path_list=cropped_train_seq_points, new_seq_path=save_root, prefix=prefix)
            symlinker(path_list=cropped_train_seq_labels, new_seq_path=save_root, prefix=prefix)
            #pre += 1
        
        # Match it to sub real set length precision
        if round(upsample_ratio % 1, 2) >= 0.01:
            # Calculate missing amount
            n_points_missing = int((n_datapoints//len(real_train_seqs)) * round(upsample_ratio % 1, 2))
            
            # Symlink missing amount
            symlinker(path_list=train_seq[0][:n_points_missing], new_seq_path=save_root, prefix=prefix + 1)
            symlinker(path_list=train_seq[1][:n_points_missing], new_seq_path=save_root, prefix=prefix + 1)
            #pre += 1
            
    
    # Symlink the synthetic sequences
    for synth_seq in zip(synth_train_points, synth_train_labels):
        symlinker(path_list=synth_seq[0], new_seq_path=save_root)
        symlinker(path_list=synth_seq[1], new_seq_path=save_root)
    
    # Symlink validation and testing sequences
    for test_val_seq in zip(test_val_points, test_val_labels):
        symlinker(path_list=test_val_seq[0], new_seq_path=save_root)
        symlinker(path_list=test_val_seq[1], new_seq_path=save_root)
    
    
    # Write recipe to file
    with open(f"{save_root}/recipe.txt", "a") as file:
        file.write(f"root_synth: {root_synth}\n")
        file.write(f"synth_train_seqs: {synth_train_seqs}\n")
        file.write(f"\n")
        file.write(f"root_real: {root_real}\n")
        file.write(f"real_train_seqs: {real_train_seqs}\n")
        file.write(f"real_val_seqs: {real_val_seqs}\n")
        file.write(f"real_test_seqs: {real_test_seqs}\n")
    