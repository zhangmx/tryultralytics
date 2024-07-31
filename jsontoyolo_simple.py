import os
import json
import random
import shutil

# Define the class labels 
class_labels = {"OK": 0, "NGReverse": 1, "component": 2} # Change/add more for your database

# Define the directories
input_dir = './pictures/train' # Replace with your directory
output_dir = './datasets/ccd1' # Replace with your directory

os.makedirs(output_dir, exist_ok=True)

# Define the split ratio
split_ratio = 0.9

# Create the output directories
os.makedirs(os.path.join(output_dir, 'images/train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'images/val'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'labels/train'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'labels/val'), exist_ok=True)

# Collect all json filenames
json_files = [f for f in os.listdir(input_dir) if f.endswith('.json')]

# Shuffle and split the files
random.shuffle(json_files)
split_index = int(len(json_files) * split_ratio)
train_files = json_files[:split_index]
val_files = json_files[split_index:]

def process_files(files, split):
    for filename in files:
        with open(os.path.join(input_dir, filename)) as f:
            data = json.load(f)

        # Create corresponding image and label paths
        image_filename = data['imagePath']  # Assuming the images are .jpg
        label_filename = filename.replace('.json', '.txt')

        image_output_path = os.path.join(output_dir, 'images', split, image_filename)
        label_output_path = os.path.join(output_dir, 'labels', split, label_filename)

        # Copy the image to the output directory
        shutil.copy(os.path.join(input_dir, image_filename), image_output_path)

        with open(label_output_path, 'w') as out_file:
            for shape in data['shapes']:
                if shape['shape_type'] == 'circle':
                    # For circles, points contain the center and a point on the circumference
                    x_center, y_center = shape['points'][0]
                    x_circum, y_circum = shape['points'][1]

                    radius = ((x_center - x_circum) ** 2 + (y_center - y_circum) ** 2) ** 0.5
                    x1 = x_center - radius
                    y1 = y_center - radius
                    x2 = x_center + radius
                    y2 = y_center + radius
                else:
                    # For other shapes, we'll assume it's a rectangle for simplicity
                    x1, y1 = shape['points'][0]
                    x2, y2 = shape['points'][1]

                dw = 1. / data['imageWidth']
                dh = 1. / data['imageHeight']
                w = x2 - x1
                h = y2 - y1
                x = x1 + (w / 2)
                y = y1 + (h / 2)

                x *= dw
                w *= dw
                y *= dh
                h *= dh

                class_label = class_labels[shape['label']]

                out_file.write(f"{class_label} {x} {y} {w} {h}\n")

process_files(train_files, 'train')
process_files(val_files, 'val')

print("Conversion and splitting completed successfully!")
