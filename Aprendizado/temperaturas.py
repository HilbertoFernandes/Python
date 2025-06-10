import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        temp = float(entry_temp.get())
        if var_opcao.get() == 1:  # Celsius para Fahrenheit
            resultado = (temp * 9/5) + 32
            label_resultado.config(text=f"{temp:.2f} °C = {resultado:.2f} °F")
        else:  # Fahrenheit para Celsius
            resultado = (temp - 32) * 5/9
            label_resultado.config(text=f"{temp:.2f} °F = {resultado:.2f} °C")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

janela = tk.Tk()
janela.title("Conversor de Temperatura")

label_instrucao = tk.Label(janela, text="Digite a temperatura:")
label_instrucao.pack(pady=5)

entry_temp = tk.Entry(janela)
entry_temp.pack(pady=5)

var_opcao = tk.IntVar(value=1)
radio_c_to_f = tk.Radiobutton(janela, text="Celsius para Fahrenheit", variable=var_opcao, value=1)
radio_f_to_c = tk.Radiobutton(janela, text="Fahrenheit para Celsius", variable=var_opcao, value=2)
radio_c_to_f.pack()
radio_f_to_c.pack()

botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop()
