import os
import shutil

def copy_files(file_list, src_dir, dest_dir, src_extension):
    """
    Copies files from the source directory to the destination directory based on a list of filenames.
    Adjusts the source file extension for each file based on the provided src_extension.
    """
    for file_name in file_list:
        # Correctly format filename by ensuring only one extension is added
        base_name = file_name.split('.')[0]  # Assuming file_name might contain an extension
        actual_file_name = f"{base_name}{src_extension}"
        src_path = os.path.join(src_dir, actual_file_name)
        dest_path = os.path.join(dest_dir, actual_file_name)
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
        else:
            print(f"File {src_path} not found.")

def read_file_list(file_path):
    """
    Reads a text file and returns a list of lines (filenames), excluding the file extension.
    """
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    # Assume filenames in the txt file might include an extension, so we ignore it
    return [line.split('.')[0] for line in lines]  # Extract the base name if extensions are present

if __name__ == "__main__":
    base_dir = '../../data/'  # Update this to the absolute path of your 'data' directory
    metadata_dir = os.path.join(base_dir, 'metadata')

    # Source directories for preprocessed images and masks
    images_src_dir = os.path.join(base_dir, 'preprocessed/images')
    masks_src_dir = os.path.join(base_dir, 'preprocessed/masks')

    # Destination directories for the dataset splits
    train_images_dest_dir = os.path.join(base_dir, 'split/train/images')
    train_masks_dest_dir = os.path.join(base_dir, 'split/train/masks')
    val_images_dest_dir = os.path.join(base_dir, 'split/val/images')
    val_masks_dest_dir = os.path.join(base_dir, 'split/val/masks')
    test_images_dest_dir = os.path.join(base_dir, 'split/test/images')
    test_masks_dest_dir = os.path.join(base_dir, 'split/test/masks')

    # Create destination directories if they do not exist
    for path in [train_images_dest_dir, train_masks_dest_dir, val_images_dest_dir, val_masks_dest_dir, test_images_dest_dir, test_masks_dest_dir]:
        os.makedirs(path, exist_ok=True)

    # Read file lists from the .txt files
    train_files = read_file_list(os.path.join(metadata_dir, 'training.txt'))
    val_files = read_file_list(os.path.join(metadata_dir, 'validation.txt'))
    test_files = read_file_list(os.path.join(metadata_dir, 'test.txt'))

    # Copy image files according to the lists, handling the correct file extension
    copy_files(train_files, images_src_dir, train_images_dest_dir, src_extension='.tif')
    copy_files(val_files, images_src_dir, val_images_dest_dir, src_extension='.tif')
    copy_files(test_files, images_src_dir, test_images_dest_dir, src_extension='.tif')

    # Copy mask files according to the lists, handling the correct file extension
    copy_files(train_files, masks_src_dir, train_masks_dest_dir, src_extension='.png')
    copy_files(val_files, masks_src_dir, val_masks_dest_dir, src_extension='.png')
    copy_files(test_files, masks_src_dir, test_masks_dest_dir, src_extension='.png')

    print("Files successfully copied to train, validation, and test split folders.")
