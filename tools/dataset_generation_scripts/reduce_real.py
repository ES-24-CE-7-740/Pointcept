import os
from pathlib import Path
import numpy as np


### Config ######################################
root = Path("data/tractors_and_combines_real")
train_sequences = ['00', '01']
validate_sequences = ['03_val']
test_sequences = ['02_test']

n_datapoints_list = [
    200,
    400,
    600,
    800,
    1000,
]
#################################################




# Initialize lists for points and labels
train_points = []
train_labels = []

# Create two lists containing all training data paths
for seq in train_sequences:
    sequence_path = root / 'dataset' / 'Sequences' / seq
    points_path = sequence_path / 'points'
    labels_path = sequence_path / 'labels'

    # Add points and labels to the respective lists
    train_points.extend(points_path.iterdir())
    train_points = sorted(train_points)
    train_labels.extend(labels_path.iterdir())
    train_labels = sorted(train_labels)
    

# Create reduced dataset for each amount in n_datapoints_list
for n_datapoints in n_datapoints_list:

    # Sample the training sequences with n_datapoints
    for idx in np.linspace(0, len(train_points)-1, n_datapoints).astype(np.int16):#range(0, len(train_points), 6):
        
        # Define point cloud and label paths
        point_path: Path = train_points[idx]
        label_path: Path = train_labels[idx]
        
        
        for path in [point_path, label_path]:
            # Define save path
            save_path_parts = list(path.parts)
            save_path_parts.insert(-5, 'reduced')
            save_path_parts.insert(-5, f'{n_datapoints}')
            save_path = Path(*save_path_parts)
            
            # Create save directory
            os.makedirs(save_path.parent.absolute(), exist_ok=True)
            
            # Create symlink to file path
            save_path.symlink_to(path.absolute())
        

    # Copy the validate and test sequences
    for seq in (validate_sequences + test_sequences):
        sequence_path = root / 'dataset' / 'Sequences' / seq
        symlink_sequence_path = root / 'reduced' / f'{n_datapoints}' / 'dataset' / 'Sequences' / seq
        
        # Create dir
        os.makedirs(symlink_sequence_path.parent, exist_ok=True)
        
        # Create symlink
        symlink_sequence_path.symlink_to(sequence_path.absolute(), target_is_directory=True)
    
    