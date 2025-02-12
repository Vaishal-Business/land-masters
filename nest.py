import cv2
import os

# Settings
image_folder = r"C:\Users\vaish\Downloads\Copy of Development\moon zoom\tour of moon\footage"  # Replace with the folder containing the images
output_video = 'tour_of_moon.mp4'
fps = 30  # Frames per second

# Collect sorted image file names
image_files = [f for f in os.listdir(image_folder) if f.startswith('tour of moon_') and f.endswith('.jpeg')]
image_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))  # Sort based on numbers

# Read the first image to get dimensions
first_image_path = os.path.join(image_folder, image_files[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# Initialize the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
video = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

# Write each image to the video
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the video writer
video.release()

print(f"Video saved as {output_video}")
