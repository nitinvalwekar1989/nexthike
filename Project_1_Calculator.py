import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg="#2C3E50")  # Dark background

entry = tk.Entry(root, font=("Arial", 20), borderwidth=15, relief=tk.RIDGE, bg="gray", fg="black")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ("7", "lightblue"), ("8","lightblue"), ("9","lightblue"), ("+", "silver"),
    ("4", "lightblue"), ("5", "lightblue"), ("6", "lightblue"), ("-", "silver"),
    ("1", "lightblue"), ("2", "lightblue"), ("3", "lightblue"), ("*", "silver"),
    ("C", "#F1C40F"), ("0", "#3498DB"), ("=", "#2ECC71"), ("/", "silver")
]

for i, (text, color) in enumerate(buttons):
    btn = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2, bg=color, fg="darkblue")
    btn.grid(row=(i//4)+1, column=i%4)
    btn.bind("<Button-1>", on_click)

root.mainloop()