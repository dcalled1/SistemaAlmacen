## Guía de instalación

### Hardware

#### Requisitos:

- Raspberry Pi 3 o superior.
- Tarjeta MicroSD 8 GB o más.
- Ratón y techado USB.
- Monitor HDMI.
- Sensor RFID MFRC522.

#### Instalación:

1. Instale todos los componentes con su respectivo cableado y conecte la Raspberry Pi a la energía.
2. Conecte el sensor RFID a la Raspberry de la siguiente manera:

|Pin sensor|Pin Raspberry|
|--|--|
|SDA|24|
|SCK|23|
|MOSI|19|
|MISO|21|
|GND|6|
|RST|22|
|3.3v|1|

Mapa de pines de la Raspberry Pi:
![Pines](https://docs.microsoft.com/en-us/windows/iot-core/media/pinmappingsrpi/rp2_pinout.png)

### Software

#### Requisitos:

- Sistema operativo para Raspberry Pi instalado (haga click [aquí](https://raspberryparatorpes.net/instalacion/noobs-paso-a-paso-instalar-el-sistema-operativo-en-la-raspberry-pi/) para instalar paso a paso Raspbian).
- MongoDB. Para instalarlo, junto con todas sus dependencias en Raspbian, escriba en la terminal "sudo apt-get install mongodb".
- Python 3. Para instalarlo, junto con todas sus dependencias en Raspbian, escriba en la terminal "sudo apt-get install python3". 
- Python package Index. Para instalarlo, junto con todas sus dependencias en Raspbian, escriba en la terminal "sudo apt-get install python3-pip". 
- PyMongo. Para instalarlo, junto con todas sus dependencias en Raspbian, escriba en la terminal "sudo apt-get install python3-pymongo". 
- Actualice todos sus paquete escribiendo en la terminal "sudo apt-get update".
- Active la interfaz SPI de la Raspberry Pi. Para esto, escriba en la terminal "sudo raspi-config", luego navegue con las flechas del teclado hasta llegar a Interfaces, seleccione la opción y luego navegue hasta SPI y acepte.

**Nota:** Para asegurar que los cambios hayan sido efectuados, reinicie la Raspberry y posterior mente escriba "service mongodb start" y "service mongodb status". Si el mensaje le avisa que el servicio funciona correctamente, podemos continuar.

#### Instalación:

- Clone el repositorio usando git (para instalar, ejecute "sudo apt-get git") con el siguiente comando: "git clone https://github.com/dcalled1/SistemaAlmacen.git".
- Acceda a la carpeta del repositorio escribiendo "cd SistemaAlmacen".

