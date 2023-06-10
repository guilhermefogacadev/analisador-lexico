  #Importações da maquina de Moore,Tokens,Alfabeto,Estado, Estado inicial e Transições
from automata.fa.Moore import Moore
from Classes.Fixos import tokens,alphabet,states,startState,transitions
from Classes.Tabela import output_table
from sys import argv

#Função para realizar o teste recebendo ele por parametro
def abreArquivo(caminho):
  arquivo= open(caminho,'r');
  leitura=arquivo.read()
  print(moore.get_output_from_string(leitura))
  
moore = Moore(states, alphabet, tokens, transitions, startState,output_table)

abreArquivo('prog-002.cm')
'''
if __name__ == "__main__":
    if len(argv) < 2 :
        raise IOError("Use "+ argv[0] + " file.cm")
    else :
        aux = argv[1].split('.')
        if aux[-1] != 'cm':
            raise IOError("Not a .cm file!")
        data = open(argv[1])

        source_file = data.read()

        #print("Definição da Máquina")
        #print(moore)
        print("Entrada:")
        print(source_file)

        print("Lista de Tokens:")
        print(moore.get_output_from_string(source_file))

'''















