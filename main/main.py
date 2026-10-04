import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog

def eval_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def click(sym):
    entry.insert(tk.END, sym)

def clear():
    entry.delete(0, tk.END)

class opacityS(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.result=None
        super().__init__(parent, title = title)

    def body(self,frame):
        tk.Label(frame, text="Opacity Slider").grid(row=0)
        self.entry_value = tk.Scale(frame, from_=0, to=100, orient="horizontal")
        self.entry_value.grid(row=1, column=1)
        return self.entry_value

    def apply(self):
        self.result = self.entry_value.get()
        return self.result

def load_file():

    filename = filedialog.askopenfilename()
    if filename != "":
        f2 = open(filename, 'r')
        dat = f2.read()
        f2.close()
        notes.delete(1.0, "end-1c")
        notes.insert("end-1c", dat)

def save():
    filename = filedialog.asksaveasfilename(filetypes=(("Text Document", "*.txt"), ("All Files", "*.*")), defaultextension=".txt")
    if filename != "":
        tw = notes.get('1.0', 'end-1c')
        file = open(filename, 'w')
        file.write(tw)
        file.close()

def bl():
    root.call('set_theme', 'dark')

def li():
    root.call('set_theme', 'light')

def opa():
    dialog = opacityS(root, "Opacity Selector")
    alpha = dialog.result / 100
    if alpha <= 0.10:
        root.attributes("-alpha", 100)
        messagebox.showerror("Error", "Opacity too low.")
    else:
        root.attributes("-alpha", alpha)

def msg():
    messagebox.showinfo("HELP", "This is like a text editor and a calculator conbined write equasions and store the answers.")

root = tk.Tk()
root.geometry("1200x550")
root.title("Notecalc")
root.call('source', 'azure.tcl')
root.call('set_theme', 'dark')

menuu = tk.Menu(root)
root.configure(menu=menuu)

file_men = tk.Menu(menuu)
vis_men = tk.Menu(menuu)
he_men = tk.Menu(menuu)
menuu.add_cascade(label="Files", menu=file_men)
menuu.add_cascade(label="Windows", menu=vis_men)
menuu.add_cascade(label="Help", menu=he_men)
file_men.add_command(label="Save", command=save)
file_men.add_command(label="Load", command=load_file)
vis_men.add_command(label="Dark", command=bl)
vis_men.add_command(label="Light", command=li)
vis_men.add_command(label="Opacity", command=opa)
he_men.add_command(label="Help", command=msg)

entry = tk.Entry(root, width=40, borderwidth=5, font=("Aerial", 20), relief="solid")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0)
]

for text,row,col in buttons:
    if text == "=":
        button = tk.Button(root, text=text, command=eval_expression, width=10, height=2)
    elif text == "C":
        button = tk.Button(root, text=text, command=clear, width=10, height=2)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: click(t), width=10, height=2)

    button.grid(row=row, column=col)

notes = tk.Text(root, width=35, font=("Aerial", 20), height=16)
notes.place(x=635, y=10)

root.mainloop()
