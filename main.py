import tools

def main():
  tam = eval(input("Indique el tamaño de la lista: "))
  inf = eval(input("el rango inferior de los valores de la lista: "))
  sup = eval(input("el rango superior de los valores de la lista: "))

  list = tools.createList(tam, inf, sup)
  print("la lista ha queado así: ", list)
  print("la suma de los elementos da: ", tools.sumList(list))
  input("digite ENTER para terminar ")


main()
