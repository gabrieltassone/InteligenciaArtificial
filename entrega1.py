from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer


INITIAL = ((1,2,300), (2,0,300), (3,0,300), (3,3,0))

SALIDA = [3,3]


def tuple2list(t):
    return list(t)


def list2tuple(t):
    return tuple(t)

def aumentarTemperatura(state):
    for indice, artefacto in enumerate(state[0:3]):
        artefacto1 = tuple2list(artefacto)
        if [artefacto[0], artefacto[1]] != SALIDA:
            artefacto1[2] += 25
        state[indice] = artefacto1
        state[indice] = list2tuple(state[indice])
    return state

def enfriarTemperatura(state, posx, posy):
    for indice, artefacto in enumerate(state[0:3]):
        if artefacto[0] == posx and artefacto[1] == posy:
            artefacto1 = tuple2list(artefacto)
            artefacto1[2] -= 150
            state[indice] = artefacto1
            state[indice] = list2tuple(state[indice])
    #state = aumentarTemperatura(state)
    return state

def artefactoQuemado(state):
    bandera = 0
    for artefacto in state[0:3]:
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
        robot = state1[3]
        posxRobot, posyRobot = robot[0], robot[1]
        acciones_disponibles = []

        posiciones = []
        posiciones.append(posxRobot)
        posiciones.append(posyRobot)
        flag = 0
        #state1 = aumentarTemperatura(state1)

        if (artefactoQuemado(state1) == False):
	        for artefactos in state1[0:3]:
	            #Misma posicion que un artefacto, se puede mover el artefacto y el robot
	            if posiciones == [artefactos[0], artefactos[1]]:
	                flag = 1
	                if posxRobot > 0:
	                    acciones_disponibles.append("Arriba")
	                    acciones_disponibles.append("SubirArtefacto")

	                if posxRobot < 3:
	                    acciones_disponibles.append("Abajo")
	                    acciones_disponibles.append("BajarArtefacto")

	                if posyRobot > 0:
	                    acciones_disponibles.append("Izquierda")
	                    acciones_disponibles.append("MoverIzquierdaArtefacto")

	                if posyRobot < 3:
	                    acciones_disponibles.append("Derecha")
	                    acciones_disponibles.append("MoverDerechaArtefacto")

	                acciones_disponibles.append("Enfriar")

	        if flag == 0:
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
        robot = state1[3]
        posxRobot, posyRobot = robot[0], robot[1]
        posiciones = []
        posiciones.append(posxRobot)
        posiciones.append(posyRobot)

        if(action == "Arriba"):
            state1 = tuple2list(state)
            state1[3] = tuple2list(state[3])
            robotSubir = state1[3]
            robotSubir[0] -= 1
            state1[3] = robotSubir            
            state1[3] = list2tuple(state1[3])
            state1 = aumentarTemperatura(state1)
            state1 = list2tuple(state1)
            state = state1

        elif(action == "Abajo"):
            state1 = tuple2list(state)
            state1[3] = tuple2list(state[3])
            robotBajar = state1[3]
            robotBajar[0] += 1
            state1[3] = robotBajar            
            state1[3] = list2tuple(state1[3])
            state1 = aumentarTemperatura(state1)
            state1 = list2tuple(state1)
            state = state1

        elif(action == "Izquierda"):
            state1 = tuple2list(state)
            state1[3] = tuple2list(state[3])
            robotIzquierda = state1[3]
            robotIzquierda[1] -= 1
            state1[3] = robotIzquierda
            state1[3] = list2tuple(state1[3])
            state1 = aumentarTemperatura(state1)
            state1 = list2tuple(state1)
            state = state1

        elif(action == "Derecha"):
            state1 = tuple2list(state)
            state1[3] = tuple2list(state[3])
            robotDerecha = state1[3]
            robotDerecha[1] += 1
            state1[3] = robotDerecha
            state1[3] = list2tuple(state1[3])
            state1 = aumentarTemperatura(state1)
            state1 = list2tuple(state1)
            state = state1

        elif(action == "SubirArtefacto"):
            for indiceArtefacto, artefactos in enumerate(state1[0:3]):
                if posiciones == [artefactos[0], artefactos[1]]:
                    state1 = tuple2list(state)
                    state1[3] = tuple2list(state[3])
                    state1[indiceArtefacto] = tuple2list(state1[indiceArtefacto])
                    robotSubir = state1[3]
                    robotSubir[0] -= 1
                    artefactoSubir = state1[indiceArtefacto]
                    artefactoSubir[0] -= 1
                    state1[3] = robotSubir
                    state1[indiceArtefacto] = artefactoSubir
                    state1[3] = list2tuple(state1[3])
                    state1[indiceArtefacto] = list2tuple(state1[indiceArtefacto])
                    state1 = aumentarTemperatura(state1)
                    state1 = list2tuple(state1)
                    state = state1
                    break

        elif(action == "BajarArtefacto"):
            for indiceArtefacto, artefactos in enumerate(state1[0:3]):
                if posiciones == [artefactos[0], artefactos[1]]:
                    state1 = tuple2list(state)
                    state1[3] = tuple2list(state[3])
                    state1[indiceArtefacto] = tuple2list(state1[indiceArtefacto])
                    robotBajar = state1[3]
                    robotBajar[0] += 1
                    artefactoBajar = state1[indiceArtefacto]
                    artefactoBajar[0] += 1
                    state1[3] = robotBajar
                    state1[indiceArtefacto] = artefactoBajar
                    state1[3] = list2tuple(state1[3])
                    state1[indiceArtefacto] = list2tuple(state1[indiceArtefacto])
                    state1 = aumentarTemperatura(state1)
                    state1 = list2tuple(state1)
                    state = state1
                    break            

        elif(action == "MoverIzquierdaArtefacto"):
            for indiceArtefacto, artefactos in enumerate(state1[0:3]):
                if posiciones == [artefactos[0], artefactos[1]]:
                    state1 = tuple2list(state)
                    state1[3] = tuple2list(state[3])
                    state1[indiceArtefacto] = tuple2list(state1[indiceArtefacto])
                    robotIzquierda = state1[3]
                    robotIzquierda[1] -= 1
                    artefactoIzquierda = state1[indiceArtefacto]
                    artefactoIzquierda[1] -= 1
                    state1[3] = robotIzquierda
                    state1[indiceArtefacto] = artefactoIzquierda
                    state1[3] = list2tuple(state1[3])
                    state1[indiceArtefacto] = list2tuple(state1[indiceArtefacto])
                    state1 = aumentarTemperatura(state1)
                    state1 = list2tuple(state1)
                    state = state1
                    break            

        elif(action == "MoverDerechaArtefacto"):
            for indiceArtefacto, artefactos in enumerate(state1[0:3]):
                if posiciones == [artefactos[0], artefactos[1]]:
                    state1 = tuple2list(state)
                    state1[3] = tuple2list(state[3])
                    state1[indiceArtefacto] = tuple2list(state1[indiceArtefacto])
                    robotDerecha = state1[3]
                    robotDerecha[1] += 1
                    artefactoDerecha = state1[indiceArtefacto]
                    artefactoDerecha[1] += 1 
                    state1[3] = robotDerecha
                    state1[indiceArtefacto] = artefactoDerecha
                    state1[3] = list2tuple(state1[3])
                    state1[indiceArtefacto] = list2tuple(state1[indiceArtefacto])
                    state1 = aumentarTemperatura(state1)
                    state1 = list2tuple(state1)
                    state = state1
                    break            

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
        dentro = 0
        state=tuple2list(state)
        for artefacto in state:
            artefacto=tuple2list(artefacto)
            if [artefacto[0], artefacto[1]] != SALIDA:
            	dentro += 1
            current_row, current_col = artefacto[0], artefacto[1]
            goal_row, goal_column = 3,3
            distance = abs(current_row - goal_row) + abs(current_col - goal_column)
            total += distance
            total += dentro
            artefacto=list2tuple(artefacto)
        state=list2tuple(state)
        return total

    """def heuristic(self, state):
        total=0
        state=tuple2list(state)
        for artefacto in state:
            artefacto=tuple2list(artefacto)
            temperatura = artefacto[2]
            current_row, current_col = artefacto[0], artefacto[1]
            goal_row, goal_column = 3,3
            distance = abs(current_row - goal_row) + abs(current_col - goal_column)
            total += distance
            total += abs(temperatura)
            artefacto=list2tuple(artefacto)
        state=list2tuple(state)
        return total"""


def resolver(metodo_busqueda, posiciones_aparatos):
    problema= BomerobotProblem(INITIAL)
    visor = BaseViewer()
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
    problema = BomerobotProblem(INITIAL)

#visor=ConsoleViewer()
#visor=BaseViewer()
#visor=WebViewer()

#resultado = astar(problema,graph_search=True,viewer=visor)
#resultado = greedy(problema,graph_search=True,viewer=visor)
#resultado = depth_first(problema,graph_search=True,viewer=visor)
#resultado = breadth_first(problema,graph_search=True,viewer=visor)

"""print("Estado meta:")
print(resultado.state)
print("Camino:")
for accion, estado in resultado.path():
    print("Accion", accion)
    print("Llegue a", estado)
print(visor.stats)
print("Profundidad: ", len(resultado.path()))"""
