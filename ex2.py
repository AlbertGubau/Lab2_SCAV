# This file is able to create a new BBB container using multiple audio tracks, Albert Gubau NIA: 229416
import os
from parse_video_info import *


def ex2(in_file):

    # Remove the previous call result
    if os.path.exists('ex2output.mp4'):
        os.remove('ex2output.mp4')

    # Get the audio of the video as a stereo mp3
    os.system('ffmpeg -i ' + str(in_file) + '.mp4 -vn -ac 2 output.mp3')  # -vn means no video

    # Get the audio of the video as an aac audio with 100kbits/s of bitrate (lower bit-rate)
    os.system('ffmpeg -i ' + str(in_file) + '.mp4 -vn -b:a 100K output.aac')

    # Map the audio tracks to the 1-minute version of the BBB video
    os.system('ffmpeg -i BBB_1min.mp4 -i output.mp3 -i output.aac -map 0 -map 1:a -map 2:a -c copy ex2output.mp4')

    # Show the information of the output video
    print("\nThe resulting information for the video resulting of executing Ex2 is:")
    parse_video_info('ex2output')

    # Remove temporary files that we will use to generate the video with multiple audio tracks
    os.remove('output.mp3')
    os.remove('output.aac')
    

ex2("BBB")
