import tensorflow as tf
import PIL
batch_size = 8

image_size=64
train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1.0/255.0,
)
test_datagen=tf.keras.preprocessing.image.ImageDataGenerator(rescale=1.0/255.0)

train_generator=train_datagen.flow_from_directory(
    'data/train',
    target_size=(image_size,image_size),
    batch_size=batch_size,
    class_mode='categorical',
)

validation_generator=test_datagen.flow_from_directory(
    'data/test',
    target_size=(image_size,image_size),
    batch_size=batch_size,
    class_mode='categorical'
)
kwargs = dict()
model = tf.keras.models.Sequential([

    tf.keras.layers.Conv2D(64, 3,use_bias=False, activation='relu', input_shape=(image_size, image_size, 3)),
	tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
	
	tf.keras.layers.Conv2D(64, 3, padding="same", **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.ReLU(),


	tf.keras.layers.Conv2D(128, 3, padding="same", **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.ReLU(),

	tf.keras.layers.Conv2D(128, 3, padding="same", **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    tf.keras.layers.ReLU(),

	tf.keras.layers.Flatten(),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(64, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(64, **kwargs),
    tf.keras.layers.BatchNormalization(momentum=0.99, scale=False),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.ReLU(),
    tf.keras.layers.Dense(12, **kwargs),
    tf.keras.layers.Activation("softmax")

])
model.summary()
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(learning_rate=0.01, decay=0.0001),metrics=['accuracy'])

STEP_SIZE_TRAIN=train_generator.n//train_generator.batch_size
STEP_SIZE_VALID=validation_generator.n//validation_generator.batch_size

model.fit(train_generator,steps_per_epoch=STEP_SIZE_TRAIN,epochs=10,validation_data=validation_generator, validation_steps=STEP_SIZE_VALID)
model.save_weights("model")




