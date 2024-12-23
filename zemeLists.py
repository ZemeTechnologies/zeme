from tkinter import *
from tkinter import messagebox

def add():
    item = entry1.get()
    if item != "":
        List.insert(END, item)
        entry1.delete(0, END)
    else:
        messagebox.showwarning(title = "WARNING", message = "You must provide an input.")

def remove():
    try:
        itemIndex = List.curselection()[0]
        List.delete(itemIndex)
    except:
        messagebox.showerror(title = "ERROR", message = "The item you want to delete hasn't been selected.")

def replace():
    item = entry2.get()
    if item != "":
        itemIndex = List.curselection()[0]
        if entry2.get() != item:
            try:
                List.delete(itemIndex)
                List.insert(END, item)
                entry2.delete(0, END)
            except:
                messagebox.showwarning(title = "WARNING", message = "The item you want to replace hasn't been selected.")
        else:
            messagebox.showwarning(title = "WARNING", message = "You must have a different item name than the old one.")
    else:
        messagebox.showwarning(title = "WARNING", message = "You must provide an input.")
def main():
    print("Hello from Zeme Technologies! zemetechnologies.github.io")
    root = Tk()
    root.resizable(False, False)
    root.title("Zeme Lists")

    global List
    List = Listbox(root, cursor = "hand2")
    List.grid(row = 0, column = 0)

    Label(root, text = "Item Name:").grid(row = 2, column = 0)
    global entry1
    entry1 = Entry(root)
    entry1.grid(row = 3, column = 0)

    Label(root, text = "New Item Name (For Replace Method):").grid(row = 5, column = 0)
    global entry2
    entry2 = Entry(root)
    entry2.grid(row = 6, column = 0)

    addButton = Button(root, text = "Add item", command = add, cursor = "circle").grid(row = 4, column = 0)
    removeButton = Button(root, text = "Remove item", command = remove, cursor = "circle").grid(row = 1, column = 0)
    replaceButton = Button(root, text = "Replace item", command = replace, cursor = "circle").grid(row = 7, column = 0)

    root.mainloop()

main()