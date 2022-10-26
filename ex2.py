# This file is able to parse the relevant info of the BBB video, Albert Gubau NIA: 229416
import os


def ex2(in_file):

    if os.path.exists('output.mp3'):
        os.remove('output.mp3')

    if os.path.exists('output.aac'):
        os.remove('output.aac')

    if os.path.exists('ex2output.mp4'):
        os.remove('ex2output.mp4')

    command_line = 'ffmpeg -i BBB.mp4 -vn -ac 2 output.mp3'  # -vn means no video
    os.system(command_line)

    command_line = 'ffmpeg -i BBB.mp4 -vn -b:a 100K output.aac'

    os.system(command_line)

    command_line = 'ffmpeg -i BBB_1min.mp4 -i output.mp3 -i output.aac -map 0 -map 1:a -map 2:a -c copy ex2output.mp4 '

    os.system(command_line)

    command_line = 'ffmpeg -i output.mp4'

    os.system(command_line)


ex2("BBB.mp4")
