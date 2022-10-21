import tensorflow as tf
import numpy as np
from numpy.random import seed
seed(1)
from tensorflow.random import set_seed
set_seed(2)
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import time
import glob
import random
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import os
import cv2
import shutil

# Dataset can be found here:
# https://www.kaggle.com/datasets/sid4sal/alpaca-dataset-small

# Training code adapted from: ARI on Kaggle

base_path = 'dataset'
classes = os.listdir(base_path)
filepaths = []
labels = []
for c in classes:
    flist = os.listdir(base_path + '/' + c)
    for f in flist:
        fpath = os.path.join(base_path, c, f)
        filepaths.append(fpath)
        labels.append(c)

Fseries=pd.Series(filepaths, name='file_paths').astype(str)
Lseries=pd.Series(labels, name='labels')
df=pd.concat([Fseries,Lseries], axis=1)

train_df, test_df = train_test_split(df, train_size=0.96, random_state=1)
train_df, valid_df = train_test_split(train_df, train_size=0.96, random_state=1)

target_size=(300,300)
batch_size=32

train_datagen = ImageDataGenerator(preprocessing_function=tf.keras.applications.efficientnet.preprocess_input, zoom_range=0.2, width_shift_range=0.1, height_shift_range=0.1)
test_datagen = ImageDataGenerator(preprocessing_function=tf.keras.applications.efficientnet.preprocess_input)
train_gen = train_datagen.flow_from_dataframe(train_df, x_col='file_paths', y_col='labels', target_size=target_size, batch_size=batch_size, color_mode='rgb', class_mode='binary')
valid_gen = test_datagen.flow_from_dataframe(valid_df, x_col='file_paths', y_col='labels', target_size=target_size, batch_size=batch_size, color_mode='rgb', class_mode='binary')
test_gen = test_datagen.flow_from_dataframe(test_df, x_col='file_paths', y_col='labels', target_size=target_size, batch_size=batch_size, color_mode='rgb', class_mode='binary')

base_model = tf.keras.applications.EfficientNetB3(include_top=False, input_shape=(300,300,3))
model = tf.keras.Sequential([
    base_model, 
    tf.keras.layers.GlobalAveragePooling2D(), 
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.BatchNormalization(), 
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer=Adam(0.001), metrics=['accuracy'])

patience = 2
stop_patience = 5
factor = 0.5

callbacks = [
    tf.keras.callbacks.ModelCheckpoint("classify_model.h5", save_weights_only=True, save_best_only=True, verbose = 0),
    tf.keras.callbacks.EarlyStopping(patience=stop_patience, monitor='val_loss', verbose=1, restore_best_weights=True),
    tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=factor, patience=patience, verbose=1)
]

epochs = 30
history = model.fit(train_gen, validation_data=valid_gen, epochs=epochs, callbacks=callbacks, verbose=1)

best_model = model
best_model.load_weights('./classify_model.h5')
best_model.evaluate(test_gen)
