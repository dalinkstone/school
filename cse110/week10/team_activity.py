import tkinter as tk

window = tk.Tk()
window.title("MoneyPack")
window.resizable(width=True, height=True)

welcome_frame = tk.Frame(master=window)
entry_frame = tk.Frame(master=window)

welcome = tk.Label(master=welcome_frame, text="Welcome to MoneyPack!", foreground='green', background='black')
entry_label = tk.Label(master=entry_frame, text="Please enter an account name", fg='green', bg='black')
entry = tk.Entry(fg='green', bg='black', width=50)


entry_label.pack()
entry.pack()

account_name = entry.get()

window.mainloop()
