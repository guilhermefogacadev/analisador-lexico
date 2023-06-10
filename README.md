# Analisador Léxico C-

Neste projeto, desenvolvemos um analisador léxico para a linguagem C- utilizando a biblioteca automata-py. O analisador léxico é uma parte importante do processo de compilação, sendo responsável por analisar o código fonte e identificar os tokens que compõem a linguagem.

## Tecnologias Utilizadas
- [Python 3.10.8]- Linguagem Base
- [Automata-py] - Framework que disponibilizou a Máquina de Moore
- [Replit] - Compilador Online.


## Instalação da biblioteca Automata-py.
Para instalar a biblioteca Automata-py, siga as etapas abaixo:
Abra um terminal e execute o seguinte comando para instalar a biblioteca automata-py usando o gerenciador de pacotes pip:

```sh
pip install automata
```
## Tokens Reconhecidos

| Lexioma | Token |
| ------ | ------ |
| if | IF |
| else |ELSE |
| int | INT|
| void | VOID |
| while |WHILE|
| return | RETURN|
| float | FLOAT|
| + | PLUS |
| - | MINUS|
| * | TIMES |
| / | DIVIDE |
| > | GREATER|
| < | LESS |
| >= | GREATER_EQUAL |
| <= | LESS_EQUAL |
| = | ATTRIBUITION |
| == | EQUALS|
| != | DIFFERENT|
| . | DOT |
| ; | SEMICOLLON |
| { | LBRACES |
| } | RBRACES |
| [ | LBRACKETS |
| ] | RBRACKETS |
| ( | LPAREN |
| ) | RPAREN |
| abcdefghijklmnopqrstuvwxyz | ID |
| 1234567890 | NUMBER |

## Funcionamento

### Todas palavras reservadas seguem a seguinte Lógica:
Com a máquina de Moore é possível encontrar o caminho de cada palavra. Quando a última letra da palavra reservada é encontrada se imprime o Token.
 - Exemplo: [IF]- Busca-se as letras 'i','f' e imprime ;
 - Porém Tokens como void, if, else, while e return podem ser acompanhados de "()", portanto se encontrado um "símbolo" ao fim da palavra, será imprimido o token+simbolo. Distinguindo assim situações específicas. 
 - Outro ponto de importância são nomes de váriaveis, incluindo a Main, que são identificadas pelo Token 'ID'.
 - Exemplo de Impressão: ``` if( ) -> IF LPAREN RPAREN ```;
 - Exemplo de Impressão: ``` int main() -> INT ID LPAREN RPAREN```;

