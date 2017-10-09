from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer


#INITIAL = ((1,2,300), (2,0,300), (3,0,300), (3,3,0))

SALIDA = [3,3]


def tuple2list(t):
	return list(t)

def list2tuple(t):
	return tuple(t)

def aumentarTemperatura(state):
	for indice, artefacto in enumerate(state):
		if indice != 0:
			artefacto1 = tuple2list(artefacto)
			if [artefacto[0], artefacto[1]] != SALIDA:
				artefacto1[2] += 25
			state[indice] = artefacto1
			state[indice] = list2tuple(state[indice])
	return state

def enfriarTemperatura(state, posx, posy):
	for indice, artefacto in enumerate(state):
		if indice != 0:
			if artefacto[0] == posx and artefacto[1] == posy:
				artefacto1 = tuple2list(artefacto)
				artefacto1[2] -= 150
				state[indice] = artefacto1
				state[indice] = list2tuple(state[indice])
	return state

def artefactoQuemado(state):
	bandera = 0
	for artefacto in state:
		artefacto1 = tuple2list(artefacto)
		if artefacto1[2] > 500:
			bandera = 1
			break
	if bandera == 1:
		return True
	else:
		return False

class BomerobotProblem(SearchProblem):
	def is_goal(self, state):
		state = tuple2list(state)
		bandera = 0
		for artefacto in state:
			if bandera == 0:
				posx = artefacto[0]
				posy = artefacto[1]
				posicion = []
				posicion.append(posx)
				posicion.append(posy)
				if posicion == [3,3]:
					bandera = 0
				else:
					bandera = 1
		state = list2tuple(state)
		if bandera == 0:
			return True
		else:
			return False

	def cost(self, state1, action, state2):
		return 1

	def actions(self, state):
		state1 = tuple2list(state)
		robot = state1[0]
		posxRobot, posyRobot = robot[0], robot[1]
		acciones_disponibles = []
		posiciones = []
		posiciones.append(posxRobot)
		posiciones.append(posyRobot)
		flag = 0

		if (artefactoQuemado(state1) == False):
			for indice, artefactos in enumerate(state1):
				#Misma posicion que un artefacto, se puede mover el artefacto y el robot
				if indice == 1:
					if posiciones == [artefactos[0], artefactos[1]]:
						flag = 1
						if posxRobot > 0:
							acciones_disponibles.append("SubirArtefacto1")

						if posxRobot < 3:
							acciones_disponibles.append("BajarArtefacto1")

						if posyRobot > 0:
							acciones_disponibles.append("MoverIzquierdaArtefacto1")

						if posyRobot < 3:
							acciones_disponibles.append("MoverDerechaArtefacto1")

				elif indice == 2:
					if posiciones == [artefactos[0], artefactos[1]]:
						flag = 1
						if posxRobot > 0:
							acciones_disponibles.append("SubirArtefacto2")

						if posxRobot < 3:
							acciones_disponibles.append("BajarArtefacto2")

						if posyRobot > 0:
							acciones_disponibles.append("MoverIzquierdaArtefacto2")

						if posyRobot < 3:
							acciones_disponibles.append("MoverDerechaArtefacto2")

				elif indice == 3:
					if posiciones == [artefactos[0], artefactos[1]]:
						flag = 1
						if posxRobot > 0:
							acciones_disponibles.append("SubirArtefacto3")

						if posxRobot < 3:
							acciones_disponibles.append("BajarArtefacto3")

						if posyRobot > 0:
							acciones_disponibles.append("MoverIzquierdaArtefacto3")

						if posyRobot < 3:
							acciones_disponibles.append("MoverDerechaArtefacto3")

			if flag == 1:
				#El robot se mueve y puede enfriar porque hay un elemento en su misma posicion
				if posxRobot > 0:
					acciones_disponibles.append("Arriba")

				if posxRobot < 3:
					acciones_disponibles.append("Abajo")

				if posyRobot > 0:
					acciones_disponibles.append("Izquierda")

				if posyRobot < 3:
					acciones_disponibles.append("Derecha")

				acciones_disponibles.append("Enfriar")

			else:
				#El robot se mueve solo 
				if posxRobot > 0:
					acciones_disponibles.append("Arriba")

				if posxRobot < 3:
					acciones_disponibles.append("Abajo")

				if posyRobot > 0:
					acciones_disponibles.append("Izquierda")

				if posyRobot < 3:
					acciones_disponibles.append("Derecha")

		state1 = list2tuple(state1)
		state = state1
		return acciones_disponibles

	def result(self, state, action):
		state1 = tuple2list(state)
		robot = state1[0]
		posxRobot, posyRobot = robot[0], robot[1]
		posiciones = []
		posiciones.append(posxRobot)
		posiciones.append(posyRobot)

		if(action == "Arriba"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			robotSubir = state1[0]
			robotSubir[0] -= 1
			state1[0] = robotSubir
			state1[0] = list2tuple(state1[0])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "Abajo"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			robotBajar = state1[0]
			robotBajar[0] += 1
			state1[0] = robotBajar
			state1[0] = list2tuple(state1[0])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "Izquierda"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			robotIzquierda = state1[0]
			robotIzquierda[1] -= 1
			state1[0] = robotIzquierda
			state1[0] = list2tuple(state1[0])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "Derecha"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			robotDerecha = state1[0]
			robotDerecha[1] += 1
			state1[0] = robotDerecha
			state1[0] = list2tuple(state1[0])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "SubirArtefacto1"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[1] = tuple2list(state1[1])
			robotSubir = state1[0]
			robotSubir[0] -= 1
			artefactoSubir = state1[1]
			artefactoSubir[0] -= 1
			state1[0] = robotSubir
			state1[1] = artefactoSubir
			state1[0] = list2tuple(state1[0])
			state1[1] = list2tuple(state1[1])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "BajarArtefacto1"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[1] = tuple2list(state1[1])
			robotBajar = state1[0]
			robotBajar[0] += 1
			artefactoBajar = state1[1]
			artefactoBajar[0] += 1
			state1[0] = robotBajar
			state1[1] = artefactoBajar
			state1[0] = list2tuple(state1[0])
			state1[1] = list2tuple(state1[1])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverIzquierdaArtefacto1"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[1] = tuple2list(state1[1])
			robotIzquierda = state1[0]
			robotIzquierda[1] -= 1
			artefactoIzquierda = state1[1]
			artefactoIzquierda[1] -= 1
			state1[0] = robotIzquierda
			state1[1] = artefactoIzquierda
			state1[0] = list2tuple(state1[0])
			state1[1] = list2tuple(state1[1])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverDerechaArtefacto1"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[1] = tuple2list(state1[1])
			robotDerecha = state1[0]
			robotDerecha[1] += 1
			artefactoDerecha = state1[1]
			artefactoDerecha[1] += 1 
			state1[0] = robotDerecha
			state1[1] = artefactoDerecha
			state1[0] = list2tuple(state1[0])
			state1[1] = list2tuple(state1[1])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "SubirArtefacto2"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[2] = tuple2list(state1[2])
			robotSubir = state1[0]
			robotSubir[0] -= 1
			artefactoSubir = state1[2]
			artefactoSubir[0] -= 1
			state1[0] = robotSubir
			state1[2] = artefactoSubir
			state1[0] = list2tuple(state1[0])
			state1[2] = list2tuple(state1[2])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "BajarArtefacto2"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[2] = tuple2list(state1[2])
			robotBajar = state1[0]
			robotBajar[0] += 1
			artefactoBajar = state1[2]
			artefactoBajar[0] += 1
			state1[0] = robotBajar
			state1[2] = artefactoBajar
			state1[0] = list2tuple(state1[0])
			state1[2] = list2tuple(state1[2])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverIzquierdaArtefacto2"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[2] = tuple2list(state1[2])
			robotIzquierda = state1[0]
			robotIzquierda[1] -= 1
			artefactoIzquierda = state1[2]
			artefactoIzquierda[1] -= 1
			state1[0] = robotIzquierda
			state1[2] = artefactoIzquierda
			state1[0] = list2tuple(state1[0])
			state1[2] = list2tuple(state1[2])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverDerechaArtefacto2"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[2] = tuple2list(state1[2])
			robotDerecha = state1[0]
			robotDerecha[1] += 1
			artefactoDerecha = state1[2]
			artefactoDerecha[1] += 1 
			state1[0] = robotDerecha
			state1[2] = artefactoDerecha
			state1[0] = list2tuple(state1[0])
			state1[2] = list2tuple(state1[2])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "SubirArtefacto3"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[3] = tuple2list(state1[3])
			robotSubir = state1[0]
			robotSubir[0] -= 1
			artefactoSubir = state1[3]
			artefactoSubir[0] -= 1
			state1[0] = robotSubir
			state1[3] = artefactoSubir
			state1[0] = list2tuple(state1[0])
			state1[3] = list2tuple(state1[3])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "BajarArtefacto3"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[3] = tuple2list(state1[3])
			robotBajar = state1[0]
			robotBajar[0] += 1
			artefactoBajar = state1[3]
			artefactoBajar[0] += 1
			state1[0] = robotBajar
			state1[3] = artefactoBajar
			state1[0] = list2tuple(state1[0])
			state1[3] = list2tuple(state1[3])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverIzquierdaArtefacto3"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[3] = tuple2list(state1[3])
			robotIzquierda = state1[0]
			robotIzquierda[1] -= 1
			artefactoIzquierda = state1[3]
			artefactoIzquierda[1] -= 1
			state1[0] = robotIzquierda
			state1[3] = artefactoIzquierda
			state1[0] = list2tuple(state1[0])
			state1[3] = list2tuple(state1[3])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "MoverDerechaArtefacto3"):
			state1 = tuple2list(state)
			state1[0] = tuple2list(state[0])
			state1[3] = tuple2list(state1[3])
			robotDerecha = state1[0]
			robotDerecha[1] += 1
			artefactoDerecha = state1[3]
			artefactoDerecha[1] += 1 
			state1[0] = robotDerecha
			state1[3] = artefactoDerecha
			state1[0] = list2tuple(state1[0])
			state1[3] = list2tuple(state1[3])
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		elif(action == "Enfriar"):
			state1 = tuple2list(state)
			state1 = enfriarTemperatura(state1, posxRobot, posyRobot)
			state1 = aumentarTemperatura(state1)
			state1 = list2tuple(state1)
			state = state1

		state = list2tuple(state1)
		return state

	def heuristic(self, state):
		total=0
		state=tuple2list(state)
		for indice, artefacto in enumerate(state):
			if indice == 0:
				artefacto=tuple2list(artefacto)
				current_row, current_col = artefacto[0], artefacto[1]
				goal_row, goal_column = 3,3
				distance_robot = abs(current_row - goal_row) + abs(current_col - goal_column)
				artefacto=list2tuple(artefacto)
			else:
				artefacto=tuple2list(artefacto)
				current_row, current_col = artefacto[0], artefacto[1]
				goal_row, goal_column = 3,3
				distance = abs(current_row - goal_row) + abs(current_col - goal_column)
				total += distance
				artefacto=list2tuple(artefacto)
		state=list2tuple(state)
		return (2*total) - distance_robot

'''estado = [(3,3,0),]

nuevo_estado = ((),)

posiciones_aparatos = ((1, 2), (2, 0), (3, 0))
lista_aparatos = []

posiciones_aparatos = list(posiciones_aparatos)
for artefacto in posiciones_aparatos:
	lista_artefacto = list(artefacto)
	lista_aparatos.append(lista_artefacto)

posiciones_aparatos = tuple(posiciones_aparatos)

for aparato in lista_aparatos:
	aparato.append(300)

for aparato in lista_aparatos:
	tupla_aparato = tuple(aparato)
	estado.append(tupla_aparato)

nuevo_estado = tuple(estado)'''

def resolver(metodo_busqueda, posiciones_aparatos):
	estado = [(3,3,0),]
	nuevo_estado = ((),)
	lista_aparatos = []

	posiciones_aparatos = list(posiciones_aparatos)
	for artefacto in posiciones_aparatos:
		lista_artefacto = list(artefacto)
		lista_aparatos.append(lista_artefacto)

	posiciones_aparatos = tuple(posiciones_aparatos)

	for aparato in lista_aparatos:
		aparato.append(300)

	for aparato in lista_aparatos:
		tupla_aparato = tuple(aparato)
		estado.append(tupla_aparato)

	nuevo_estado = tuple(estado)
	problema= BomerobotProblem(nuevo_estado)

	if metodo_busqueda == 'breadth_first':
		resultado= breadth_first(problema,graph_search=True)
		return resultado
	if metodo_busqueda == 'depth_first':
		resultado= depth_first(problema,graph_search=True)
		return resultado
	if metodo_busqueda == 'greedy':
		resultado= greedy(problema,graph_search=True)
		return resultado
	if metodo_busqueda== 'astar':
		resultado= astar(problema,graph_search=True)
		return resultado

	

if __name__ == '__main__':
	problema = BomerobotProblem(nuevo_estado)

#visor=ConsoleViewer()
#visor=BaseViewer()
#visor=WebViewer()

#resultado = astar(problema,graph_search=True,viewer=visor)
#resultado = greedy(problema,graph_search=True,viewer=visor)
#resultado = depth_first(problema,graph_search=True,viewer=visor)
#resultado = breadth_first(problema,graph_search=True,viewer=visor)

'''print("Estado meta:")
print(resultado.state)
print("Camino:")
for accion, estado in resultado.path():
	print("Accion", accion)
	print("Llegue a", estado)
print(visor.stats)
print("Profundidad: ", len(resultado.path()))'''