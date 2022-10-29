import os


def ex4(in_file):

    # ffmpeg -i displays a lot of info, so we save it in a .txt
    command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 2> full_result_ex4.txt'
    os.system(command_line)

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

    # Select a broadcasting standard taking into account the audio tracks
    if audio_lines.__contains__(" dra "):
        print("The broadcasting standard must be DTMB.")

    elif audio_lines.__contains__(" ac3 ") and \
            not audio_lines.__contains__(" mp3 ") and \
            not audio_lines.__contains__(" aac ") and \
            not audio_lines.__contains__(" mp2 ") and \
            not audio_lines.__contains__(" mp1 "):

        print("The broadcasting standard can be ATSC because the video only has ac3 audio tracks.")

    elif audio_lines.__contains__(" aac ") and \
            not audio_lines.__contains__(" mp3 ") and \
            not audio_lines.__contains__(" ac3 ") and \
            not audio_lines.__contains__(" mp2 ") and \
            not audio_lines.__contains__(" mp1 "):

        print("The broadcasting standard can be ISDB because the video only has aac audio tracks.")


    else:
        print("The broadcasting standrad can be any of the following ones: ATSC, ISDB, DTMB, DVB")





    os.remove("full_result_ex4.txt")


ex4("BBB")
