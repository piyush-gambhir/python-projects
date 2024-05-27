from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip


def download_highest_quality(url):
    yt = YouTube(url)

    # Get the highest quality video and audio streams
    video_stream = yt.streams.filter(
        adaptive=True, file_extension='mp4').order_by('resolution').desc().first()
    audio_stream = yt.streams.filter(
        only_audio=True, file_extension='mp3').order_by('abr').desc().first()

    # Download video and audio
    print(
        f"Downloading video: {video_stream.resolution} - {video_stream.mime_type} - {video_stream.fps}fps...")
    video_path = video_stream.download(filename='video.mp4')
    print(
        f"Downloading audio: {audio_stream.abr} - {audio_stream.mime_type}...")
    audio_path = audio_stream.download(filename='audio.mp3')

    return video_path, audio_path


def merge_video_audio(video_path, audio_path, output_path='output.mp4'):
    print("Merging video and audio...")
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
    print(f"Merged video saved as {output_path}")


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    video_path, audio_path = download_highest_quality(video_url)
    merge_video_audio(video_path, audio_path)
