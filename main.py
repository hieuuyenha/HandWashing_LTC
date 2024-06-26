from numpy.core.defchararray import array
from layer1_model import *
from layer2_model import *
from data_preprocess import *
import argparse
import sys

def train_model(model, database):
    model.fit(database)

def test_model(model, database):
    model.predict(database)

def eval_layer2(layer1_model, layer2_model, vid_path):
    frame_list = extract_single_vid(vid_path)
    _, raw_data = layer1_model._process_video(np.array(frame_list))

    feature_vector = [step[0] for step in raw_data] + [step[1] for step in raw_data]
    data = np.array(feature_vector).reshape(1, -1)
    predict_result, predict_precent = layer2_model.evaluate(data)

    if (predict_result[0] == 1):
        print("Predict label: No")
    elif (predict_result[0] == 0):
        print("Predict label: Yes")
    print(f"Probability:\tYes: {predict_precent[0][0]}, No: {predict_precent[0][1]}")
    return (predict_result, predict_precent)

def clean_data(is_regenerate_layer1, is_regenerate_layer2):
    if is_regenerate_layer1:
        clear_data(LAYER_1_TRAIN_PATH)
        clear_data(LAYER_1_VALID_PATH)
        clear_data(LAYER_1_TEST_PATH)

    if is_regenerate_layer2:
        clear_data(LAYER_2_TRAIN_PATH)
        clear_data(LAYER_2_VALID_PATH)
        clear_data(LAYER_2_TEST_PATH)
        clear_data(LAYER_2_TRAIN_PROCESSED_PATH)
        clear_data(LAYER_2_VALID_PROCESSED_PATH)
        clear_data(LAYER_2_TEST_PROCESSED_PATH)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l','--layer', help="Choose which layer to run on: preprocess/layer1/layer2", default="layer1", required=False) #Hieu
    parser.add_argument('--train', help="Set train mode", default="true")
    parser.add_argument('--test', help="Set test mode", default="true")
    parser.add_argument('--eval', help="Set eval mode",default="false")
    parser.add_argument('--divideLayer1', help="Flag to trigger shuffle layer 1 data again", default="false") #Hieu
    parser.add_argument('--divideLayer2', help="Flag to trigger shuffle layer 2 data again", default="false") #Hieu
    parser.add_argument('-p', '--path',  help="Set video path for evaluation")

    args = parser.parse_args()
    if args.path != None:
        layer1_model = setup_layer1_model(MODEL_EPOCH_NUM)
        layer2_model = setup_layer2_model(LAYER2_EPOCH_NUM)

        eval_layer2(layer1_model, layer2_model, args.path)

    elif args.layer == "preprocess":
        clean_data(REGENERATE_LAYER1_DATA, REGENERATE_LAYER2_DATA)

        if args.divideLayer1 == "true":
            divide_layer1_data = True
        else:
            divide_layer1_data = False
        
        if args.divideLayer2 == "true":
            divide_layer2_data = True
        else:
            divide_layer2_data = False
            
        data_preprocess(divide_layer1_data, divide_layer2_data, REGENERATE_LAYER1_DATA, REGENERATE_LAYER2_DATA)
    elif args.layer == "layer1":
        layer1_database = setup_layer1_database()
        layer1_model = setup_layer1_model(MODEL_EPOCH_NUM)

        if args.train == "true":
            train_model(layer1_model, layer1_database)
        if args.test == "true":
            test_model(layer1_model, layer1_database)

    elif args.layer == "layer2":
        processing_layer2_feature_data()
        layer2_database = setup_layer2_database()
        layer2_model = setup_layer2_model(LAYER2_EPOCH_NUM)

        if args.train == "true":
            train_model(layer2_model, layer2_database)
        if args.test == "true":
            test_model(layer2_model, layer2_database)
    else:
        print("Wrong usage.")
        parser.print_help()
