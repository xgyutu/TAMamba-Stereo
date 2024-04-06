from .kitti_dataset_1215 import KITTIDataset
# from .kitti_dataset_1215_augmentation import KITTIDataset
from .sceneflow_dataset import SceneFlowDatset

__datasets__ = {
    "sceneflow": SceneFlowDatset,
    "kitti": KITTIDataset
}
