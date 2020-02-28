from tkinter import *
from tkinter import filedialog


#   onclick_button_browse_files()
#
#   Description
#       Prompts the user to choose the file
def onclick_button_browse_files():

    directory = filedialog.askopenfilename()    # Prompt the user to choose a file

    if len(directory) != 0:     # The user chose a file
        # Fill in the file address text entry
        entry_file_address.delete(0, END)
        entry_file_address.insert(0, directory)


#   generate_output_window()
#
#   Description
#       Generates a window that tells the user what lines
#       exceed the character max
def generate_output_window():
    try:
        file_address = entry_file_address.get()
        open(file_address)
    except Exception:   # The user inputted an invalid file address
        error_string.set("File address invalid")
        return

    try:
        max_line_length = int(entry_max_length.get())
    except Exception:   # The user inputted an invalid value for max line
        error_string.set("Max line length invalid")
        return

    window_output = Tk()    # The window that shows the output
    text = Text(window_output)  # The field that holds the output string
    text.grid(row=0, column=0, sticky='W')

    # Write the output string to the output window
    text.insert(END, get_excess_lines(file_address, max_line_length))

    window_output.mainloop()


#   get_excess_lines(file_address, max_line_length)
#
#   Parameters
#       file_address-       (string)    holds the address of the file to be read
#       max_line_length-    (int)       holds the maximum length of each line
#
#   Return
#       A string containing the lines that exceed the max length
#       Format:
#           Line:   #
#           Characters: <characters in line>
#           Line text:  <Contents of line>
#
#   Description
#       Returns a string containing information about every line
#       that exceeds the character limit
def get_excess_lines(file_address, max_line_length):
    current_line = 1
    return_str = ""

    #   Loop through each line in the file
    for line in open(file_address, 'r').readlines():

        #   Remove all the spaces from the beginning of the line
        while line[0] == ' ':
            line = line[1:]

        #   If the line exceeds the maximum length
        if len(line) > max_line_length:
            #   Add the line's information to the return string
            return_str = return_str + "Line:\t%i\n" % current_line
            return_str = return_str + "Characters:\t%i\n" % len(line)
            return_str = return_str + "Line Text:\t%s\n" % line
            return_str = return_str + "\n"
        current_line = current_line + 1

    return return_str


#   Initialize window
window_main = Tk()
window_main.title("Line Length Checker")

error_string = StringVar()
#   Initialize labels
Label(window_main, text="File Address", ).grid(row=0, column=0, sticky='W')
Label(window_main, text="Max File Length").grid(row=1, column=0, sticky='W')
Label(window_main, textvariable=error_string, fg = "red").grid(row=2, column=1, sticky='W')

#   Initialize entries fields
entry_file_address = Entry(window_main, width=50)
entry_max_length = Entry(window_main, width=50)

entry_file_address.grid(row=0, column=1, sticky='w')
entry_max_length.grid(row=1, column=1, sticky='W')

#   Initialize buttons
button_browse_files = Button(window_main, text="Browse", command=onclick_button_browse_files)
button_submit = Button(window_main, text="Submit", command=generate_output_window)

button_browse_files.grid(row=0, column=2, sticky='W')
button_submit.grid(row=2, column=0, sticky='W')

window_main.mainloop()
