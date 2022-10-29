# This file is able to parse the relevant info of the BBB video, Albert Gubau NIA: 229416
import os


def parse_video_info(in_file):

    # ffmpeg -i displays a lot of info, so we save it in a .txt
    command_line = 'ffmpeg -i ' + str(in_file) + ' 2> full_result.txt'
    os.system(command_line)

    print("")
    print("This is the relevant information that we can retrieve of the BBB video:\n")

    with open('full_result.txt') as result:
        lines = result.readlines()
    for line in lines:
        if line.__contains__("Duration") or line.__contains__("Stream"):
            print(line)

    os.remove("full_result.txt")


parse_video_info("BBB.mp4")
