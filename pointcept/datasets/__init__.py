from .defaults import DefaultDataset, ConcatDataset
from .builder import build_dataset
from .utils import point_collate_fn, collate_fn

# indoor scene
from .s3dis import S3DISDataset
from .scannet import ScanNetDataset, ScanNet200Dataset
from .scannetpp import ScanNetPPDataset
from .scannet_pair import ScanNetPairDataset
from .arkitscenes import ArkitScenesDataset
from .structure3d import Structured3DDataset

# outdoor scene
from .semantic_kitti import SemanticKITTIDataset
from .nuscenes import NuScenesDataset
from .waymo import WaymoDataset
from .tractors_and_combines_synth import TractorsAndCombinesSynthDataset
from .tractors_and_combines_dec import TractorsAndCombinesDecDataset

from .ttgch_real_wml import TTGCHRealDataset
from .ttgch_synth_wml import TTGCHSynthDataset
# object
from .modelnet import ModelNetDataset
from .shapenet_part import ShapeNetPartDataset

# dataloader
from .dataloader import MultiDatasetDataloader

# Real only dataset
from .tractors_and_combines_real import TractorsAndCombinesRealDataset # Old
from .tractors_and_combines_real_v2 import TractorsAndCombinesRealV2Dataset # Includes new data

# Combined dataset
from .tractors_and_combines_combined import TractorsAndCombinesCombinedDataset # Old
from .tractors_and_combines_combined_v2 import TractorsAndCombinesCombinedV2Dataset # Includes new data

# Ablation dataset
from .tractors_and_combines_dec_ablation import TractorsAndCombinesDecAblationDataset

# Tractor generalization
from .tractor_generalization_bluevaltra import TractorGeneralizationBlueValtraDataset
from .tractor_generalization_greyvaltra import TractorGeneralizationGreyValtraDataset
from .tractor_generalization_fendt300 import TractorGeneralizationFendt300Dataset
from .tractor_generalization_fendt1000 import TractorGeneralizationFendt1000Dataset
from .tractor_generalization_orangevaltra import TractorGeneralizationOrangeValtraDataset
from .tractor_generalization_forkvaltra import TractorGeneralizationForkValtraDataset
