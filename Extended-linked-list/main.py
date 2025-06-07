from Extended_Linked_List import ExtendedLinkedList


lista = ExtendedLinkedList(node_capacity=8)

print("--- Inserindo elementos ---")
valores_a_inserir = [3, 7, 9, 11, 18, 20, 21, 27]
for v in valores_a_inserir:
    lista.insert(v)

lista.print_list()
print(f"Total de elementos: {lista.total_elements()}\n")

print("--- Inserindo 34 para encher o primeiro nó e forçar split---")
lista.insert(34)
lista.print_list()
print(f"Total de elementos: {lista.total_elements()}\n")

print("--- Inserindo 25 , inserção normal ---")
lista.insert(25)
lista.print_list()
print(f"Total de elementos: {lista.total_elements()}\n")

print("--- Testando busca por posição (get_element_at) ---")
print(f"Elemento na posição 0: {lista.get_element_at(0)}")
print(f"Elemento na posição 7: {lista.get_element_at(7)}")
print(f"Elemento na posição 4: {lista.get_element_at(4)}")
print(f"Elemento na posição 99 (inválido): {lista.get_element_at(99)}\n")

print("--- Removendo elementos ---")
print("Removendo o valor 11:")
lista.remove(11)
lista.print_list()

print("\nRemovendo o valor 25:")
lista.remove(25)
lista.print_list()
print(f"Total de elementos: {lista.total_elements()}\n")

print("--- Esvaziando um nó para testar a remoção dele ---")
print("Removendo 18, 20, 21, 27 e 34. O segundo nó deve sumir:")
lista.remove(18)
lista.remove(20)
lista.remove(21)
lista.remove(27)
lista.remove(34)
lista.print_list()
print(f"Total de elementos: {lista.total_elements()}\n")