# Proyecto: Conversor de Texto a Voz

Este proyecto, desarrollado por mi, permite convertir texto a voz mediante una interfaz gráfica de usuario (GUI) sencilla creada con `tkinter`. Utiliza la librería `gTTS` (Google Text-to-Speech) para generar un archivo de audio a partir del texto ingresado.

## Características

- Interfaz gráfica simple y amigable.
- Conversión de texto a voz en idioma español.
- Reproducción automática del archivo de audio generado.

## Requisitos

Para ejecutar este proyecto, necesitas:

- Python 3.x
- Librería `gTTS`

### Instalación de dependencias

Ejecuta el siguiente comando para instalar `gTTS`:

```bash
pip install gTTS
```

## Cómo ejecutar el proyecto

1. Clona el repositorio o descarga los archivos del proyecto.

   ```bash
   git clone https://github.com/Danny894/texto-a-voz.git
   ```

   O descarga manualmente el archivo principal.

2. Navega al directorio del proyecto:

   ```bash
   cd texto-a-voz
   ```

3. Ejecuta el script en tu terminal:

   ```bash
   python texto_a_voz.py
   ```

## Uso

1. Escribe el texto que deseas convertir en el cuadro de texto.
2. Haz clic en el botón **Convertir a Voz**.
3. El audio generado se reproducirá automáticamente y se guardará como `salida.mp3` en el directorio actual.

## Compatibilidad

- macOS: El comando `afplay` se utiliza para reproducir el audio.
- Windows: Puedes cambiar `os.system("afplay salida.mp3")` por `os.system("start salida.mp3")`.
- Linux: Cambia `os.system("afplay salida.mp3")` por `os.system("mpg123 salida.mp3")` o el reproductor de tu elección.

## Ejemplo de código

```python
from gtts import gTTS
import os
from tkinter import Tk, Text, Button, Label, END

def convertir_texto_a_voz():
    texto = text_area.get("1.0", END).strip()
    if texto:
        tts = gTTS(text=texto, lang='es')
        tts.save("salida.mp3")
        os.system("afplay salida.mp3")

root = Tk()
root.title("Texto a Voz")
root.geometry("500x300")

label = Label(root, text="Escribe el texto que deseas convertir a voz:")
label.pack(pady=5)

text_area = Text(root, height=10, width=50)
text_area.pack(pady=5)

boton_convertir = Button(root, text="Convertir a Voz", command=convertir_texto_a_voz)
boton_convertir.pack(pady=5)

root.mainloop()
```

## Licencia
Este proyecto es de uso libre para fines educativos o personales.

---
**Desarrollado por Danny894**.

