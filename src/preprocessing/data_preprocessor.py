import os
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def get_full_path(relative_path):
    """
    Constructs a full path to the data directory, relative to the script location.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Absolute directory of the script
    return os.path.join(script_dir, relative_path)


def load_images_from_folder(folder):
    """
    Load all images from a specified folder and return them as a numpy array.
    Also returns the filenames to keep track of them.
    """
    images = []
    filenames = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
            filenames.append(filename)
    return np.array(images), filenames


def preprocess_images(images):

    # Normalize images to the range [0, 1]
    images_normalized = images.astype('float32') / 255.0
    return images_normalized


def save_images_to_folder(images, filenames, folder):
    """
    Saves images to the specified folder, using the given filenames.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    for img, filename in zip(images, filenames):
        save_path = os.path.join(folder, filename)
        # Convert image back to uint8 format before saving, if it was normalized
        img_uint8 = (img * 255).astype('uint8')
        cv2.imwrite(save_path, img_uint8)


if __name__ == "__main__":
    # Paths relative to the script location
    images_dir = get_full_path('../../data/images')
    masks_dir = get_full_path('../../data/masks')
    preprocessed_images_dir = get_full_path('../../data/preprocessed/images')
    preprocessed_masks_dir = get_full_path('../../data/preprocessed/masks')

    # Load images and masks
    images, image_filenames = load_images_from_folder(images_dir)
    masks, mask_filenames = load_images_from_folder(masks_dir)

    # Preprocess images and masks (e.g., normalization, resizing)
    images_preprocessed = preprocess_images(images)
    masks_preprocessed = preprocess_images(masks)  # Assuming similar preprocessing for masks, if needed

    # Save preprocessed images and masks
    save_images_to_folder(images_preprocessed, image_filenames, preprocessed_images_dir)
    save_images_to_folder(masks_preprocessed, mask_filenames, preprocessed_masks_dir)

    print(f"Saved {len(images_preprocessed)} preprocessed images to {preprocessed_images_dir}.")
    print(f"Saved {len(masks_preprocessed)} preprocessed masks to {preprocessed_masks_dir}.")
