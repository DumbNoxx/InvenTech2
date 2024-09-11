import tkinter as tk

root = tk.Tk()
root.geometry()

for e, expand in enumerate([False, True]):
    for f, fill in enumerate([None, tk.X, tk.Y, tk.BOTH]):
        for s, side in enumerate([tk.TOP, tk.LEFT, tk.BOTTOM, tk.RIGHT]):
            position = '+{}+{}'.format(s * 205 + 100 + e * 820, f * 235 + 100)
            win = tk.Toplevel(root)
            win.geometry('200x200'+position)
            text = str("side='{}'\nfill='{}'\nexpand={}".format(side, fill, str(expand)))
            tk.Label(win, text=text, bg=['#FF5555', '#55FF55'][e]).pack(side=side, fill=fill, expand=expand)
                
root.mainloop()