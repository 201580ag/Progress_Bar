import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
progress = ttk.Progressbar(root, length=200, mode="determinate")
progress.pack()

for i in range(10):
    progress["value"] = (i + 1) * 10
    root.update_idletasks()
    time.sleep(0.1)

root.mainloop()