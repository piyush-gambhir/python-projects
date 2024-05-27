import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def convert_mp4_to_mp3(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Check if the file is an MP4 file
        if file.endswith(".mp4"):
            input_path = os.path.join(input_folder, file)

            # Generate output file path with the same name but with .mp3 extension
            output_file = os.path.splitext(file)[0] + ".mp3"
            output_path = os.path.join(output_folder, output_file)

            # Convert MP4 to MP3 using moviepy
            video_clip = VideoFileClip(input_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_path, codec='mp3')

            # Close the clips
            audio_clip.close()
            video_clip.close()


if __name__ == "__main__":
    input_folder = "./mp4/"
    output_folder = "./mp3/"

    convert_mp4_to_mp3(input_folder, output_folder)
