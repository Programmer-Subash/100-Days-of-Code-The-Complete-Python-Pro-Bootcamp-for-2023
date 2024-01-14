import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

mile = tk.StringVar()
mile.set("0")

def mileToKm():
    return float(mile.get()) * 1.60934


def calculate():
    output_label["text"] = f"{mileToKm()}"


# mile textbox
mile_entry = tk.Entry(width=10, textvariable=mile)
mile_entry.grid(row=0, column=1)

# mile label
tk.Label(text="Miles", padx=10, pady=10).grid(row=0, column=2)

# equal to
tk.Label(text="is equal to", padx=10, pady=10).grid(row=1, column=0)

# output label
output_label = tk.Label(text="0",padx=10, pady=10)
output_label.grid(row=1, column=1)

# km label
tk.Label(text="Km",padx=10, pady=10).grid(row=1, column=2)

# calculator button
calculator_button = tk.Button(text="Calculate", command=calculate,padx=10, pady=10)
calculator_button.grid(row=2, column=1)
window.mainloop()
