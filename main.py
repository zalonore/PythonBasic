import tools

def main():
  size = eval(input("Indiq el tamaño de la lista: "))
  inf = eval(input("el rango inferior de los valores de la lista: "))
  sup = eval(input("el rango super de los valores de la lista: "))

  list = tools.createList(size,inf,sup)
  print("la lista ha queado así: \n",list)
  print("la suma de los elementos da: \n",tools.sumList())
  input("digite ENTER para terminar ")

  


main()
