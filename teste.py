from tkinter import *

from tkinter import ttk

root = Tk()

alimentosList = ttk.Treeview(root,column=('nome', 'caloria', 'total'))
alimentosList.heading("#0",text="")
alimentosList.heading("nome",text="Nome")
alimentosList.heading("caloria", text='Calorias')
alimentosList.heading("total", text='Total')

alimentosList.column("#0", width="0")
alimentosList.column("nome", width="200")
alimentosList.column("caloria", width="50")
alimentosList.column("total", width="50")
alimentosList.grid()




root.mainloop()