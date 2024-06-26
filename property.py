import os

### PROPERTY ###
######
LAYER_1_RAWDATA_PATH = os.path.join("data", "layer_1_data", "raw_video")
LAYER_2_RAWDATA_PATH = os.path.join("data", "layer_2_data", "raw_video")

LAYER_1_TRAIN_PATH = os.path.join("data", "layer_1_data", "feature_data","train")
LAYER_1_VALID_PATH = os.path.join("data", "layer_1_data", "feature_data","valid")
LAYER_1_TEST_PATH = os.path.join("data", "layer_1_data", "feature_data","test")

LAYER_2_TRAIN_PATH = os.path.join("data", "layer_2_data", "feature_data","train")
LAYER_2_VALID_PATH = os.path.join("data", "layer_2_data", "feature_data","valid")
LAYER_2_TEST_PATH = os.path.join("data", "layer_2_data", "feature_data","test")

LAYER_2_TRAIN_PROCESSED_PATH = os.path.join("data", "layer_2_data", "processed_data","train")
LAYER_2_VALID_PROCESSED_PATH = os.path.join("data", "layer_2_data", "processed_data","valid")
LAYER_2_TEST_PROCESSED_PATH = os.path.join("data", "layer_2_data", "processed_data","test")


VIDEO_EXTENSION = ('.mp4', '.avi')
DATA_EXTENSION = ('.npy')

REGENERATE_LAYER1_DATA = False                                      # Re-compute dataset flag
REGENERATE_LAYER2_DATA = False                                      # Re-compute dataset flag

LAYER_1_TRAIN_FILE=os.path.join("data","layer_1_data","train.lst")
LAYER_1_VALID_FILE=os.path.join("data","layer_1_data","val.lst")
LAYER_1_TEST_FILE=os.path.join("data","layer_1_data","test.lst")
LAYER_2_TRAIN_FILE=os.path.join("data","layer_2_data","train.lst")
LAYER_2_VALID_FILE=os.path.join("data","layer_2_data","val.lst")
LAYER_2_TEST_FILE=os.path.join("data","layer_2_data","test.lst")

######

### Preprocessing hyperparameter ###
######
PROCESS_VIDEO_LENGTH = 30                                           # frames per sub video to train
FRAME_STEP = 3                                                      # only take 1 every 3 frames
WINDOWS_LENGTH = int(PROCESS_VIDEO_LENGTH / FRAME_STEP)             # length of sliding windows when reading full video
######

### Layer 1 Model hyperparameter ###
######
VALID_RATIO = 0.1                                                   # Valid percentage when dividing dataset
TEST_RATIO = 0.1                                                    # Test percentage when dividing dataset
BATCH_SIZE = 64                                                     # Batch size fitting in network
NUMBER_OF_TREE = 3                                                 # Number of tree in random forest (default: 3)

## Set DIFFERENT_TREE_LIST if tree in forest is different type of network or MODEL_TYPE if all tree have same type ##
DIFFERENT_TREE_LIST = None                                          # Example for using 2 kind of network: ["ltc", "lstm"] 
MODEL_TYPE = "ltc"                                                  # type of Cell for network (lstm / ltc / ltc_ex / ltc_rk / node / ctgru / ctrnn)

MODEL_SIZE = 10 
NAME_FOREST = "ltc"                                                   # time step
MODEL_EPOCH_NUM = 100                                               # iterative
MODEL_LOG_PERIOD = 1                                                # number of iterative for each save
MODEL_SPARSITY = 0.0
######

### Layer 2 Model parameter ###
######
LAYER_2_MODEL_TYPE = "mlp"                                          # Type of layer 2 model
LAYER_2_VALID_RATIO = 0.2                                           # Valid percentage when dividing dataset
LAYER_2_TEST_RATIO = 0.1                                            # Test percentage when dividing dataset

LAYER2_EPOCH_NUM = 200                                              # Number of epoch when training layer2 
LAYER2_ACTIVATION = 'relu'                                          # Activation function type for MLP ((identity, logistic, tanh, relu)
LAYER2_SOLVER = 'adam'                                              # Optimizer type for MLP (lbfgs, sgd, adam)
######


### Validate properties ###
if (DIFFERENT_TREE_LIST is None):
    SAVE_LOCATION_NAME = f"{MODEL_TYPE}_{NAME_FOREST}"
    TREE_TYPE_LIST = [MODEL_TYPE] * NUMBER_OF_TREE
else:
    if (len(DIFFERENT_TREE_LIST) != NUMBER_OF_TREE):
        raise Exception('The list of tree name not match the number of tree')

    SAVE_LOCATION_NAME = f"hybrid"
    for tree in ([ (i,DIFFERENT_TREE_LIST.count(i)) for i in dict.fromkeys(DIFFERENT_TREE_LIST) ]):
        SAVE_LOCATION_NAME += f"_{tree[1]}{tree[0]}"
        TREE_TYPE_LIST = DIFFERENT_TREE_LIST