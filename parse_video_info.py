# This file is able to parse the relevant info of the BBB video, Albert Gubau NIA: 229416
import os


def parse_video_info(in_file):

    # ffmpeg -i displays a lot of info, so we save it in a .txt
    os.system('ffmpeg -i ' + str(in_file) + '.mp4 2> full_result.txt')

    print("")
    print("This is the relevant information that we can retrieve from the video:\n")

    with open('full_result.txt') as result:  # We read the lines of the saved txt document with the info of the video
        lines = result.readlines()
    for line in lines:
        if line.__contains__("Duration") or line.__contains__("Stream"):  # These are our important flags
            print(line)

    os.remove("full_result.txt")  # We remove the info result


# Call the function with the BBB video
parse_video_info("BBB")
