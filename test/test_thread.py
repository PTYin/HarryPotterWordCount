import matplotlib
from matplotlib import pyplot as plt
import tkinter as tk
import threading
import InputDialog as dialog
import re


class Test:

    def __init__(self):
        self.expected_percentage = 0.2
        file = tk.filedialog.askopenfilename(title='open file', filetypes=[('text', '*.txt'), ('All Files', '*')])
        self.root = dialog.InputDialog(self)
        self.root.mainloop()
        self.root.destroy()
        self.run(file)
        print("hi")

    def run(self, file):
        thread = threading.Thread(target=self.target, args=(file,))
        thread.start()

    def target(self, f):
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
        # max 9
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
        # print(max_list, [val / total_words for val in max_count], sep="\n")
        # maxList.append("其它")
        # maxCount.append(int((1 - nowPercentage) * totalWords))

        fig = plt.figure(figsize=(32, 32))
        print('here')
        ax1 = fig.add_subplot(111)
        # plt.title('Harry Potter Words Count')
        tuple_builder = [0.0 for index in range(len(max_count))]
        tuple_builder[0] = 0.1
        explode = tuple(tuple_builder)
        ax1.pie(max_count, labels=max_list, autopct='%1.1f%%', explode=explode, textprops={'size': 'larger'})
        ax1.labels = max_list
        ax1.x = max_count
        ax1.explode = explode
        print('here')
        ax1.axis('equal')
        print('here')
        ax1.set_title('Harry Potter Words Count')
        print('here')


if __name__ == "__main__":
    test = Test()