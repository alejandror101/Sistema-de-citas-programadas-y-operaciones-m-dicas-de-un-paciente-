class Paciente:

	'''
	/**
	 * @brief 			Recibe de los argumentos elementos necesarios para crear un nodo "expediente"

	 * @param       self 		Se refiere al objeto instanciado de la Función, es usado dentro 
					para asignar contenido o atributos de dicho objeto.

	 * @param       apell		Recibe una cadena que contiene el apelido del paciente 

	 * @param     	nomb 		Recibe una cadena  de caracteres que especifica el nombre del paciente

	 * @param     	edad 		Parametro que contiene la edad del paciente 

	 * @param  	sang 		Recibe una cadena que contiene el tipo de sand¿gre del paciente 

	 * @param 	cons 		Recibe el número del consultorio asignado al paciente

	 * @return  			No devuelve ningun objeto, unicamente crea la plantilla del nodo 

	 */
	'''
	def __init__(self,apell,nomb,edad,sang,cons):
		self.apellido = apell
		self.nombre = nomb
		self.edad = edad
		self.sangre = sang
		self.consultorio = cons

	'''
	/**
	 * @brief			Devuelve la infomración contenida dentro de un nodo "expediente" 

	 * @param      self 		Se refiere al objeto instanciado de la clase, es usado dentro 
					para leer el contenido o atributos de dicho objeto

	 * @return  			Los datos del nodo "expediente" expresado en cadena o entero para el caso de edad y consultorio

	 *7
	'''

	def __str__(self):
		return "%s - %s - %i - %s - %i" % (self.apellido, self.nombre, self.edad, self.sangre, self.consultorio)

