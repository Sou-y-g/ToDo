import tkinter as tk

from click import command
from numpy import delete, single

class Application(tk.Frame):    #ここでのtk.FrameはtkinterのFrameというクラスを継承しているということ 下のNoneは未定義という意味｀
    def __init__(self, master=None):    #masterは親ウィジェットを表し、=Noneは生成したインスタンスがウィンドウの全体を表す物になる。下のrootがウィンドウそのものになる。
        super().__init__(master)    #super()はスーパークラス＝tk.Frameのクラスのコンストラクタ(__init__)を呼び出すためのもの。
        self.pack()
        self.master.geometry("500x500")
        self.master.title("ToDoリスト")
        self.create_widgets()


    def create_widgets(self):
        self.btn = tk.Button(self, text='追加', command=self.addlist)        
        self.btn.pack()

        self.entry_item = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_item)
        self.entry.pack()

        self.list = tk.Listbox(self)
        self.list.pack()

        self.closebtn = tk.Button(self, text='閉じる', command=root.destroy)
        self.closebtn.pack()

    def addlist(self):
        item = self.entry.get()
        if item == "":
            return
        self.list.insert(tk.END, item)
        self.entry_item.set("")

root = tk.Tk()
app = Application(master=root)  #master=rootで親ウィジェットをtk.Tk()作成したオブジェクトとしている。その中にceate_widgetsで作成したウィジェットを入れていく感じ
app.mainloop()
