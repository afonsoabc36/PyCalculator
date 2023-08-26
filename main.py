import tkinter as tk

def on_click(button):
    current_text = result_var.get()
    if button == "=":
        try:
            result = eval(current_text)
            result_var.set(result)
        except:
            result_var.set("Error")
    elif button == "C":
        result_var.set("")
    elif button == "⌫":
        result_var.set(current_text[:-1])
    else:
        result_var.set(current_text + button)

app = tk.Tk()
app.title("Calculator")

result_var = tk.StringVar()
result_var.set("")

result_label = tk.Label(app, textvariable=result_var, font=("Helvetica", 24))
result_label.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

buttons = [
    ("⌫", 1, 0), ("(", 1, 1), (")", 1, 2), ("C", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3)
]

for (button, row, col) in buttons:
    button = tk.Button(app, text=button, padx=20, pady=20, command=lambda text=button: on_click(text))
    button.grid(row=row, column=col, sticky="nsew")

for i in range(5):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
