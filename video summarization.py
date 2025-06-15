
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Function to extract summarized video
def summarize_video(input_video, output_video, duration=10):
    # Load the video file
    video = VideoFileClip(input_video)
    
    # Divide the video into equal parts
    total_duration = video.duration  # Get the total length of the video
    segment_duration = total_duration / 5  # Extract 5 key segments
    
    clips = []
    for i in range(5):
        start_time = i * segment_duration
        end_time = start_time + (duration / 5)  # Adjusting for final duration
        clips.append(video.subclip(start_time, min(end_time, total_duration)))

    # Concatenate selected clips
    summarized_clip = concatenate_videoclips(clips)
    
    # Save the summarized video
    summarized_clip.write_videofile(output_video, codec="libx264", fps=24)
    print(f"Summarized video saved as {output_video}")

# Provide the input video file
input_video = "video.mp4"  # Change this to your video file
output_video = "summary.mp4"

# Run summarization
summarize_video(input_video, output_video)
