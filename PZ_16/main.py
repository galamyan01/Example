import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#00BFFF', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="11.png")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить дисциплину', command=self.open_dialog, bg='#00BFFF',
                                         bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="14.png")
        btn_search = tk.Button(toolbar, text="Поиск дисциплины", command=self.open_search_dialog, bg='#00BFFF',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.RIGHT)

        self.update_img = tk.PhotoImage(file="12.png")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать дисциплину", command=self.open_update_dialog,
                                    bg='#00BFFF',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="15.png")
        btn_delete = tk.Button(toolbar, text="Убрать дисциплину", command=self.delete_records, bg='#00BFFF',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.RIGHT)

        self.refresh_img = tk.PhotoImage(file="13.png")
        btn_refresh = tk.Button(toolbar, text="Обновить дисциплины", command=self.view_records, bg='#00BFFF',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.RIGHT)

        self.tree = ttk.Treeview(self, columns=(
        'kod_disciplin', 'name_disciplin', 'specialonst', 'lekc', 'prackt', 'labarator', 'otchet'), height=15,
                                 show='headings')

        self.tree.column('kod_disciplin', width=120, anchor=tk.CENTER)
        self.tree.column('name_disciplin', width=180, anchor=tk.CENTER)
        self.tree.column('specialonst', width=140, anchor=tk.CENTER)
        self.tree.column('lekc', width=140, anchor=tk.CENTER)
        self.tree.column('prackt', width=140, anchor=tk.CENTER)
        self.tree.column('labarator', width=140, anchor=tk.CENTER)
        self.tree.column('otchet', width=140, anchor=tk.CENTER)

        self.tree.heading('kod_disciplin', text='Номер дисциплины')
        self.tree.heading('name_disciplin', text='Наименование дисциплины')
        self.tree.heading('specialonst', text='Специальность')
        self.tree.heading('lekc', text='Лекции')
        self.tree.heading('prackt', text='Практические')
        self.tree.heading('labarator', text='Лабаратоные')
        self.tree.heading('otchet', text='Форма отчетности')

        self.tree.pack()

    def records(self, kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet):
        self.db.insert_data(kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet)
        self.view_records()

    def update_record(self, kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet):
        self.db.cur.execute("""UPDATE disciplina SET kod_disciplin=?, name_disciplin=?, specialonst=?, lekc=?, prackt=?, labarator=?, otchet=? WHERE kod_disciplin=?""" ,
                            (kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet,
                             self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM disciplina""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM disciplina WHERE kod_disciplin=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, name_disciplin):
        name_disciplin = ("%" + name_disciplin + "%",)
        self.db.cur.execute("""SELECT * FROM disciplina WHERE name_disciplin LIKE ?""", name_disciplin)
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить дисциплину')
        self.geometry('400x270+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Номер дисциплины')
        label_description.place(x=25, y=25)
        self.entry_score1 = ttk.Entry(self)
        self.entry_score1.place(x=170, y=25)

        label_name = tk.Label(self, text='Наименование дисциплины')
        label_name.place(x=5, y=50)
        self.entry_name1 = ttk.Entry(self)
        self.entry_name1.place(x=170, y=50)

        label_spec = tk.Label(self, text='Специальность')
        label_spec.place(x=35, y=75)
        self.entry_name2 = ttk.Entry(self)
        self.entry_name2.place(x=170, y=75)

        label_lecs = tk.Label(self, text='Лекции (в часах)')
        label_lecs.place(x=35, y=100)
        self.entry_score2 = ttk.Entry(self)
        self.entry_score2.place(x=170, y=100)

        label_score = tk.Label(self, text='Практика (в часах)')
        label_score.place(x=35, y=125)
        self.entry_score3 = ttk.Entry(self)
        self.entry_score3.place(x=170, y=125)

        label_score = tk.Label(self, text='Лабараторные (в часах)')
        label_score.place(x=20, y=150)
        self.entry_score4 = ttk.Entry(self)
        self.entry_score4.place(x=170, y=150)

        label_otch = tk.Label(self, text='Форма отчета')
        label_otch.place(x=35, y=175)
        self.entry_name3 = ttk.Entry(self)
        self.entry_name3.place(x=170, y=175)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=210)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=210)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_score1.get(), self.entry_name1.get(),
                                                                       self.entry_name2.get(), self.entry_score2.get(),
                                                                       self.entry_score3.get(), self.entry_score4.get(),
                                                                       self.entry_name3.get()))
        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать дисциплину")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=210)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_score1.get(), self.entry_name1.get(),
                                                                       self.entry_name2.get(), self.entry_score2.get(),
                                                                       self.entry_score3.get(), self.entry_score4.get(),
                                                                       self.entry_name3.get()))
        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск дисциплины")
        self.geometry("400x140+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск дисциплин, по наименованию")
        label_search.place(x=5, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=220, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('PZ_16.db') as self.con:
            self.cur = self.con.cursor()
            #self.cur.execute("DROP TABLE IF EXISTS disciplina")
            self.cur.execute("""CREATE TABLE IF NOT EXISTS disciplina (
                kod_disciplin INTEGER PRIMARY KEY AUTOINCREMENT,
                name_disciplin TEXT NOT NULL,
                specialonst INTEGER NOT NULL DEFAULT 1,
                lekc INTEGER,
                prackt INTEGER,
                labarator INTEGER,
                otchet TEXT NOT NULL
                )""")

    def insert_data(self, kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet):
        self.cur.execute(
            """INSERT INTO disciplina(kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet) VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (kod_disciplin, name_disciplin, specialonst, lekc, prackt, labarator, otchet))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Учебный план")
    root.geometry("1000x500+300+200")
    root.resizable(False, False)
    root.mainloop()
