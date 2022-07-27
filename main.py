import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger, PdfFileReader

box = tk.Tk()
box.withdraw()
while True:
    while True:
        list_files = filedialog.askopenfilenames(parent=box,
                                                 title="Choose files",
                                                 filetypes=[("PDF files", '*.pdf')])
        if len(list_files) < 2:
            action = input("You have to select at least two files. Do you want to try again?"
                           " If so, write 'yes', else write anything, and press enter. \n")
            if action.lower() != "yes":
                exit()
        else:
            break

    mergedObject = PdfFileMerger()
    for path in list_files:
        mergedObject.append(PdfFileReader(path))
    while True:
        save_file_path = filedialog.asksaveasfilename(title="Choose file name",
                                                  defaultextension=".pdf")
        if save_file_path == '':
            action = input("You didn't choose any filename. "
                           "If you want choose filename write 'yes', else write anything, and press enter. \n")
            if action.lower() != "yes":
                exit()
        else:
            break

    mergedObject.write(save_file_path)
    action = input("If you want to join other files, write 'yes', else write anything, and press enter. \n")
    if action.lower() != "yes":
        break
