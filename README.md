
Dataset source: https://www.kaggle.com/realtimear/hand-wash-dataset

LTC reference: https://github.com/raminmh/liquid_time_constant_networks/tree/master

# How to run

### Train model

- Go to src folder then:
    1. Preprocessing the data 
        
        > `python main.py -l preprocess`

        This will create a list of data of both layer1 and layer2 for train/valid/test dataset, the list is written in file `.lst`.
    2. Train the inner layer (i.e layer1).

        > `python main.py -l layer1`

        This method will use for start training and testing the layer 1 model.

       

    3. Train the outer layer (i.e layer2). 

        This method will use for start training and testing the layer 1 model.

        > `python main.py -l layer2`


### Evaluate whole project with video 
Turning on the --eval flag and feed video path to --path

> `python main.py --eval true --path <video_path>`

