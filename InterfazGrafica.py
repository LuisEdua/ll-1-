import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from AnalizadorSintactico import analizador_sintactico

def procesar():
    entrada = texto_entrada.get("1.0", tk.END)
    resultado = analizador_sintactico(entrada)
    
    texto_salida.delete("1.0", tk.END)
    texto_salida.insert(tk.END, resultado)

ventana = tk.Tk()
ventana.title("Analizador Sintactico")

ventana.geometry("800x600")

texto_entrada = ScrolledText(ventana, height=15)
texto_entrada.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

boton_procesar = tk.Button(ventana, text="Procesar", command=procesar)
boton_procesar.pack(pady=5)

texto_salida = ScrolledText(ventana, height=15)
texto_salida.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

ventana.mainloop()
