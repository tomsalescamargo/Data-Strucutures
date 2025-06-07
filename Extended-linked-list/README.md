# Lista Encadeada Estendida em Python

## 🇧🇷 Versão em Português

### Descrição do Projeto

Este projeto é uma implementação em Python de uma **Lista Encadeada Estendida**, um Tipo Abstrato de Dado (TAD) proposto como trabalho acadêmico. Diferente de uma lista encadeada tradicional onde cada nó armazena um único elemento, esta estrutura utiliza nós que contêm um pequeno array de tamanho fixo (neste caso, com 8 posições).

A principal vantagem é a **otimização do uso de memória**, pois a proporção de ponteiros para dados é significativamente reduzida (aproximadamente 1 ponteiro para cada 8 elementos). A estrutura também implementa um mecanismo de auto-balanceamento: ao tentar inserir um elemento em um nó já cheio, o nó é dividido em dois, e metade dos seus elementos são movidos para o novo nó, mantendo a lista balanceada e eficiente para futuras inserções.

### Funcionalidades Principais

O TAD `ExtendedLinkedList` implementa as seguintes operações:

  * **`insert(value)`**: Insere um novo valor na lista, mantendo sempre a ordem crescente dos elementos. Se o nó alvo estiver cheio, ele automaticamente realiza a operação de *split* para manter o balanceamento.
  * **`remove(value)`**: Remove um valor específico da lista. Se a remoção resultar em um nó completamente vazio, o nó é removido da cadeia para evitar desperdício de espaço.
  * **`get_element_at(k)`**: Retorna o elemento que está na k-ésima posição da lista geral, navegando pelos nós e seus arrays internos para encontrar o índice correto.
  * **`total_elements()`**: Calcula e retorna a quantidade total de elementos armazenados em toda a estrutura, somando os contadores de cada nó.
  * **`print_list()`**: Uma função auxiliar para visualizar o estado atual da lista, mostrando cada nó, sua contagem de itens e os dados que ele armazena.

### Estrutura do Projeto

O código é modular e está organizado nos seguintes arquivos:

  * **`node.py`**: Contém a classe `Node`, que representa a estrutura de cada "caixinha" da lista. É responsável por gerenciar o array de dados, a contagem de elementos e o ponteiro para o próximo nó.
  * **`lista_encadeada_estendida.py`**: Contém a classe `ExtendedLinkedList`, que é a implementação principal do TAD. Ela gerencia a coleção de nós e toda a lógica de inserção, remoção, busca e balanceamento.
  * **`main.py`**: É o código de teste, responsável por instanciar a lista e executar uma série de operações para demonstrar e validar todas as funcionalidades implementadas.

### Como Executar

1.  Certifique-se de ter o **Python 3** instalado.
2.  Clone este repositório para a sua máquina local.
3.  Abra um terminal na pasta do projeto e execute o arquivo de teste com o comando:
    ```bash
    python main.py
    ```
4.  O terminal exibirá a saída de todas as operações de teste, mostrando a criação, o *split*, a inserção, a busca e a remoção de elementos.

-----

## 🇬🇧 English Version

### Project Description

This project is a Python implementation of an **Extended Linked List**, an Abstract Data Type (ADT) developed as an academic assignment. Unlike a traditional linked list where each node stores a single element, this structure uses nodes that contain a small, fixed-size array (in this case, with a capacity of 8).

The main advantage is **memory optimization**, as the pointer-to-data ratio is significantly reduced (approximately 1 pointer for every 8 elements). The structure also implements a self-balancing mechanism: when attempting to insert an element into a full node, the node is split in two, and half of its elements are moved to the new node, keeping the list balanced and efficient for future insertions.

### Core Features

The `ExtendedLinkedList` ADT implements the following operations:

  * **`insert(value)`**: Inserts a new value into the list, always maintaining the ascending order of elements. If the target node is full, it automatically performs a *split* operation to maintain balance.
  * **`remove(value)`**: Removes a specific value from the list. If this removal results in a completely empty node, the node is removed from the chain to prevent wasted space.
  * **`get_element_at(k)`**: Returns the element located at the k-th position of the overall list, navigating through the nodes and their internal arrays to find the correct index.
  * **`total_elements()`**: Calculates and returns the total number of elements stored across the entire structure by summing the counters of each node.
  * **`print_list()`**: A helper function to visualize the current state of the list, showing each node, its item count, and the data it holds.

### Project Structure

The code is modular and organized into the following files:

  * **`node.py`**: Contains the `Node` class, which represents the structure of each "box" in the list. It is responsible for managing the data array, the element count, and the pointer to the next node.
  * **`lista_encadeada_estendida.py`**: Contains the `ExtendedLinkedList` class, which is the main implementation of the ADT. It manages the collection of nodes and all the logic for insertion, removal, searching, and balancing.
  * **`main.py`**: The test script, responsible for instantiating the list and executing a series of operations to demonstrate and validate all implemented features.

### How to Run

1.  Ensure you have **Python 3** installed.
2.  Clone this repository to your local machine.
3.  Open a terminal in the project folder and run the test file with the command:
    ```bash
    python main.py
    ```
4.  The terminal will display the output of all test operations, showing the creation, splitting, insertion, searching, and removal of elements.
