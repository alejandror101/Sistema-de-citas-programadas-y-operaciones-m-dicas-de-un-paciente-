import persona

class Queue:

	'''
	/**
	 * @brief  			Inicializa o crea un objeto  lista  

	 * @param      self 		Se refiere al objeto instanciado de la función, es usado dentro 
					para crear un objeto objeto lista

	 * @return  			Devuelve un objeto de tipo lista 

	 */
	'''

	def __init__(self):
		self.objetos = list()

	'''
	/**
	 * @brief  Queue_Enqueue() 	Recibe de los argumentos elementos necesarios para un expediente
					y mediante la función alterna Paciente los inserta a una cola.

	 * @param       self 		Se refiere al objeto instanciado de Queue_Enqueue(), es usado dentro 
					para ingresar contenido o atributos de dicho objeto.

	 * @param     	apell		Recibe una cadena que contiene el apelido del paciente 

	 * @param     	nomb 		Recibe una cadena  de caracteres que especifica el nombre del paciente

	 * @param     	edad 		Parametro que contiene la edad del paciente 

	 * @param  	sang 		Recibe una cadena que contiene el tipo de sand¿gre del paciente 

	 * @return  			No devuelve ningun objeto, unicamente ingresa elementos en la cola 

	 */
	'''

	def Queue_Enqueue(self,apell,nomb,edad,sang,cons):
		self.objetos.append(persona.Paciente(apell,nomb,edad,sang,cons))


	'''
	/**
	 * @brief	Queue_Dequeue()	Retira el primer objeto o elemento que se encuentra dentro de la cola 

	 * @param       self 		Se refiere al objeto instanciado de Queue_Dequeue(), es usado dentro 
					para retirar el contenido o atributos de dicho objeto

         * @return  			Devuelve el primer objeto retirado de la cola 

		  !!

         * @return 			Una cadena que espefica que la cola se ha quedado sin elementos 

	 */
	'''

	def Queue_Dequeue(self):
		try:
			return self.objetos.pop(0)
		except:
			raise ValueError("La cola está vacía")

	'''
	/**
	 * @brief       Queue_Print()	Imprime los expedientes o objetos de tipo Paciente que se encuentran  
					dentro de la cola, con sus correspondientes datos 

	 * @param       self 		Se refiere al objeto instanciado de Queue_Print(), es usado dentro 
					para imprimir el contenido o atributos de dicho objeto

	 * @return  		        Los datos de todos los expedientes creados expresados en un cadena 

	 */
	'''

	def Queue_Print(self):
		for i in self.objetos:
			print("   ",i)

	'''
	/**
	 * @brief	Queue_IsEmpty()	Indica si la cola contiene objetos de tipo Paciente o no  

	 * @param       self 		Se refiere al objeto instanciado de Queue_IsEmpty(), es usado dentro 
					para comparar el contenido o atributos de dicho objeto

	 * @return  			Un dato del tipo Booleano, que define si se encuentra vacía o no 

	 */ 
	'''

	def Queue_IsEmpty(self):
		if len(self.objetos) == 0:
			return True
		else:
			return False

	'''
	/**
	 * @brief	Queue_Ordenar()	Ordena los objetos o elementos dentro de la cola a partir del apellido
					paterno correspondiente al Paciente

	 * @param       self 		Se refiere al objeto instanciado de Queue_Ordenar(), es usado dentro 
					para ordenar el contenido o atributos de dicho objeto

	 * @return  			No devuelve ningun tipo de dato, unicamente ordena la cola

	 */
	'''

	def Queue_Ordenar(self):
		self.objetos.sort(key=lambda paciente: paciente.apellido)

