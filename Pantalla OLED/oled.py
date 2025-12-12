import serial
import time

# Configura el puerto (Cambia 'COM3' por el tuyo, en Mac/Linux es algo como '/dev/ttyUSB0')
puerto = 'COM6' 
baudios = 115200

try:
    esp32 = serial.Serial(puerto, baudios, timeout=1)
    time.sleep(2) # Esperar a que se estabilice la conexión
    print(f"Conectado a {puerto}. Escribe algo y presiona Enter (Escribe 'salir' para terminar):")

    while True:
        mensaje = input("Texto para OLED > ")
        
        if mensaje.lower() == 'salir':
            break
            
        # Enviar el mensaje con un salto de línea al final
        esp32.write((mensaje + '\n').encode('utf-8'))

    esp32.close()

except Exception as e:
    print(f"Error: {e}")