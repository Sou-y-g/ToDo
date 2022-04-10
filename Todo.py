from audioop import add
import tkinter as tk
from turtle import update

from sympy import print_rcode
from yaml import compose_all


class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.grid()
        self.master.geometry('500x400')
        self.master.title('check')
        self.create_widget()

    def create_widget(self):
        self.add_btn = tk.Button(text='追加', command=self.add_key)
        self.add_btn.grid(column=4, row=0)
        
        self.entry_item = tk.StringVar()
        self.entry = tk.Entry(textvariable=self.entry_item)
        self.entry.grid(column=2, row=0)

        self.todo_list = tk.Listbox()
        self.todo_list.grid(column=3, row=2)

        self.del_btn = tk.Button(text='削除', command=self.del_key)
        self.del_btn.grid(column=3, row=3)

        self.exit_btn = tk.Button(text='閉じる', command=root.destroy)
        self.exit_btn.grid(column=3, row=4)



    def add_key(self):
        item = self.entry.get()
        if item == '':
            return

        self.todo_list.insert(tk.END, item)

        self.entry_item.set('')

    def del_key(self):
        selectindex = tk.ACTIVE
        self.todo_list.delete(selectindex)


root = tk.Tk()
app = Application(master=root)  #master=rootで親ウィジェットをtk.Tk()作成したオブジェクトとしている。その中にceate_widgetsで作成したウィジェットを入れていく感じ
app.mainloop()