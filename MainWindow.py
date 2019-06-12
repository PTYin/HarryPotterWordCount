from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # NavigationToolbar2TkAgg

import tkinter as tk
from tkinter import filedialog

import threading
import re
import InputDialog


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()  # 创建主窗体
        self.root.geometry("600x500")
        menubar = tk.Menu(self.root)
        self.canvas = tk.Canvas(self.root)
        menubar.add_command(label='open file', command=self.open_file_dialog)
        self.root['menu'] = menubar
        self.expected_percentage = 0.8

    def open_file_dialog(self):
        file = tk.filedialog.askopenfilename(title='open file', filetypes=[('text', '*.txt'), ('All Files', '*')])
        self.dialog = InputDialog.InputDialog(self)
        self.dialog.mainloop()
        load_thread = threading.Thread(target=self.create_matplotlib, args=(file,))
        load_thread.start()

    def create_matplotlib(self, f):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        plt.style.use("ggplot")

        file = open(f, 'r', encoding='utf-8')
        word_list = list(file.read())
        word_count = {}
        total_words = 0
        for word in word_list:
            if re.match('\\w', word):
                total_words += 1
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        max_list = []
        max_count = []
        now_percentage = 0
        while now_percentage < self.expected_percentage:
            max_count.append(0)
            max_list.append("")
            for word, count in word_count.items():
                if max_count[-1] < count:
                    max_count[-1] = count
                    max_list[-1] = word
            word_count.pop(max_list[-1])
            now_percentage = 0
            for val in max_count:
                now_percentage += val / total_words
        print(max_list, [val / total_words for val in max_count], sep="\n")

        fig = plt.figure(figsize=(32, 32))
        ax1 = fig.add_subplot(111)
        tuple_builder = [0.0 for index in range(len(max_count))]
        tuple_builder[0] = 0.1
        explode = tuple(tuple_builder)
        ax1.pie(max_count, labels=max_list, autopct='%1.1f%%', explode=explode, textprops={'size': 'larger'})
        ax1.axis('equal')
        ax1.set_title('Words Count')

        self.create_form(fig)

    def create_form(self, figure):
        self.clear()
        figure_canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas = figure_canvas.get_tk_widget()

        self.toolbar = NavigationToolbar2Tk(figure_canvas, self.root)
        self.toolbar.update()
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def clear(self):
        self.canvas.destroy()
        if hasattr(self, 'toolbar'):
            self.toolbar.destroy()


if __name__ == "__main__":
    mainWindow = MainWindow()
    mainWindow.root.mainloop()
