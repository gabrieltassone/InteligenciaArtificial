import itertools

from simpleai.search import (CspProblem, backtrack, min_conflicts,
								MOST_CONSTRAINED_VARIABLE,
								LEAST_CONSTRAINING_VALUE,
								HIGHEST_DEGREE_VARIABLE)

vikingos = ['Agnar', 'Bjarni', 'Cnut', 'Diarf', 'Egil']
armaduras = ['Rojo', 'Azul', 'Verde', 'Blanco', 'Amarillo']
escudos = ['Trebol', 'Cruz', 'Pajaros', 'Dragon', 'Arbol']
armas = ['Martillo', 'Hacha', 'Lanza', 'Espada', 'Garrote']
amuletos = ['Pendiente', 'Anillo', 'Pulsera', 'Cinturon', 'Moneda']

variables = ['Agnar', 'Bjarni', 'Cnut', 'Diarf', 'Egil', 
				'Rojo', 'Azul', 'Verde', 'Blanco', 'Amarillo',
				'Trebol', 'Cruz', 'Pajaros', 'Dragon', 'Arbol',
				'Martillo', 'Hacha', 'Lanza', 'Espada', 'Garrote',
				'Pendiente', 'Anillo', 'Pulsera', 'Cinturon', 'Moneda']


dominios = { variable: list(range(5))
			for variable in variables}

dominios['Agnar'] = [0]
dominios['Azul'] = [1]
dominios['Pajaros'] = [2]

restricciones = []

def Restricciones_vikingos(variables, values):
	variable_1, variable_2 = variables
	posicion_1, posicion_2 = values
	if(variable_1 == 'Bjarni' and variable_2 == 'Rojo'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Rojo' and variable_2 == 'Bjarni'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Egil' and variable_2 == 'Pendiente'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Pendiente' and variable_2 == 'Egil'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Diarf' and variable_2 == 'Trebol'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Trebol' and variable_2 == 'Diarf'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Verde' and variable_2 == 'Blanco'):
		return posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Blanco' and variable_2 == 'Verde'):
		return posicion_1 == (posicion_2 + 1)
	elif(variable_1 == 'Verde' and variable_2 == 'Cruz'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Cruz' and variable_2 == 'Verde'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Martillo' and variable_2 == 'Anillo'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Anillo' and variable_2 == 'Martillo'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Amarillo' and variable_2 == 'Hacha'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Hacha' and variable_2 == 'Amarillo'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Lanza' and variable_2 == 'Pulsera'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Pulsera' and variable_2 == 'Lanza'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Cinturon' and variable_2 == 'Hacha'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Hacha' and variable_2 == 'Cinturon'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Espada' and variable_2 == 'Dragon'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Dragon' and variable_2 == 'Espada'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Cnut' and variable_2 == 'Garrote'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Garrote' and variable_2 == 'Cnut'):
		return posicion_1 == posicion_2
	elif(variable_1 == 'Lanza' and variable_2 == 'Arbol'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)
	elif(variable_1 == 'Arbol' and variable_2 == 'Lanza'):
		return posicion_1 == (posicion_2 + 1) or posicion_1 == (posicion_2 - 1)

	return True

def Variables_separadas(variables, values):
	posicion_1, posicion_2 = values
	return posicion_1 != posicion_2

for vikingo, item in itertools.combinations(variables,2):
	restricciones.append(((vikingo, item),Restricciones_vikingos))

for vikingo_1, vikingo_2 in itertools.combinations(vikingos,2):
	restricciones.append(((vikingo_1, vikingo_2), Variables_separadas))

for armadura_1, armadura_2 in itertools.combinations(armaduras,2):
	restricciones.append(((armadura_1, armadura_2), Variables_separadas))

for escudo_1, escudo_2 in itertools.combinations(escudos,2):
	restricciones.append(((escudo_1, escudo_2), Variables_separadas))

for arma_1, arma_2 in itertools.combinations(armas,2):
	restricciones.append(((arma_1, arma_2), Variables_separadas))

for amuleto_1, amuleto_2 in itertools.combinations(amuletos,2):
	restricciones.append(((amuleto_1, amuleto_2), Variables_separadas))

#problema = CspProblem(variables, dominios, restricciones)
#resultado = backtrack(problema, value_heuristic=LEAST_CONSTRAINING_VALUE, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
#resultado = min_conflicts(problema, iterations_limit=100)

#print(resultado)

def resolver(metodo_busqueda, iteraciones):
	problema = CspProblem(variables, dominios, restricciones)
	if metodo_busqueda == 'backtrack':
		resultado= backtrack(problema, value_heuristic=LEAST_CONSTRAINING_VALUE, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
		return resultado
	if metodo_busqueda == 'min_conflicts':
		resultado= min_conflicts(problema, iterations_limit=iteraciones)
		return resultado

if __name__ == '__main__':
	problema = CspProblem(variables, dominios, restricciones)
