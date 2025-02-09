import os
from tkinter import Tk, Text, Button, Label, END
from gtts import gTTS

def convertir_texto_a_voz():
    texto = text_area.get("1.0", END).strip()
    if texto:
        tts = gTTS(text=texto, lang='es')
        tts.save("salida.mp3")
        os.system("afplay salida.mp3")  # `afplay` para macOS

# Crear ventana principal
root = Tk()
root.title("Texto a Voz")

# Asegurar colores visibles en macOS
root.configure(bg="lightgray")

# Etiqueta de descripción
label = Label(root, text="Escribe el texto que deseas convertir a voz:", bg="lightgray", fg="black")
label.pack(pady=5)

# Área de texto con colores visibles
text_area = Text(root, height=10, width=50, bg="white", fg="black", insertbackground="black")
text_area.pack(pady=5)

# Botón para ejecutar la conversión
boton_convertir = Button(root, text="Convertir a Voz", command=convertir_texto_a_voz)
boton_convertir.pack(pady=5)

# Establecer tamaño mínimo de ventana
root.geometry("500x300")
root.mainloop()

