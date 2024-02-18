import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dropout, Conv2DTranspose, concatenate
from tensorflow.keras.models import Model


def unet(input_size=(256, 256, 1)):
    inputs = Input(input_size)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(inputs)
    conv1 = Conv2D(64, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    # Add more layers to construct the full U-Net architecture...
    # Final layer
    conv9 = Conv2D(1, 1, activation='sigmoid')(conv1)
    model = Model(inputs=[inputs], outputs=[conv9])
    return model


# Define your data generators
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1. / 255)

train_image_generator = train_datagen.flow_from_directory(
    '../../data/split/train/images',  # Update this path
    target_size=(256, 256),
    color_mode='grayscale',
    class_mode=None,
    batch_size=32,
    seed=42)

train_mask_generator = train_datagen.flow_from_directory(
    '../../data//split/train/masks',  # Update this path
    target_size=(256, 256),
    color_mode='grayscale',
    class_mode=None,
    batch_size=32,
    seed=42)

# Combine generators into one which yields image and masks
train_generator = zip(train_image_generator, train_mask_generator)

# Initialize U-Net model
model = unet()

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train model
model.fit(
    train_generator,
    steps_per_epoch=200,
    epochs=5)  # Adjust the number of steps per epoch and epochs as needed
