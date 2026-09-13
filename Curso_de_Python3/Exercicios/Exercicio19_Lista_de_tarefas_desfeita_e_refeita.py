# Criar uma lista de tarefas que o usuário pode digitar comandos, os quais poderam
# Desfazer o último item da lista e pode refazer, recolaocando o item de novo.
import os

# Criando listas.
lista_tarefas = []
lista_tarefas_backup = []
lista_comandos = ["listar", "desfazer", "refazer", "apagar chat", 
                  "apagar passado", "sair"]

# Método para desfazer e refazer lista.
def lista_no_tempo (lista_desfeita, lista_refeita):
    lista_refeita.append(lista_desfeita[-1])
    lista_desfeita.pop()

while True:
    # Interface visual.
    print("Digite um comando ou algo à adicionar a lista de tarefas.")
    print("Comandos: Listar | Desfazer | Refazer | Apagar chat | Apagar passado | Sair")
    mensagem = input("Mensagem: ")

    # Verificando o que foi digitado, se foi um comando ou uma tarefa.
    if mensagem == "":
        continue
    mensagem = mensagem.strip()
    mensagem = mensagem.lower()
    indice = -1
    for index, valor  in enumerate(lista_comandos):
        if valor == mensagem:
            indice = index
            break 
    
    #Adicionando tarefa.
    if indice == -1:
        lista_tarefas.append(mensagem)
        print("Tarefa adicionada. ")
        # Mostrando lista.
    elif indice == 0:
        print("Lista de tarefas: ")
        for valor in lista_tarefas:
            print(valor)
        # Desfazendo.
    elif indice == 1:
        if len(lista_tarefas) != 0:
            lista_no_tempo(lista_tarefas, lista_tarefas_backup)
        else:
            print("A lista está vazia.")
        # Refazendo.
    elif indice == 2:
        if len(lista_tarefas_backup) != 0:
            lista_no_tempo(lista_tarefas_backup, lista_tarefas)
        else:
            print("Não há o que refazer.")
        # Apagando terminal.
    elif indice == 3:
        os.system("cls" if os.name == "nt" else "clear")
        # Excluindo histórico.
    elif indice == 4:
        lista_tarefas_backup.clear()
        # Fechando programa.
    else:
        break

print("Fechando programa.")