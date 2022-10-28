import tools

def main():
  size = eval(input("Indique el tamaño de la lista: "))
  inf = eval(input("el rango inferior de los valores de la lista: "))
  sup = eval(input("el rango superior de los valores de la lista: "))

  list = tools.createList(size,inf,sup)
  print("la lista ha queado así: \n",list)
  


main()
