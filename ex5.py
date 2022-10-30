# This file is able to integrate the previous tasks into one class, Albert Gubau NIA: 229416
import os


class Lab2SCAV:

    # Initialize the interactive menu and the class attributes
    def __init__(self, in_file, out_ex2, out_ex3):
        self.in_file = in_file
        self.out_ex2 = out_ex2
        self.out_ex3 = out_ex3

        print("\nThe following script always uses the BBB video as an input.")

        continuation = True
        while continuation:
            try:
                option = int(input("\nChoose the exercise that you want to execute:\n"
                                   "1 --> Task 1 (Get video information)\n"
                                   "2 --> Task 2 (Create a new container with multiple audio tracks)\n"
                                   "3 --> Task 3 (Resize the video with a given input)\n"
                                   "4 --> Task 4 (Broadcasting standard selector)\n"
                                   "0 --> EXIT\n"
                                   "Write the number here: "))
            except ValueError as e:
                print(e)
                option = 0

            if option == 1:
                print("")
                print("########################## VIDEO INFORMATION (Task 1) ################################")
                self.parse_video_info()

            elif option == 2:
                print("")
                print("########################## MULTIPLE AUDIO TRACKS (Task 2) ################################")
                self.ex2()

            elif option == 3:

                print("")
                print("########################## RESIZE VIDEO (Task 3) ################################")

                try:
                    width = int(input("\nChoose what resize do you want:"
                                      "\nWrite the width here (e.g 1280): "))

                    height = int(input("Write the height here (e.g 720): "))

                except ValueError as e:
                    width = 1280
                    height = 720
                    print(e)

                self.resize_video(width, height)

            elif option == 4:
                print("")
                print(
                    "########################## VIDEO BROADCASTING STANDARDS (Task 4) ################################")
                print("")
                self.in_ex4 = input("Choose the file that you want, in the same folder and without format "
                                    "(e.g to use frog.mp4 that is in the same folder as this script just write frog): ")
                self.ex4()

            else:
                continuation = False

    # Task 1
    def parse_video_info(self):

        # ffmpeg -i displays a lot of info, so we save it in a .txt
        os.system('ffmpeg -i ' + str(self.in_file) + '.mp4 2> full_result.txt')

        print("")
        print("This is the relevant information that we can retrieve from the video:\n")

        # We read the lines of the saved txt document with the info of the video
        with open('full_result.txt') as result:
            lines = result.readlines()

        for line in lines:  # These are our important flags
            if line.__contains__("Duration") or line.__contains__("Stream") or line.__contains__(" Video "):
                print(line)

        os.remove("full_result.txt")  # We remove the info result

    # Task 2
    def ex2(self):

        print("Charging...")
        # Remove the previous call result
        if os.path.exists(self.out_ex2 + '.mp4'):
            os.remove(self.out_ex2 + '.mp4')

        # Get the audio of the video as a stereo mp3
        os.system('ffmpeg -i ' + str(self.in_file) + '.mp4 -vn -ac 2 output.mp3 2>NUL')  # -vn means no video

        # Get the audio of the video as an aac audio with 100kbits/s of bitrate (lower bit-rate)
        os.system('ffmpeg -i ' + str(self.in_file) + '.mp4 -vn -b:a 100K output.aac 2>NUL')

        # Map the audio tracks to the 1-minute version of the BBB video
        os.system('ffmpeg -i BBB_1min.mp4 -i output.mp3 -i output.aac '
                  '-map 0 -map 1:a -map 2:a -c copy ' + str(self.out_ex2) + '.mp4 2>NUL')

        # Remove the temporary file storing the stderr that ffmpeg writes in the terminal
        os.remove("NUL")

        # Show the information of the output video
        print("\nThe resulting information for the video resulting of executing Ex2 is:")
        self.in_file = self.out_ex2
        self.parse_video_info()
        self.in_file = self.in_file

        # Remove temporary files that we will use to generate the video with multiple audio tracks
        os.remove('output.mp3')
        os.remove('output.aac')

    # Task 3
    def resize_video(self, w, h):

        print("Charging...")

        # We check what resolution is the one that the user wants, and we store the correspondent command line

        if os.path.exists(self.out_ex3 + ".mp4"):
            os.remove(self.out_ex3 + ".mp4")

        if (w > 0 and h > 0) and (w % 2 == 0 and h % 2 == 0):
            command_line = 'ffmpeg -i ' + str(self.in_file) + '.mp4 -vf scale=' + str(w) + ':' + str(h) \
                           + ' ' + str(self.out_ex3) + '.mp4 2>NUL'

        else:
            command_line = ''
            print("The resolution value is not valid (width and height must be positive and divisible by 2)"
                  ", exiting program... ")

        # Call the command line in the terminal
        os.system(command_line)

        # Remove the temporary generated file of the ffmpeg stderr
        os.remove('NUL')

        # Let's see the resulting video info to check that the resolution has been changed properly
        self.in_file = self.out_ex3
        self.parse_video_info()
        self.in_file = self.in_file

    # Task 4
    def ex4(self):

        # ffmpeg -i displays a lot of info, so we save it in a .txt
        command_line = 'ffmpeg -i ' + str(self.in_ex4) + '.mp4 2> full_result_ex4.txt'
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


# Create a class instance
lab2_scav = Lab2SCAV("BBB", "ex2output", "ex3output")
