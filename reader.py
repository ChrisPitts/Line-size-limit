from tkinter import *
from tkinter import filedialog


def onclick_button_browse_files():
    directory = filedialog.askopenfilename()
    if len(directory) != 0:
        entry_file_address.delete(0, END)
        entry_file_address.insert(0, directory)


def generate_output_window():
    try:
        file_address = entry_file_address.get()
        open(file_address)
    except Exception:
        error_string.set("File address invalid")
        return

    try:
        max_line_length = int(entry_max_length.get())
    except Exception:
        error_string.set("Max line length invalid")
        return

    window_output = Tk()
    text = Text(window_output)
    text.grid(row=0, column=0, sticky='W')
    text.insert(END, get_excess_lines(file_address, max_line_length))

    window_output.mainloop()


def get_excess_lines(file_address, max_line_length):
    current_line = 1
    return_str = ""

    for line in open(file_address, 'r').readlines():
        while line[0] == ' ':
            line = line[1:]
        if len(line) > max_line_length:
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
