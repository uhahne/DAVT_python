import sys
import ffmpeg

def compress_video(input_file, output_file, vcodec='h264'):
    """
    Compress a video file using ffmpeg with specified parameters.

    :param input_file: Path to the input video file
    :param output_file: Path to the output compressed video file
    :param codec: Codec to use for compression (default is h264)
    :param crf: Constant Rate Factor (lower value means better quality, but larger file size)
    :param preset: Preset for compression speed (slower presets give better compression)
    """
    try:
        output_file_with_params = f"{output_file.rsplit('.', 1)[0]}__vcodec{vcodec}.{output_file.rsplit('.', 1)[1]}"
        (
            ffmpeg
            .input(input_file)
            .output(output_file_with_params, vcodec=vcodec )
            .run(overwrite_output=True)
        )
        print(f"Video compressed successfully: {output_file_with_params}")

    except ffmpeg.Error as e:
        print(f"Error occurred: {e.stderr.decode()}")

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
    return video_stream['codec_name']
    
if __name__ == "__main__":
    input_video = 'data/tbd'  # Replace with your input video file path
    output_video = 'data/output.mp4'  # Replace with your desired output video file path
    if (get_codec(input_video) != None):
        compress_video(input_video, output_video)