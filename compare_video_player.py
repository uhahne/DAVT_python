import sys
import cv2
import numpy as np
from pathlib import Path
import ffmpeg


# Paths to the video files
video_path_1 = 'data/starcraft/StarCraft.yuv'
video_path_2 = 'data/starcraft/output.mp4'

# Function to compute the mean squared difference between two frames
def mean_squared_difference_per_pixel(frame1, frame2):
    return np.mean((frame1 - frame2) ** 2)/frame1.size

# Function to compute the difference between two frames
def compute_frame_difference(frame1, frame2):
    # Convert frames to grayscale
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    # Compute the absolute difference between the two frames
    difference = cv2.absdiff(gray1, gray2)
    
    # Apply a threshold to get a binary image
    _, difference = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
    
    # Convert the binary image to BGR format
    difference = cv2.cvtColor(difference, cv2.COLOR_GRAY2BGR)
    
    return difference

# Compare the used codecs of the video files using ffprobe

def get_codec(video_path):
    try:
        probe = ffmpeg.probe(video_path)
    except ffmpeg.Error as e:
        print(e.stderr, file=sys.stderr)
        sys.exit(1)

    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print('No video stream found', file=sys.stderr)
        sys.exit(1)

    print(f"Codec: {video_stream['codec_name']}")

def getFileInformation(video_path):
    # Print file sizes of the video files in MB
    file_size = Path(video_path).stat().st_size / (1024 * 1024)
    print(f"File size: {file_size:.2f} MB")
    return file_size

# Open the video files
cap1 = cv2.VideoCapture(video_path_1)
cap2 = cv2.VideoCapture(video_path_2)

print("Comparing video files:")
print(f"Video 1: {video_path_1}")
get_codec(video_path_1)
file_size_1 = getFileInformation(video_path_1)
data_rate_1 = cap1.get(cv2.CAP_PROP_BITRATE) / 1000
print(f"Data rate of video 1: {data_rate_1:.2f} kbps")
print('-------\n')

print(f"Video 2: {video_path_2}")
get_codec(video_path_2)
file_size_2 = getFileInformation(video_path_2)
data_rate_2 = cap2.get(cv2.CAP_PROP_BITRATE) / 1000
print(f"Data rate of video 2: {data_rate_2:.2f} kbps")
print('-------\n')

print(f"Ratio of file size 1 to file size 2: {file_size_1 / file_size_2:.2f}")
print(f"Ratio of data rate 1 to data rate 2: {data_rate_1 / data_rate_2:.2f}")
print('-------\n')

frame_count = 0
total_msd = 0

while cap1.isOpened() and cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        break
    
    # Resize frames to the same height
    height = min(frame1.shape[0], frame2.shape[0])
    frame1 = cv2.resize(frame1, (int(frame1.shape[1] * height / frame1.shape[0]), height))
    frame2 = cv2.resize(frame2, (int(frame2.shape[1] * height / frame2.shape[0]), height))
    frame_diff = compute_frame_difference(frame1, frame2)

    # Compare the frames
    msd = mean_squared_difference_per_pixel(frame1, frame2)
    total_msd += msd
    frame_count += 1

    # Concatenate frames horizontally
    combined_frame = np.hstack((frame1, frame2, frame_diff))

    # Display the combined frame
    cv2.imshow('Video Player', combined_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video captures and close windows
cap1.release()
cap2.release()
cv2.destroyAllWindows()

if frame_count > 0:
    average_msd = total_msd / frame_count
    print(f"Average Mean Squared Difference per pixel: {average_msd:.7f}")
else:
    print("No frames to compare.")