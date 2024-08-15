import os
from PIL import Image
import json

# Directory where the images are stored
image_directory = 'assets/images/banner/'

# Resolution that the images must match
required_resolution = (1920, 1080)  # Example resolution

# File to store the valid image paths
output_json = 'assets/images/banner_images.json'

def validate_image_resolution(image_path, required_resolution):
    """Check if the image matches the required resolution."""
    with Image.open(image_path) as img:
        return img.size == required_resolution

def scan_images(directory, required_resolution):
    """Scan the directory for images and validate their resolution."""
    valid_images = []
    
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_path = os.path.join(directory, filename)
            if validate_image_resolution(image_path, required_resolution):
                valid_images.append(image_path)
    
    return valid_images

def write_json_file(image_paths, output_json):
    """Write the valid image paths to a JSON file."""
    with open(output_json, 'w') as json_file:
        json.dump(image_paths, json_file, indent=4)

def main():
    valid_images = scan_images(image_directory, required_resolution)
    write_json_file(valid_images, output_json)
    print(f"Valid images written to {output_json}")

if __name__ == "__main__":
    main()
