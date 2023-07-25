import requests
import ctypes

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)


#Clave Acceso de Unsplash
access_key = "FVWY9T6d-Xokif7EDM_g41tcBA-RfKG6EutVubL3YX0"
topic = "gundam" # to change the topic
url = f"https://api.unsplash.com/photos/random?client_id={access_key}&query={topic}"
response = requests.get(url)
data = response.json()
image_url = data["urls"]["full"]

# Descarga la imagen desde la URL
response = requests.get(image_url)
image_data = response.content

# URL de la imagen
# image_url = print('Ingrese url de la imagen: ') 
# image_url = input()
# Descargar imagen desde URL
# response = requests.get(image_url)
# image_data = response.content

# Guardar la imagen en el disco
image_path = "D:\Imagenes\Pictures\imagen.jpg"
with open(image_path, "wb") as f:
    f.write(image_data)

# Llamar a la función para poner la imagen como fondo de pantalla
set_wallpaper(image_path)
