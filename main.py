# URL Sanitizer - This app will accept an Amazon.com URL and strip all the cruft,
# leaving a nice, clean and pretty URL

#     Copyright (C) 2023  ~ David Burklin

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter as tk
import pyperclip
#from functions import sanitize

def sanitize(event):
    my_url = entry.get()
    foo = my_url.split("/?")
    descriptive_url = foo[0]

    foo = descriptive_url.split("/")
    
    short_url = foo[0] + "//" + foo[2] + "/" + foo[4] + "/" + foo[5]

    label_output1.config(text = short_url)
    label_output1.pack()
    label_output2.config(text = descriptive_url)
    label_output2.pack()

def copy1(event):
    pyperclip.copy(label_output1.cget("text"))

def copy2(event):
    pyperclip.copy(label_output2.cget("text"))

window = tk.Tk()
window.minsize(400, 150)
label = tk.Label(text="URL Sanitizer\n\n")
label.pack()
label_input = tk.Label(text="Please enter URL")
label_input.pack()
entry = tk.Entry(width=60)
entry.pack()
san_button = tk.Button(text="Sanitize")
san_button.pack()
san_button.bind("<Button-1>", sanitize)
label_output1 = tk.Label(text="Shortest URL")
label_output1.pack()
copy_1 = tk.Button(text = "Copy Shortest URL")
copy_1.pack()
copy_1.bind("<Button-1>", copy1)
label_output2 = tk.Label(text="Descriptive URL")
label_output2.pack()
copy_2 = tk.Button(text = "Copy Descriptive URL")
copy_2.pack()
copy_2.bind("<Button-1>", copy2)

window.mainloop()