weight = '/workspace/Pointcept/exp/pretrain_oacnns_on_synth_wml_end/model/model_best.pth'
resume = False
evaluate = True
test_only = True
seed = 25965751
save_path = 'tests/oa_wml_29ep_test_on_all'
num_worker = 12
batch_size = 14
batch_size_val = None
batch_size_test = None
epoch = 50
eval_epoch = 50
clip_grad = None
sync_bn = True
enable_amp = True
empty_cache = True
empty_cache_per_epoch = False
find_unused_parameters = False
mix_prob = 0.8
param_dicts = None
hooks = [
    dict(type='CheckpointLoader'),
    dict(type='IterationTimer', warmup_iter=2),
    dict(type='InformationWriter'),
    dict(type='SemSegEvaluator'),
    dict(type='CheckpointSaver', save_freq=None),
    dict(type='PreciseEvaluator', test_last=False)
]
train = dict(type='DefaultTrainer')
test = dict(type='SemSegTester', verbose=True)
num_worker_per_gpu = 2
data_root = '/workspace/ttgch_real_wml/'
n_classes = 12
model = dict(
    type='DefaultSegmentor',
    backbone=dict(
        type='OACNNs',
        in_channels=3,
        num_classes=12,
        embed_channels=64,
        enc_channels=[64, 64, 128, 256],
        groups=[4, 4, 8, 16],
        enc_depth=[3, 3, 9, 8],
        dec_channels=[256, 256, 256, 256],
        point_grid_size=[[8, 12, 16, 16], [6, 9, 12, 12], [4, 6, 8, 8],
                         [3, 4, 6, 6]],
        dec_depth=[2, 2, 2, 2],
        enc_num_ref=[16, 16, 16, 16]),
    criteria=[dict(type='CrossEntropyLoss', loss_weight=1.0, ignore_index=-1)])
optimizer = dict(type='AdamW', lr=0.002, weight_decay=0.005)
scheduler = dict(
    type='OneCycleLR',
    max_lr=0.002,
    pct_start=0.04,
    anneal_strategy='cos',
    div_factor=10.0,
    final_div_factor=100.0)
dataset_type = 'TTGCHRealDataset'
ignore_index = -1
names = [
    'ground', 'unkown_tractor', 'blue_valtra', 'grey_valtra',
    'valtra_with_forks', 'deer_krammer', 'massey', 'unknown_combine_harvester',
    'fendt_paralevel', 'ideal_10t', 'laverda', 'trailer'
]
data = dict(
    num_classes=12,
    ignore_index=-1,
    names=[
        'ground', 'unkown_tractor', 'blue_valtra', 'grey_valtra',
        'valtra_with_forks', 'deer_krammer', 'massey',
        'unknown_combine_harvester', 'fendt_paralevel', 'ideal_10t', 'laverda',
        'trailer'
    ],
    train=dict(
        type='TTGCHRealDataset',
        split='train',
        data_root='/workspace/ttgch_real_wml/',
        transform=[
            dict(
                type='RandomRotate',
                angle=[-1, 1],
                axis='z',
                center=[0, 0, 0],
                p=0.5),
            dict(type='RandomScale', scale=[0.9, 1.1]),
            dict(type='RandomFlip', p=0.5),
            dict(type='RandomJitter', sigma=0.005, clip=0.02),
            dict(
                type='GridSample',
                grid_size=0.05,
                hash_type='fnv',
                mode='train',
                keys=('coord', 'segment'),
                return_grid_coord=True),
            dict(
                type='PointClip',
                point_cloud_range=(-35.2, -35.2, -4, 35.2, 35.2, 2)),
            dict(type='SphereCrop', sample_rate=0.8, mode='random'),
            dict(type='SphereCrop', point_max=120000, mode='random'),
            dict(type='ToTensor'),
            dict(
                type='Collect',
                keys=('coord', 'grid_coord', 'segment'),
                feat_keys='coord')
        ],
        test_mode=False,
        ignore_index=-1,
        loop=1),
    val=dict(
        type='TTGCHRealDataset',
        split='val',
        data_root='/workspace/ttgch_real_wml/',
        transform=[
            dict(
                type='GridSample',
                grid_size=0.05,
                hash_type='fnv',
                mode='train',
                keys=('coord', 'segment'),
                return_grid_coord=True),
            dict(
                type='PointClip',
                point_cloud_range=(-35.2, -35.2, -4, 35.2, 35.2, 2)),
            dict(type='ToTensor'),
            dict(
                type='Collect',
                keys=('coord', 'grid_coord', 'segment'),
                feat_keys='coord')
        ],
        test_mode=False,
        ignore_index=-1),
    test=dict(
        type='TTGCHRealDataset',
        split='test',
        data_root='/workspace/ttgch_real_wml/',
        transform=[],
        test_mode=True,
        test_cfg=dict(
            voxelize=dict(
                type='GridSample',
                grid_size=0.05,
                hash_type='fnv',
                mode='test',
                return_grid_coord=True,
                keys='coord'),
            crop=None,
            post_transform=[
                dict(
                    type='PointClip',
                    point_cloud_range=(-35.2, -35.2, -4, 35.2, 35.2, 2)),
                dict(type='ToTensor'),
                dict(
                    type='Collect',
                    keys=('coord', 'grid_coord', 'index'),
                    feat_keys='coord')
            ],
            aug_transform=[[{
                'type': 'RandomRotateTargetAngle',
                'angle': [0],
                'axis': 'z',
                'center': [0, 0, 0],
                'p': 1
            }],
                           [{
                               'type': 'RandomRotateTargetAngle',
                               'angle': [0.5],
                               'axis': 'z',
                               'center': [0, 0, 0],
                               'p': 1
                           }],
                           [{
                               'type': 'RandomRotateTargetAngle',
                               'angle': [1],
                               'axis': 'z',
                               'center': [0, 0, 0],
                               'p': 1
                           }],
                           [{
                               'type': 'RandomRotateTargetAngle',
                               'angle': [1.5],
                               'axis': 'z',
                               'center': [0, 0, 0],
                               'p': 1
                           }]]),
        ignore_index=-1))
