# Sistema-de-citas-programadas-y-operaciones-m-dicas-de-un-paciente-
El proyecto consiste en brindar un sistema que facilite el agendamiento de citas médicas de los hospitales y consultorios, basado en estructuras de datos para poder tener un mejor manejo de los datos, evitando con su aplicación las situaciones que pueden presentarse al llevarse a cabo esta tarea como el que coincidan en un mismo horario dos citas, y haciendo que se logre poder brindar un servicio eficiente a los pacientes. 

Este programa se basa en la atención de pacientes para ello usamos clases en este caso definimos asi al paciente:

    class Paciente:
    def __init__(self,apell,nomb,edad,sang,cons):
        self.apellido = apell
        self.nombre = nomb
        self.edad = edad
        self.sangre = sang
        self.consultorio = cons
    def __str__(self):
        return "%s - %s - %i - %s - %i" % (self.apellido, self.nombre, self.edad, self.sangre, self.consultorio)
                
Para usar el programa se necesita tener instalado python3 en su computadora si usa alguna distribucuón basada en linux, en caso de usar otro sistema operativo se necesitara un IDE que acepte codigos en python.
Para ejecutar basta con tener todos los archivos .py en una misma carpeta y ejecutar Consultorio.py. persona.py y queue.py sirven como complementos del programa.
El programa esta escrito en lenguaje python y se documentó para ayudar en caso de que se requiera modificar el programa.
