import tkinter as tk
from random import *

class AreYouStupidWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        # Constants
        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()
        FONT = "Helvetica"

        # Window definition
        self.geometry(f"450x500+{randint(25, SCREEN_WIDTH-470)}+{randint(10, SCREEN_HEIGHT-560)}")
        self.iconbitmap("icon.ico")
        self['background'] = "#EBF6F4"
        self.resizable(width=False, height=False)
        self.title(" " * 49 + "Are you stupid ?")

        # Content
        self.are_you_stupid = tk.Label(
            self,
            text="Are you stupid ?",
            font=(FONT, 25)
        )
        self.yes_button = tk.Button(
            self,
            text="Yes🙂",
            font=(FONT, 15),
            command=lambda: YouAreStupidWindow(master)
        )
        self.other_button = tk.Button(
            self,
            text="Other",
            font=(FONT, 15),
            command=master.destroy
        )
        self.no_button = tk.Button(
            self,
            text="No🙃",
            font=(FONT, 15),
            command=lambda: AreYouStupidWindow(master)
        )
        self.exit_button = tk.Button(
            self,
            text="Exit",
            font=(FONT, 15),
            command=self.destroy
        )
        # Element display --- Columns & Rows settings
        self.columnconfigure(0, weight=0, minsize=50)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0, minsize=10)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=0, minsize=10)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=0, minsize=50)

        self.rowconfigure(0, weight=0, minsize=50)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0, minsize=10)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=0, minsize=10)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=0, minsize=50)

        # Element display --- Buttons
        self.are_you_stupid.grid(column=1, columnspan=5, row=1, sticky="ew")
        self.yes_button.grid(column=1, row=3, sticky="ew")
        self.other_button.grid(column=3, row=3, sticky="ew")
        self.no_button.grid(column=5, row=3, sticky="ew")
        self.exit_button.grid(column=3, row=5, sticky="new")


class YouAreStupidWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        # Constants
        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()
        FONT = "Helvetica"

        # Window definition
        self.geometry(f"450x500+{randint(25, SCREEN_WIDTH-470)}+{randint(10, SCREEN_HEIGHT-560)}")
        self.iconbitmap("icon.ico")
        self['background'] = "#EBF6F4"
        self.resizable(width=False, height=False)
        self.title(" " * 49 + "Are you stupid ?")

        # Content
        self.you_button = tk.Button(
            self,
            text="You",
            font=(FONT, 15),
            command=lambda: self.are_button.grid(column=3, row=1, sticky="ew")
        )
        self.are_button = tk.Button(
            self,
            text="Are",
            font=(FONT, 15),
            command=lambda: self.stupid_button.grid(column=5, row=1, sticky="ew")
        )
        self.stupid_button = tk.Button(
            self,
            text="Stupid",
            font=(FONT, 15),
            command=lambda: print("Session locked")
        )
        # Element display --- Columns & Rows settings
        self.columnconfigure(0, weight=0, minsize=50)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0, minsize=10)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=0, minsize=10)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=0, minsize=50)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)

        # Element display --- Buttons
        self.you_button.grid(column=1, row=1, sticky="ew")
        # self.are_button.grid(column=3, row=1, sticky="ew")  # Those buttons will be displayed by other buttons
        # self.stupid_button.grid(column=5, row=1, sticky="ew")


if __name__ == '__main__':
    root = tk.Tk()
    AreYouStupidWindow(root)
    root.withdraw()  # Hide root window, see https://stackoverflow.com/questions/1406145
    root.mainloop()
