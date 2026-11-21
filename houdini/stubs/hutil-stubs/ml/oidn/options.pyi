# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from typing import Literal

def get_default_device() -> Literal['cuda', 'mps', 'cpu']: ...

class PreProcessOptions:
    """
    Intel(R) Open Image Denoise - Training
    usage: preprocess.py [-h]

    Preprocesses training and validation datasets.

    positional arguments:
    {hdr,ldr,sh1,albedo,alb,normal,nrm,[]}
                            set of input features

    options:
    -h, --help            show this help message and exit
    --config CONFIG, -c CONFIG
                            load configuration from JSON file (overrides command-line arguments)
    --clean_aux           train with noise-free (reference) auxiliary features
    --filter {RT,RTLightmap}, -f {RT,RTLightmap}
                            filter to train (determines some default arguments)
    --preproc_dir PREPROC_DIR, -P PREPROC_DIR
                            directory of preprocessed datasets
    --train_data TRAIN_DATA, -t TRAIN_DATA
                            name of the training dataset
    --valid_data VALID_DATA, -v VALID_DATA
                            name of the validation dataset
    --data_dir DATA_DIR, -D DATA_DIR
                            directory of datasets (e.g. training, validation, test)
    --ext EXT, -X EXT
                            image file extension
    --device {cpu,cuda,mps}, -d {cpu,cuda,mps}
                            type of device(s) to use
    --device_id DEVICE_ID, -k DEVICE_ID
                            ID of the first device to use
    --num_devices NUM_DEVICES, -n NUM_DEVICES
                            number of devices to use (with IDs device_id .. device_id+num_devices-1)

    optional advanced arguments:
    --transfer {linear,srgb,pu,log}, -x {linear,srgb,pu,log}
                            transfer function
    --deterministic, --det
                            makes computations deterministic (slower performance)
    """
    features: list[str]
    clean_aux: bool
    filter: str
    preproc_dir: str
    train_data: str
    valid_data: str
    data_dir: str
    ext: str
    device: str
    device_id: int
    num_devices: int
    transfer: str
    deterministic: bool
    def __init__(self, features: list[str] = ..., clean_aux: bool = False, filter: str = '', preproc_dir: str = 'preproc', train_data: str = '', valid_data: str = '', data_dir: str = 'data', ext: str = 'exr', device: str = ..., device_id: int = 0, num_devices: int = 1, transfer: str = '', deterministic: bool = True) -> None: ...

class TrainingOptions:
    """
    Intel(R) Open Image Denoise - Training
    usage: train.py [-h]

    Trains a model using preprocessed datasets.

    positional arguments:
    {hdr,ldr,sh1,albedo,alb,normal,nrm,[]}
                            set of input features

    options:
    -h, --help            show this help message and exit
    --config CONFIG, -c CONFIG
                            load configuration from JSON file (overrides command-line arguments)
    --clean_aux           train with noise-free (reference) auxiliary features
    --filter {RT,RTLightmap}, -f {RT,RTLightmap}
                            filter to train (determines some default arguments)
    --preproc_dir PREPROC_DIR, -P PREPROC_DIR
                            directory of preprocessed datasets
    --train_data TRAIN_DATA, -t TRAIN_DATA
                            name of the training dataset
    --valid_data VALID_DATA, -v VALID_DATA
                            name of the validation dataset
    --results_dir RESULTS_DIR, -R RESULTS_DIR
                            directory of training results
    --result RESULT, -r RESULT
                            name of the training result
    --num_epochs NUM_EPOCHS, --epochs NUM_EPOCHS, -e NUM_EPOCHS
                            number of training epochs
    --num_valid_epochs NUM_VALID_EPOCHS, --valid_epochs NUM_VALID_EPOCHS
                            perform validation every this many epochs
    --num_save_epochs NUM_SAVE_EPOCHS, --save_epochs NUM_SAVE_EPOCHS
                            save checkpoints every this many epochs
    --lr LR, --learning_rate LR
                            initial learning rate
    --max_lr MAX_LR, --max_learning_rate MAX_LR
                            maximum learning rate
    --lr_warmup LR_WARMUP, --learning_rate_warmup LR_WARMUP
                            the percentage of the cycle spent increasing the learning rate (warm-up)
    --batch_size BATCH_SIZE, --bs BATCH_SIZE, -b BATCH_SIZE
                            mini-batch size (total batch size of all devices)
    --num_loaders NUM_LOADERS, --loaders NUM_LOADERS, -j NUM_LOADERS
                            number of data loader threads per device
    --precision {fp32,mixed}, -p {fp32,mixed}
                            training precision
    --device {cpu,cuda,mps}, -d {cpu,cuda,mps}
                            type of device(s) to use
    --device_id DEVICE_ID, -k DEVICE_ID
                            ID of the first device to use
    --num_devices NUM_DEVICES, -n NUM_DEVICES
                            number of devices to use (with IDs device_id .. device_id+num_devices-1)

    optional advanced arguments:
    --transfer {linear,srgb,pu,log}, -x {linear,srgb,pu,log}
                            transfer function
    --model {unet}, -m {unet}
                            network model
    --loss {l1,mape,smape,l2,ssim,msssim,l1_msssim,l1_grad}, -l {l1,mape,smape,l2,ssim,msssim,l1_msssim,l1_grad}
                            loss function
    --msssim_weights [MSSSIM_WEIGHTS ...]
                            MS-SSIM scale weights
    --tile_size TILE_SIZE, --ts TILE_SIZE
                            size of the cropped image tiles
    --seed SEED, -s SEED  seed for random number generation
    --deterministic, --det
                            makes computations deterministic (slower performance)
    """
    verbose_logs: bool
    features: list[str]
    clean_aux: bool
    filter: str
    preproc_dir: str
    train_data: str
    valid_data: str
    results_dir: str
    result: str
    num_epochs: int
    num_valid_epochs: int
    num_save_epochs: int
    lr: float
    max_lr: float
    lr_warmup: float
    batch_size: int
    num_loaders: int
    precision: str
    device: str
    device_id: int
    num_devices: int
    transfer: str
    model: str
    loss: str
    msssim_weights: Sequence[float]
    tile_size: int
    seed: int
    deterministic: bool
    def __init__(self, verbose_logs: bool = False, features: list[str] = ..., clean_aux: bool = False, filter: str = '', preproc_dir: str = 'preproc', train_data: str = '', valid_data: str = '', results_dir: str = 'results', result: str = '', num_epochs: int = 2000, num_valid_epochs: int = 10, num_save_epochs: int = 10, lr: float = 0, max_lr: float = 0, lr_warmup: float = 0.15, batch_size: int = 16, num_loaders: int = 4, precision: str = '', device: str = ..., device_id: int = 0, num_devices: int = 1, transfer: str = '', model: str = 'unet', loss: str = 'l1_msssim', msssim_weights: Sequence[float] = [0.2, 0.2, 0.2, 0.2, 0.2], tile_size: int = 256, seed: int = 0, deterministic: bool = False) -> None: ...

class ExportOptions:
    """
    Intel(R) Open Image Denoise - Training
    usage: export.py [-h]

    Exports a training result to the runtime model weights format (TZA).

    positional arguments:
      {weights,package}     what to export

    options:
      -h, --help            show this help message and exit
      --config CONFIG, -c CONFIG
                            load configuration from JSON file (overrides command-line arguments)
      --results_dir RESULTS_DIR, -R RESULTS_DIR
                            directory of training results
      --result RESULT, -r RESULT
                            name of the training result
      --num_epochs NUM_EPOCHS, --epochs NUM_EPOCHS, -e NUM_EPOCHS
                            number of training epochs
      --output OUTPUT, -o OUTPUT
                            output file
      --device {cpu,cuda,mps}, -d {cpu,cuda,mps}
                            type of device(s) to use
      --device_id DEVICE_ID, -k DEVICE_ID
                            ID of the first device to use
      --num_devices NUM_DEVICES, -n NUM_DEVICES
                            number of devices to use (with IDs device_id .. device_id+num_devices-1)

    optional advanced arguments:
      --deterministic, --det
                            makes computations deterministic (slower performance)
    """
    features: list[str]
    target: str
    results_dir: str
    result: str
    num_epochs: int
    export_dir: str
    output: str
    device: str
    device_id: int
    num_devices: int
    deterministic: bool
    def __init__(self, features: list[str] = ..., target: str = 'weights', results_dir: str = 'results', result: str = '', num_epochs: int = -1, export_dir: str = '', output: str = '', device: str = ..., device_id: int = 0, num_devices: int = 1, deterministic: bool = True) -> None: ...
