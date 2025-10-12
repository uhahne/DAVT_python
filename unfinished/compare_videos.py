import cv2
import numpy as np

def mean_squared_difference(frame1, frame2):
    return np.mean((frame1 - frame2) ** 2)

def compare_videos(video_path1, video_path2):
    cap1 = cv2.VideoCapture(video_path1)
    cap2 = cv2.VideoCapture(video_path2)

    if not cap1.isOpened() or not cap2.isOpened():
        print("Error: Could not open one of the video files.")
        return

    frame_count = 0
    total_msd = 0

    while True:
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        if not ret1 or not ret2:
            break

        if frame1.shape != frame2.shape:
            print("Error: Frames have different shapes.")
            break

        msd = mean_squared_difference(frame1, frame2)
        total_msd += msd
        frame_count += 1

    cap1.release()
    cap2.release()

    if frame_count > 0:
        average_msd = total_msd / frame_count
        print(f"Average Mean Squared Difference: {average_msd}")
    else:
        print("No frames to compare.")

if __name__ == "__main__":
    video_path1 = '../../DAVT/itur525_29tabletennis_original.avi'
    video_path2 = '../../DAVT/output.mp4'
    compare_videos(video_path1, video_path2)