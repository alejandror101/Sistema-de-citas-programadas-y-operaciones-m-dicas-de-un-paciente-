# -*- coding: utf-8 -*-
import sys
import random
import persona
import queue

'''
/**
 * @brief	PedirDatos()	Recibe de los argumentos elementos necesarios para un expediente y asigna nuevamente los datos para poder ser usando en una función alterna.
 * @param     	apell		Recibe una cadena que contiene el apelido del paciente 

 * @param     	nomb 		Recibe una cadena  de caracteres que especifica el nombre del paciente

 * @param     	edad 		Parametro que contiene la edad del paciente 

 * @param   	sang 		Recibe una cadena que contiene el tipo de sangre del paciente 

 * @return  		        Devuelve elementos de tipo cadena 

 */
'''

def PedirDatos(apell,nomb,edad,sang):

	apell = input("Introduzca los apellidos del paciente: ")
	nomb = input("Introduzca el nombre del paciente: ")
	edad = int(input("Introduzca la edad del paciente: "))
	sang = input("Introduzca su tipo de sangre: ")

	return apell,nomb,edad,sang

'''
/**
 * @brief	   Buscar()		Dentro de un objeto lista catea o analiza si hay similitudes en un expediente
					mediante la busqueda lineal del apellido y nombre del paciente 

 * @param 	    param 		Recibe la referencia de una lista en memoria para poder ser modificada, en este 
					caso leer su contenido o atributos del objeto

 * @return  				Devuelve los datos del nodo "expediente" encotrado, expresado en cadena junto al indice
					o posición donde fue encontrado
	   !!

 * @return    				Devuelve los datos del nodo "expediente" encotrado, expresado en cadena junto al indice
					"-1" en caso de no ser encontrado el expediente
 */
'''

def Buscar(lista):

	apellbuscar = input("Introduzca los apellidos del paciente al que pertenece el expediente: ")
	nombrbuscar = input("Introduzca los nombres del paciente al que pertenece el expediente: ")
	
	apell = 'Apellido'
	nomb = 'Nombre'
	edad = 12
	sang = 'A positiva'

	indice = 0
	for i in lista:
		if (i.apellido == apellbuscar) and (i.nombre == nombrbuscar):
			apell = i.apellido
			nomb = i.nombre
			edad = i.edad
			sang = i.sangre
			break
		indice += 1

	if (i.apellido == apellbuscar) and (i.nombre == nombrbuscar):
		return apell,nomb,edad,sang,indice
	else:
		return apell,nomb,edad,sang,-1

'''
/**
 * @brief	    menu()		Imprime en pantalla todas las opciónes que dispone el Sistema de citas programadas y operaciones médicas    

 * @return  				Devuelve la opción deseada por el paciente 
	   !!

 * @return    				Davieuelve una cadena en caso de que la opción no se encuentre en lista
 */
'''

def menu():

	while 1:
		print( "\n"
				"1) Crear un nuevo expediente clinico\n"
				"2) Agendar cita medica              \n"
				"3) Modificar expediente existente   \n"
				"4) Eliminar expediente clinico      \n"
				"5) Mostrar los expedientes que hay en el sistema\n"
				"6) Mostrar los expedientes que hay en el Consultorio 1\n"
				"7) Mostrar los expedientes que hay en el consultorio 2\n"
				"8) Pasar al paciente del consultorio 1 y devolver el expediente al archivo general\n"
				"9) Pasar al paciente del consultorio 2 y devolver el expediente al archivo general\n"
				"0) Salir\n" 
				"\n "
			  )

		print("\n Porfavor ingrese el número de la opción deseada;")
		opción = int (input ("------>   "))

		if 0 <= opción and opción <= 9:
			return opción
		else: 
			print("Lo lamento , opción no reconocida :( ")

def main():

	Archivo = list()
	Consultorio1 = queue.Queue()
	Consultorio2 = queue.Queue()

	print("\n")
	print("   **************************************************\n")
	print("   *          Sistema de citas programadas y        *\n")
	print("   *               operaciones médicas de           *\n")
	print("   *                   un paciente                  *\n")
	print("   **************************************************\n\n")

	print("\n ! Bienvenido al sitema de citas médicas ¡ \n")
	
	while 1:

		op = menu()

		if op == 1:

			print("\n")
			print("   **************************************************\n")
			print("   *        Generador de expedientes clínicos       *\n")
			print("   **************************************************\n\n")

			apell = 'Apellido'
			nomb = 'Nombre'
			edad = 12
			sang = 'A positiva'

			apell,nomb,edad,sang = PedirDatos(apell,nomb,edad,sang)

			Archivo.append(persona.Paciente(apell,nomb,edad,sang,0))

			Archivo.sort(key=lambda paciente: paciente.apellido)

			print("\n")
			print("   **************************************************\n")
			print("   *       ¡¡Listo su expediente se ha creado!!     *\n")
			print("   **************************************************\n\n")


		elif op == 2:

			print("\n")
			print("   **************************************************\n")
			print("   *             Agenda de citas médicas            *\n")
			print("   **************************************************\n\n")

			if len(Archivo) > 0:
				cons = random.randint(1,2)

				apell = 'Apellido'
				nomb = 'Nombre'
				edad = 12
				sang = 'A positiva'
				indice = 0

				apell,nomb,edad,sang,indice = Buscar(Archivo)

				if indice != -1:
					if cons == 1:
						Archivo.pop(indice)
						Archivo.sort(key=lambda paciente: paciente.apellido)
						Consultorio1.Queue_Enqueue(apell,nomb,edad,sang,1)

					if cons == 2:
						Archivo.pop(indice)
						Archivo.sort(key=lambda paciente: paciente.apellido)
						Consultorio2.Queue_Enqueue(apell,nomb,edad,sang,2)

					print("\n   La asignación de su cita ha sido realizada \n")	
					print("   Su cita ha sido programada en el consultorio :",cons)
				else:
					print("No se encontró el expediente")
			else:
				print("\n   No se pudo agendar la cita debido a que la lista de expedientes esta vacía \n")


		elif op == 3:

			print("\n")
			print("   **************************************************\n")
			print("   *        Aclaraciones a expedientes clinicos     *\n")
			print("   **************************************************\n\n")

			if len(Archivo) > 0:
				apell = 'Apellido'
				nomb = 'Nombre'
				edad = 12
				sang = 'A positiva'
				indice = 0

				apell,nomb,edad,sang,indice = Buscar(Archivo)
				if indice != -1:
					Archivo.pop(indice)
					print("\n")
					print("   ***************************************************\n")
					print("   *     Ingrese los nuevos datos del expediente     *\n")
					print("   ***************************************************\n\n")
					apell,nomb,edad,sang = PedirDatos(apell,nomb,edad,sang)
					Archivo.append(persona.Paciente(apell,nomb,edad,sang,0))
					Archivo.sort(key=lambda paciente: paciente.apellido)
				else:
					print("No se encontró el expediente")
			else:
				print("\n")
				print("   **************************************************\n")
				print("   *       La lista de expedientes esta vacia       *\n")
				print("   **************************************************\n\n")

			print("\n")
			print("   **************************************************\n")
			print("   *    ¡¡Listo sus datos han sido actualizados!!   *\n")
			print("   **************************************************\n\n")


		elif op == 4:

			print("\n")
			print("   ****************************************************\n")
			print("   *            Eliminacion de expedientes            *\n")
			print("   **************************************************\n\n")

			if len(Archivo) > 0:
				apell = 'Apellido'
				nomb = 'Nombre'
				edad = 12
				sang = 'A positiva'
				indice = 0

				apell,nomb,edad,sang,indice = Buscar(Archivo)
				if indice != -1:
					Archivo.pop(indice)

					print("\n")
					print("   ***************************************************\n")
					print("   *   ¡¡ Listo el expediente ha sido eliminado !!   *\n")
					print("   ***************************************************\n\n")

				else:
					print("No se encontró el expediente")

			else:
				print("\n")
				print("   ***********************************************************\n")
				print("   *                 No hay nada que eliminar                *\n")
				print("   ***********************************************************\n\n")


		elif op == 5:

			if len(Archivo) > 0:

				print("\n")
				print("   *************************************************************\n")
				print("   *           Estos son los expedientes archivados            *\n")
				print("   *   Estan los expedientes mostrados de la siguiente forma   *\n")
				print("   * Apellidos - Nombres - Edad - Tipo de sangre - Consultorio *\n")
				print("   *************************************************************\n\n")

				for i in Archivo:
					print("   ",i )

				print("\n")
				print("   **************************************************\n")
				print("   *               Gracias por esperar              *\n")
				print("   **************************************************\n\n")

			else:

				print("\n")
				print("   *************************************************************\n")
				print("   *              No hay expedientes archivados                *\n")
				print("   *************************************************************\n\n")


		elif op == 6:

			if Consultorio1.Queue_IsEmpty() != True:

				print("\n")
				print("   *************************************************************\n")
				print("   *   Estos son los expedientes que hay en el consultorio 1   *\n")
				print("   *   Estan los expedientes mostrados de la siguiente forma   *\n")
				print("   * Apellidos - Nombres - Edad - Tipo de sangre - Consultorio *\n")
				print("   *************************************************************\n\n")
				Consultorio1.Queue_Print()

				print("\n")
				print("   **************************************************\n")
				print("   *               Gracias por esperar              *\n")
				print("   **************************************************\n\n")
			else:
				print("\n")
				print("   *************************************************************\n")
				print("   *           No hay expedientes en el consultorio 1          *\n")
				print("   *************************************************************\n\n")


		elif op == 7:

			if Consultorio2.Queue_IsEmpty() != True:

				print("\n")
				print("   *************************************************************\n")
				print("   *   Estos son los expedientes que hay en el consultorio 2   *\n")
				print("   *   Estan los expedientes mostrados de la siguiente forma   *\n")
				print("   * Apellidos - Nombres - Edad - Tipo de sangre - Consultorio *\n")
				print("   *************************************************************\n\n")
				Consultorio2.Queue_Print()

				print("\n")
				print("   **************************************************\n")
				print("   *               Gracias por esperar              *\n")
				print("   **************************************************\n\n")

			else:

				print("\n")
				print("   *************************************************************\n")
				print("   *           No hay expedientes en el consultorio 2          *\n")
				print("   *************************************************************\n\n")


		elif op == 8:

			if Consultorio1.Queue_IsEmpty() != True:

				apell = 'Apellido'
				nomb = 'Nombre'
				edad = 12
				sang = 'A positiva'
				indice = 0

				for i in Consultorio1.objetos:
					apell = i.apellido
					nomb = i.nombre
					edad = i.edad
					sang = i.sangre
					Consultorio1.Queue_Dequeue()
					Archivo.append(persona.Paciente(apell,nomb,edad,sang,0))

				Archivo.sort(key=lambda paciente: paciente.apellido)

				print("\n")
				print("   **************************************************\n")
				print("   *                Operación exitosa               *\n")
				print("   *               Gracias por esperar              *\n")
				print("   **************************************************\n\n")

			else:

				print("\n")
				print("   **************************************************\n")
				print("   *           El consultorio 1 esta vacio          *\n")
				print("   **************************************************\n\n")


		elif op == 9:

			if Consultorio2.Queue_IsEmpty() != True:

				apell = 'Apellido'
				nomb = 'Nombre'
				edad = 12
				sang = 'A positiva'
				indice = 0

				for i in Consultorio2.objetos:
					apell = i.apellido
					nomb = i.nombre
					edad = i.edad
					sang = i.sangre
					Consultorio2.Queue_Dequeue()
					Archivo.append(persona.Paciente(apell,nomb,edad,sang,0))

				Archivo.sort(key=lambda paciente: paciente.apellido)

				print("\n")
				print("   **************************************************\n")
				print("   *                Operación exitosa               *\n")
				print("   *               Gracias por esperar              *\n")
				print("   **************************************************\n\n")

			else:

				print("\n")
				print("   **************************************************\n")
				print("   *           El consultorio 2 esta vacio          *\n")
				print("   **************************************************\n\n")


		elif op == 0: 

			print("\n")
			print("   *************************************************************\n")
			print("   *                                                           * \n")
			print("   * ¡¡ Muchas gracias por usar el Sistema de citas medicas !! *\n")
			print("   *                                                           * \n")
			print("   *************************************************************\n\n")

			sys.exit()

		else:
			print( "Lo siento, opción no reconocida :( \n");

if __name__ == '__main__':
	main()

