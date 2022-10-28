import random
# retorna la suma de los elementos de la lista
def sumList(list):
  sum = 0
  for i in list:
    sum += i
  return sum

#muestra el primer elemento de la lista
def showFirstPlace(list):
  return list[0]

#muestra el último elemento de la lista
def showLastPlace(list):
  return list[-1]

#suma un valor a toda la lista
def sumValAllList(list,val):
  for i in range(len(list)):
    list[i] += val

#dado un tamaño crear una lista con valores de un range
def createList(size, inf, sup):
  list = []
  for i in range(size):
    list.append(random.randint(inf,sup))
  return list
    