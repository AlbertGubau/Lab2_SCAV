# This file is able to deduce the broadcasting standard of an input video, Albert Gubau NIA: 229416
import os


def ex4(in_file):
    # ffmpeg -i displays a lot of info, so we save it in a .txt
    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 2> full_result_ex4.txt'
    os.system(command_line)

    # Show the audio tracks of the video
    print("")
    print("The input video has the following audio tracks:\n")

    # Extract the lines containing audio tracks information
    audio_lines = ""
    with open('full_result_ex4.txt') as result:
        lines = result.readlines()
    for line in lines:
        if line.__contains__("Audio"):
            print(line)
            audio_lines += line

    # Simple (not robust enough) selection of a broadcasting standard taking into account the audio tracks

    # Only DTMB uses DRA as audio coder
    if audio_lines.__contains__(" dra "):
        print("The broadcasting standard must be DTMB because it has a DRA audio track.")

    # ATSC only works with AC-3
    elif audio_lines.__contains__(" ac3 ") and \
            not audio_lines.__contains__(" aac ") and \
            not audio_lines.__contains__(" mp3 ") and \
            not audio_lines.__contains__(" mp2 ") and \
            not audio_lines.__contains__(" mp1 "):

        print("The broadcasting standard can be ATSC or DTMB because the video only has ac3 audio tracks.")

    # ISDB only works with AAC or AAC Latam version
    elif (audio_lines.__contains__(" aac ") or audio_lines.__contains__(" aac_latm ")) and \
            not audio_lines.__contains__(" ac3 ") and \
            not audio_lines.__contains__(" mp3 ") and \
            not audio_lines.__contains__(" mp2 ") and \
            not audio_lines.__contains__(" mp1 "):

        print("The broadcasting standard can be ISDB or DTMB because the video only has aac audio tracks.")

    # We can not find the answer
    else:
        print("The broadcasting standard can be DVB, DTMB or we can not determine it.")

    # Remove the generated info file of the video
    os.remove("full_result_ex4.txt")


# Call the function with the BBB video
ex4("BBB")
