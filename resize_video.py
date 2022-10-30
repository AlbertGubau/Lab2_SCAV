# This file is able to resize the BBB video given any input, Albert Gubau NIA: 229416
import os


def resize_video(in_file, out_file, w, h):
    # We check what resolution is the one that the user wants, and we store the correspondent command line

    if (w > 0 and h > 0) and (w % 2 == 0 and h % 2 == 0):
        command_line = 'ffmpeg -i ' + str(in_file) + '.mp4 -vf scale=' + str(w) + ':' + str(h) + ' ' \
                       + str(out_file) + '.mp4 '

    else:
        command_line = ''
        print("The resolution value is not valid (width and height must be positive and divisible by 2)"
              ", exiting program... ")

    # Call the command line in the terminal
    os.system(command_line)


# Interactive menu
print("")
print("############################## RESIZE VIDEO PROGRAM ############################################")
print("")
print("The input video file must be an mp4 in the same folder as this python script, ")
print("and the name of it needs to be 'BBB'. Please do not specify the format of the output ")
print("If we ask you for the name of the input/output, just write the name,")
print("for example, if you want the name to be frog, just write frog, do not write frog.mp4 ")
print("in the output name.")
print("")

# Input for the option

try:
    # Input filename
    input_name = str(input("Choose the input file that you want to resize: "))

    if not os.path.exists(input_name + ".mp4"):
        input_name = "BBB"

    width = int(input("Choose what resize do you want:"
                      "\nWrite the width here (e.g 1280): "))

    height = int(input("\nWrite the height here (e.g 720): "))

    # We check that the output name chosen by the user is not the same as the input name
    boolean = False

    while not boolean:
        output_name = str(input("Choose the name of the output file: "))
        if output_name != input_name:
            boolean = True

        if not boolean:
            print("")
            print("The chosen name is the same as the input, try with another name.")
            print("")

    # Call the function
    resize_video(input_name, output_name, width, height)

except Exception as e:
    print(e)
