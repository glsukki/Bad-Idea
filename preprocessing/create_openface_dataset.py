### This script creates datasets for the OpenFace library - to extract facial features - of participants reacting to the stimulusVideos of Robots and Humans in Task failure Performance
### Given a list of participants, iterate through each participant's response videos,
### and clip the video from (start_time, end_time)
### Where, start_time = clip.duration - video_clipping_duration
### video_clipping_duration - time from the end of the video.
### This is done so as to capture the participant's reactions during the moment of success or failure of the given stimulus

import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

files_to_ignore = [".DS_Store"]


def clipVideoEnd(study_video_path, participants, videos_to_clip, video_clipping_duration, output_path):

    output_path = output_path + f"cut_dataset_{video_clipping_duration}s/"
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for participant in participants:
        participant_data_path = study_video_path + participant + "/mp4StudyVideo/"
        for input_video in os.listdir(participant_data_path):
            input_video_path = participant_data_path + input_video
            if input_video not in files_to_ignore and videos_to_clip in input_video:
                clip = VideoFileClip(input_video_path)

                start_time = clip.duration - video_clipping_duration
                end_time = clip.duration
                # print(f"Video Duration = {end_time}, start = {start_time}, end = {end_time}")
                clipped_clip = clip.subclip(start_time, end_time)

                output_video_path = output_path + participant
                if not os.path.exists(output_video_path):
                    os.mkdir(output_video_path)
                output_video_path = output_video_path + "/" + input_video

                ffmpeg_extract_subclip(input_video_path, start_time, end_time, targetname=output_video_path)

                ## Does not preserve the audio
                # clipped_clip.write_videofile(output_video_path)
                
                clipped_clip.close()
                clip.close()
        # break # from participants

def main():
    study_video_path = "../../studyData/study_videos/"
    output_path = "../../studyData/"
    # participants = [participant for participant in os.listdir(study_video_path) if participant not in files_to_ignore]
    participants = [
        "1048", "1251", "1483", "1676", "2103", "2313", "2698",
        "2946", "3157", "3203", "3882", "3339", "5009", "5099",
        "5124", "5233", "5310", "5702", "6488", "7136", "7782",
        "7797", "8184", "8436", "8758", "8786", "9055", "9385",
        "9777", "9941"
    ]

    print(f"Participants are : {len(participants)}")

    video_clipping_durations = [1, 3]
    videos_to_clip = "main"

    for video_clipping_duration in video_clipping_durations:
        print(f"Begin Creating data set with clipping duration = {video_clipping_duration}")
        clipVideoEnd(
            study_video_path=study_video_path,
            participants=participants,
            videos_to_clip=videos_to_clip,
            video_clipping_duration=video_clipping_duration,
            output_path=output_path
        )

if __name__=="__main__":
    main()