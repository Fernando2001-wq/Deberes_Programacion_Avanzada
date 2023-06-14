class Metodos:
    def ingreso(self, lis, tam):
        i = 0
        while i < tam:
            print("Ingrese el [", i, "] valor de la lista")
            num = int(input("numero: "))
            lis.append(num)
            i = i + 1

    def impresion(self, lis, tam):
        for i in range(tam):
            print(lis[i])

metodos = Metodos()
milista = []

tam = int(input("Ingrese el tamaño de la lista: "))

while True:
    print("------- Menú -------")
    print("1. Ingresar elementos a la lista")
    print("2. Imprimir elementos de la lista")
    print("3. Extender lista")
    print("4. Contar elementos en la lista")
    print("5. Encontrar el índice de un elemento en la lista")
    print("6. Insertar elemento en la lista")
    print("7. Eliminar último elemento de la lista")
    print("8. Eliminar elemento de la lista por índice")
    print("9. Eliminar elemento de la lista por valor")
    print("10. Revertir la lista")
    print("11. Convertir lista de caracteres a cadena y revertir")
    print("12. Ordenar la lista")
    print("13. Ordenar la lista en orden inverso")
    print("14. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        metodos.ingreso(milista, tam)
        print("Elementos ingresados correctamente.")
        print()
    elif opcion == 2:
        print("Elementos de la lista:")
        metodos.impresion(milista, len(milista))
        print()
    elif opcion == 3:
        l2 = []
        tam = int(input("Ingrese la cantidad de elementos a agregar a la lista extendida: "))
        metodos.ingreso(l2, tam)
        milista.extend(l2)
        print("Lista extendida correctamente.")
        print()
    elif opcion == 4:
        elemento = int(input("Ingrese el elemento a contar: "))
        count = milista.count(elemento)
        print("Cantidad de veces que aparece el elemento en la lista:", count)
        print()
    elif opcion == 5:
        elemento = int(input("Ingrese el elemento a buscar: "))
        try:
            index = milista.index(elemento)
            print("El índice del elemento en la lista es:", index)
        except ValueError:
            print("El elemento no se encuentra en la lista.")
        print()
    elif opcion == 6:
        index = int(input("Ingrese el índice en el que desea insertar el elemento: "))
        elemento = int(input("Ingrese el elemento a insertar: "))
        milista.insert(index, elemento)
        print("Elemento insertado correctamente.")
        print()
    elif opcion == 7:
        if milista:
            elemento = milista.pop()
            print("Elemento eliminado de la lista:", elemento)
        else:
            print("La lista está vacía. No se puede eliminar ningún elemento.")
        print()
    elif opcion == 8:
        if milista:
            try:
                index = int(input("Ingrese el índice del elemento a eliminar: "))
                elemento = milista.pop(index)
                print("Elemento eliminado de la lista:", elemento)
            except IndexError:
                print("El índice está fuera de rango.")
        else:
            print("La lista está vacía. No se puede eliminar ningún elemento.")
        print()
    elif opcion == 9:
        if milista:
            elemento = int(input("Ingrese el elemento a eliminar: "))
            try:
                milista.remove(elemento)
                print("Elemento eliminado de la lista.")
            except ValueError:
                print("El elemento no se encuentra en la lista.")
        else:
            print("La lista está vacía. No se puede eliminar ningún elemento.")
        print()
    elif opcion == 10:
        milista.reverse()
        print("Lista revertida correctamente.")
        print()
    elif opcion == 11:
        lista = list("".join(map(str, milista)))
        lista.reverse()
        cadena = "".join(lista)
        print("Cadena revertida:", cadena)
        print()
    elif opcion == 12:
        milista.sort()
        print("Lista ordenada correctamente.")
        print()
    elif opcion == 13:
        milista.sort(reverse=True)
        print("Lista ordenada en orden inverso correctamente.")
        print()
    elif opcion == 14:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
        print()
