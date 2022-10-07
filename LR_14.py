import tkinter as tk


def task1():
    class Convert_farengeit_to_celsius(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            root.geometry("250x150")
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            pady = 5
            self.none = tk.Label(self, text=" ")
            # self.none.grid(row=0, column=0, pady=pady)
            self.text_about = tk.Label(self, text="Введите температуру в Фаренгейтах", font="Arial 10")
            self.text_about.grid(row=1, column=0, pady=pady, columnspan=2)
            self.farengeit = tk.Entry(self)
            self.farengeit.grid(row=2, column=0, pady=pady, columnspan=2)
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "convert"
            self.hi_there.grid(row=3, column=0, pady=pady)
            self.hi_there["command"] = self.convert
            self.quit = tk.Button(self, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.grid(row=5, column=0, pady=pady, columnspan=3)
            self.result = tk.Label(self, font="Arial 10")
            self.result_1 = tk.Label(self, background="lightgrey", font="Arial 14")
            self.result_1["text"] = ""
            self.result["text"] = "результат: "
            self.result.grid(row=3, column=1, pady=pady, sticky="w")
            self.result_1.grid(row=3, column=1, pady=pady, sticky="e")
            # крч сами ковыряйте этот уродск, кто хочет красивск

        def convert(self):
            self.result_1["text"] = f"{str(((int(self.farengeit.get()) - 32) * 5 / 9))[:5]}"

    root = tk.Tk()
    app = Convert_farengeit_to_celsius(master=root)
    app.mainloop()


def task2():
    def generate_ru_en():
        from random import choice
        import requests
        from googletrans import Translator
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        WORDS = response.content.split()  # .splitlines()
        WORDS = [word.decode("utf-8") for word in WORDS]
        en_word = choice(WORDS)
        print(en_word)
        ru_word = Translator().translate(str(en_word), src="en", dest="ru").text
        print(ru_word)
        return ru_word, en_word

    class Translate(tk.Frame):
        globals()["ru_word"], globals()["en_word"] = generate_ru_en()
        globals()["attempt"] = 5

        def __init__(self, master=None):
            super().__init__(master)
            root.geometry("250x280")
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            pady = 5
            # self.none = tk.Label(self, text=" ")
            # self.none.grid(row=0, column=0, pady=pady)

            self.ru_word = tk.Label(self, text=f"Загадано слово: {globals()['ru_word']}", font="Arial 10")
            self.ru_word.grid(row=0, column=0, pady=pady)

            self.text_about = tk.Label(self, text="Введите перевод слова", font="Arial 10")
            self.text_about.grid(row=1, column=0, pady=pady)

            self.word = tk.Entry(self)
            self.word.grid(row=2, column=0, pady=pady)

            self.trans = tk.Button(self, font="Arial 10")
            self.trans["text"] = "  translate  "
            self.trans.grid(row=3, column=0, pady=pady, sticky="we")
            self.trans["command"] = self.translate

            self.result_1 = tk.Label(self, background="lightgrey", font="Arial 12")
            self.result_1["text"] = ""
            self.result_1.grid(row=4, column=0, pady=pady, sticky="we")

            self.result_2 = tk.Label(self, background="lightgrey", font="Arial 12")
            self.result_2["text"] = ""
            self.result_2.grid(row=5, column=0, pady=pady, sticky="we")

            self.restart = tk.Button(self, font="Arial 10")
            self.restart["text"] = "  restart  "
            self.restart.grid(row=6, column=0, pady=pady, sticky="we")
            self.restart["command"] = self.restart_game

            self.quit = tk.Button(self, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.grid(row=7, column=0, pady=pady, sticky="we")

            # крч сами ковыряйте этот уродск, кто хочет красивск

        def translate(self):
            if globals()["attempt"] > 0:
                if self.word.get() == globals()["en_word"]:
                    self.result_1["text"] = "Правильно!"
                else:
                    self.result_1["text"] = "Неправильно!"
                    globals()["attempt"] -= 1
                    self.result_2["text"] = f" Осталось попыток: {globals()['attempt']}"
            else:
                self.result_1["text"] = "Вы проиграли!"
                self.result_2["text"] = f" Правильный ответ: {globals()['en_word']}"

        def restart_game(self):
            globals()["ru_word"], globals()["en_word"] = generate_ru_en()
            self.ru_word["text"] = f"Загадано слово: {globals()['ru_word']}"
            self.result_1["text"] = "                 "
            globals()["attempt"] = 5

    root = tk.Tk()
    app = Translate(master=root)
    app.mainloop()


def task3():
    import tkinter.filedialog as fd

    class Save_text_as(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            root.geometry("300x270")
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            pady = 5

            self.text_about = tk.Label(self, text="Введите текст, "
                                                  "который следует сохранить:", font="Arial 10")
            self.text_about.grid(row=0, column=0, pady=pady)

            self.input_text = tk.Text(self, width=30, height=10, font="Arial 10")
            self.input_text.grid(row=1, column=0, pady=pady, sticky="we")

            self.save = tk.Button(self, font="Arial 10", text="  save  ", command=self.file_save)
            self.save.grid(row=2, column=0, pady=pady, sticky="we")

        def file_save(self):
            f = fd.asksaveasfile(mode='w', defaultextension=".txt")
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            text2save = str(self.input_text.get(1.0, "end-1c"))  # starts from `1.0`, not `0.0`
            f.write(text2save)
            f.close()  # `()` was missing.

    root = tk.Tk()
    app = Save_text_as(master=root)
    app.mainloop()


def task5():
    import tkinter.filedialog as fd
    import tkinter.messagebox as mb
    from tkinter import ttk
    class Count_sphere_volume(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            root.geometry("260x230")
            root.title("объем сферы")
            # root.configure(background="lightgrey")
            self.master = master
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            pady = 7

            self.text_about = tk.Label(self, text="Рассчет объема сферы", font="Arial 10")
            self.text_about.grid(row=0, column=0, columnspan=2, pady=pady)

            self.text_radius = tk.Label(self, text="Введите радиус\nсферы:", font="Arial 10")
            self.text_radius.grid(row=1, column=0, pady=pady)

            self.radius = tk.Entry(self)
            self.radius.grid(row=1, column=1, pady=pady)

            self.text_rezult = tk.Label(self, text="Результат\nвычеслений:", font="Arial 10")
            self.text_rezult.grid(row=2, column=0, pady=pady)

            self.rezult = tk.Text(self, font="Arial 10", width=17, height=1)
            self.rezult.grid(row=2, column=1, pady=pady)

            self.count_button = tk.Button(self, font="Arial 10", text="  Вычислить  ", command=self.count, width=10)
            self.count_button.grid(row=3, column=0, columnspan=2, pady=pady)

            self.save = tk.Button(self, font="Arial 10", text="Сохранить как:", command=self.file_save, width=12)
            self.save.grid(row=4, column=0, pady=pady, sticky="w")

            self.save_as_combobox = ttk.Combobox(self, values=["txt", "html", "json"], width=7)
            self.save_as_combobox.grid(row=4, column=1, pady=pady, sticky="e")

        def count(self):
            if self.radius.get() != "":
                self.rezult.insert(1.0, str(4 / 3 * 3.14 * int(self.radius.get()) ** 3))
            else:
                mb.showerror("Ошибка", "Введите корректный радиус сферы!")

        def file_save(self):
            if self.rezult != None:
                f = fd.asksaveasfile(mode='w', defaultextension="." + self.save_as_combobox.get())
                if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                    return
                text2save = str(self.rezult.get(1.0, "end-1c"))  # starts from `1.0`, not `0.0`
                if self.save_as_combobox.get() == "txt":
                    f.write(text2save)
                if self.save_as_combobox.get() == "html":
                    f.write(f"<html><body><h1>{text2save}</h1></body></html>")
                if self.save_as_combobox.get() == "json":
                    import json
                    f.write(json.dumps(text2save))
                f.close()  # `()` was missing.
            else:
                mb.showerror("Ошибка", "Сначала вычислите объем сферы!")

    root = tk.Tk()
    app = Count_sphere_volume(master=root)
    app.mainloop()


def task4():
    def test_task():
        import PyQt5.QtWidgets as qtw
        import PyQt5.QtGui as qtg
        import PyQt5.QtCore as qtc
        import sys
        class MainWindow(qtw.QWidget):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("Работа с файлами")
                self.setLayout(qtw.QVBoxLayout())
                # self.setWindowIcon(qtg.QIcon("icon.png"))
                self.setFixedSize(300, 200)
                self.initUI()

            def initUI(self):
                self.text_about = qtw.QLabel("Работа с файлами")
                self.text_about.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_about)

                self.text_file = qtw.QLabel("Выберите файл:")
                self.text_file.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_file)

                self.file = qtw.QPushButton("Выбрать файл")
                self.file.clicked.connect(self.file_open)
                self.layout().addWidget(self.file)

                self.text_rezult = qtw.QLabel("Результат:")
                self.text_rezult.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_rezult)

                self.rezult = qtw.QTextEdit()
                self.rezult.setFont(qtg.QFont("Arial", 10))
                self.rezult.setReadOnly(True)
                self.layout().addWidget(self.rezult)

            def file_open(self):
                file_name = qtw.QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                            "Text files (*.txt);;All files (*.*)")
                if file_name[0]:
                    with open(file_name[0], "r") as f:
                        self.rezult.setText(f.read())

        app = qtw.QApplication(sys.argv)
        mw = MainWindow()
        mw.show()
        sys.exit(app.exec_())

    def task__1():
        import PyQt5.QtWidgets as qtw
        import PyQt5.QtGui as qtg
        import PyQt5.QtCore as qtc
        import sys
        class Convert_farengeit_to_celsius_2(qtw.QWidget):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("Конвертер")
                self.setLayout(qtw.QVBoxLayout())
                # self.setWindowIcon(qtg.QIcon("icon.png"))
                self.setFixedSize(400, 300)
                self.initUI()

            def initUI(self):
                # self.text_about = qtw.QLabel("Конвертер температур")
                # self.text_about.setFont(qtg.QFont("Arial", 10))
                # self.layout().addWidget(self.text_about)

                self.text_farengeit = qtw.QLabel("Введите температуру в Фаренгейтах:")
                self.text_farengeit.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_farengeit)

                self.farengeit = qtw.QLineEdit()
                self.farengeit.setFont(qtg.QFont("Arial", 10))
                self.farengeit.setValidator(qtg.QIntValidator())
                self.layout().addWidget(self.farengeit)

                self.count_button = qtw.QPushButton("Вычислить")
                self.count_button.clicked.connect(self.count)
                self.layout().addWidget(self.count_button)

                self.text_celsius = qtw.QLabel("Результат:")
                self.text_celsius.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_celsius)

                self.celsius = qtw.QLineEdit()
                self.celsius.setFont(qtg.QFont("Arial", 10))
                self.celsius.setReadOnly(True)
                self.layout().addWidget(self.celsius)

                self.quit_button = qtw.QPushButton("Выход")
                self.quit_button.clicked.connect(self.close)
                self.layout().addWidget(self.quit_button)

            def count(self):
                try:
                    self.celsius.setText(str((int(self.farengeit.text()) - 32) * 5 / 9))
                except:
                    self.celsius.setText("Ошибка")

        app = qtw.QApplication(sys.argv)
        mw = Convert_farengeit_to_celsius_2()
        mw.show()
        sys.exit(app.exec_())

    def task__2():
        import PyQt5.QtWidgets as qtw
        import PyQt5.QtGui as qtg
        import PyQt5.QtCore as qtc
        import sys
        def generate_ru_en():
            from random import choice
            import requests
            from googletrans import Translator
            word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
            response = requests.get(word_site)
            WORDS = response.content.split()  # .splitlines()
            WORDS = [word.decode("utf-8") for word in WORDS]
            en_word = choice(WORDS)
            print(en_word)
            ru_word = Translator().translate(str(en_word), src="en", dest="ru").text
            print(ru_word)
            return ru_word, en_word

        class Translate_2(qtw.QWidget):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("Угадай слово")
                self.setLayout(qtw.QVBoxLayout())
                # self.setWindowIcon(qtg.QIcon("icon.png"))
                self.setFixedSize(400, 400)
                self.initUI()

            def initUI(self):
                self.ru_word, self.en_word = generate_ru_en()
                self.attempts = 5

                self.text_about = qtw.QLabel("Угадай слово")
                self.text_about.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_about)

                self.text_word = qtw.QLabel("Слово: " + self.ru_word)
                self.text_word.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_word)

                self.word = qtw.QLineEdit()
                self.word.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.word)

                self.check_button = qtw.QPushButton("Проверить")
                self.check_button.clicked.connect(self.check)
                self.layout().addWidget(self.check_button)

                self.text_result = qtw.QLabel("Результат:")
                self.text_result.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_result)

                self.result = qtw.QLineEdit()
                self.result.setFont(qtg.QFont("Arial", 10))
                self.result.setReadOnly(True)
                self.layout().addWidget(self.result)

                self.text_attempts = qtw.QLabel("Осталось попыток: " + str(self.attempts))
                self.text_attempts.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_attempts)

                self.restart_button = qtw.QPushButton("Начать заново")
                self.restart_button.clicked.connect(self.restart)
                self.layout().addWidget(self.restart_button)

                self.quit_button = qtw.QPushButton("Выход")
                self.quit_button.clicked.connect(self.close)
                self.layout().addWidget(self.quit_button)

            def check(self):
                try:
                    if self.attempts > 0:
                        if self.word.text() == self.en_word:
                            self.result.setText("Вы угадали!")
                        else:
                            self.result.setText("Вы не угадали!")
                            self.attempts -= 1
                            self.text_attempts.setText("Осталось попыток: " + str(self.attempts))
                    else:
                        self.result.setText("Вы проиграли!\nверное слово:" +self.en_word)
                except:
                    self.result.setText("Ошибка")

            def restart(self):
                self.ru_word, self.en_word = generate_ru_en()
                self.attempts = 5
                self.text_word.setText("Слово: " + self.ru_word)
                self.result.setText("")
                self.text_attempts.setText("Осталось попыток: " + str(self.attempts))

        app = qtw.QApplication(sys.argv)
        mw = Translate_2()

        mw.show()
        sys.exit(app.exec_())

    def task__3():
        import PyQt5.QtWidgets as qtw
        import PyQt5.QtGui as qtg
        import PyQt5.QtCore as qtc

        import sys

        class Save_text_as_2(qtw.QWidget):
            def __init__(self):
                super().__init__()
                self.setWindowTitle("Сохранение текста")
                self.setLayout(qtw.QVBoxLayout())
                # self.setWindowIcon(qtg.QIcon("icon.png"))
                self.setFixedSize(400, 400)
                self.initUI()

            def initUI(self):
                self.text_about = qtw.QLabel("Введите текст")
                self.text_about.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text_about)

                self.text = qtw.QTextEdit()
                self.text.setFont(qtg.QFont("Arial", 10))
                self.layout().addWidget(self.text)

                self.save_button = qtw.QPushButton("Сохранить")
                self.save_button.clicked.connect(self.save)
                self.layout().addWidget(self.save_button)

                self.quit_button = qtw.QPushButton("Выход")
                self.quit_button.clicked.connect(self.close)
                self.layout().addWidget(self.quit_button)

            def save(self):
                try:
                    fl = qtw.QFileDialog.getSaveFileName(self, "Сохранить файл", "", "all files (*.*)")
                    with open(fl[0], "w") as f:
                        f.write(self.text.toPlainText())


                except:
                    print("Ошибка")

        app = qtw.QApplication(sys.argv)
        mw = Save_text_as_2()
        mw.show()
        sys.exit(app.exec_())

    # test_task()
    # task__1()
    task__2()
    # task__3()


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task5()
    # task4()
    pass
