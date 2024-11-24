import model
import inference_mamdani
import fuzzy_operators
import traceback

import tkinter as tk

def calculate_sum():
    try:
        if (entry1.get() == "" or entry2.get() == "" or entry3.get() == ""):
            result_label.config(text="Будь ласка, введіть валідні числа!")
            return
    
        crisp = [float(entry1.get()), float(entry2.get()), float(entry3.get())]

        inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
        result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

        result_label.config(text=f"Ціна: {int(result[0])}$ ({result[1]})")
    except ValueError as e:
        error_message = f"Сталася помилка: {str(e)}\n{traceback.format_exc()}"
        print(error_message)
        result_label.config(text="Будь ласка, введіть валідні числа!")
    except Exception as e: 
        error_message = f"Сталася помилка: {str(e)}\n{traceback.format_exc()}"
        print(error_message)


def show_graphs():
    if (entry1.get() == "" or entry2.get() == "" or entry3.get() == ""):
        result_label.config(text="Будь ласка, введіть валідні числа!")
        return

    for lv in model.input_lvs:
        fuzzy_operators.draw_lv(lv)
    fuzzy_operators.draw_lv(model.output_lv)

root = tk.Tk()
root.title("Обчислення ціни нерухомості")
root.geometry("400x300")

label1 = tk.Label(root, text="Наскільки нерухомість близька до центру (в км):")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Яка проща нерухомості (м^2):")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="Рік будівництва:")
label3.pack()

entry3 = tk.Entry(root)
entry3.pack()

calculate_button = tk.Button(root, text="Обчислити ціну", command=calculate_sum)
calculate_button.pack()

result_label = tk.Label(root, text="Ціна: ")
result_label.pack()

graph_button = tk.Button(root, text="Графіки термів", command=show_graphs)
graph_button.pack()

root.mainloop()










