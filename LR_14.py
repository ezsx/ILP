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
            self.text_about.grid(row=0, column=0,columnspan=2, pady=pady)

            self.text_radius = tk.Label(self, text="Введите радиус\nсферы:", font="Arial 10")
            self.text_radius.grid(row=1, column=0, pady=pady)

            self.radius = tk.Entry(self)
            self.radius.grid(row=1, column=1, pady=pady)

            self.text_rezult = tk.Label(self, text="Результат\nвычеслений:", font="Arial 10")
            self.text_rezult.grid(row=2, column=0, pady=pady)

            self.rezult = tk.Text(self, font="Arial 10", width=17, height=1)
            self.rezult.grid(row=2, column=1, pady=pady)

            self.count_button = tk.Button(self, font="Arial 10", text="  Вычислить  ", command=self.count, width=10)
            self.count_button.grid(row=3, column=0,columnspan=2, pady=pady)

            self.save = tk.Button(self, font="Arial 10", text="Сохранить как:", command=self.file_save,width=12)
            self.save.grid(row=4, column=0, pady=pady,sticky="w")

            self.save_as_combobox = ttk.Combobox(self, values=["txt", "html", "json"], width=7)
            self.save_as_combobox.grid(row=4, column=1, pady=pady,sticky="e")


        def count(self):
            if self.radius.get() != "":
                self.rezult.insert(1.0, str(4/3*3.14*int(self.radius.get())**3))
            else:
                mb.showerror("Ошибка", "Введите корректный радиус сферы!")

        def file_save(self):
            if self.rezult != None:
                f = fd.asksaveasfile(mode='w', defaultextension="."+self.save_as_combobox.get())
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


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    task5()