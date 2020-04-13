# SketchGAN

## Data
The Quick, Draw! dataset is publicly available and [here](https://github.com/googlecreativelab/quickdraw-dataset#get-the-data) you can find the instructions on how to download the data locally. The `load_data` module is available in order to handle the `.ndjson` drawing files. The file containing sketches of circles (`circle.ndjson`) is already in the root folder of this project in order to provide a boilerplate setup.

## Model

GANs implementation in Keras, available [here](https://github.com/eriklindernoren/Keras-GAN/blob/master/gan/gan.py). 

Here you can see a summary of the architecture:

```
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten_1 (Flatten)          (None, 784)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               401920    
_________________________________________________________________
leaky_re_lu_1 (LeakyReLU)    (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 256)               131328    
_________________________________________________________________
leaky_re_lu_2 (LeakyReLU)    (None, 256)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 257       
=================================================================
Total params: 533,505
Trainable params: 533,505
Non-trainable params: 0
_________________________________________________________________
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_4 (Dense)              (None, 256)               25856     
_________________________________________________________________
leaky_re_lu_3 (LeakyReLU)    (None, 256)               0         
_________________________________________________________________
batch_normalization_1 (Batch (None, 256)               1024      
_________________________________________________________________
dense_5 (Dense)              (None, 512)               131584    
_________________________________________________________________
leaky_re_lu_4 (LeakyReLU)    (None, 512)               0         
_________________________________________________________________
batch_normalization_2 (Batch (None, 512)               2048      
_________________________________________________________________
dense_6 (Dense)              (None, 1024)              525312    
_________________________________________________________________
leaky_re_lu_5 (LeakyReLU)    (None, 1024)              0         
_________________________________________________________________
batch_normalization_3 (Batch (None, 1024)              4096      
_________________________________________________________________
dense_7 (Dense)              (None, 784)               803600    
_________________________________________________________________
reshape_1 (Reshape)          (None, 28, 28, 1)         0         
=================================================================
Total params: 1,493,520
Trainable params: 1,489,936
Non-trainable params: 3,584
```

## Usage

```
python gan.py
```

## Results

### Circle
![circle](docs/circle.gif)

### Airplane
![airplane](docs/airplane.gif)

### Cat
![cat](docs/cat.gif)