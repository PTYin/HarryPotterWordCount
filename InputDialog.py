import tkinter as tk
import MainWindow


class InputDialog(tk.Tk):

    def __init__(self, main_window):
        tk.Tk.__init__(self)
        self.main_window = main_window
        tk.Label(self, text="Input Expected Percentage:").grid(row=0, column=0)
        self.input = tk.Entry(self, bd=5)
        self.input.insert(0, "20%")
        self.input.grid(row=0, column=1)
        tk.Button(self, text="Commit", command=self.__commit).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def __commit(self):
        self.main_window.expected_percentage = float(self.input.get().strip("%"))/100
        self.quit()
        self.withdraw()
