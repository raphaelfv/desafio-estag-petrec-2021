# Desafio Petrec - Estagiário

Utilizando a linguagem de programação Python e o framework Django, criar uma aplicação web que seja capaz de receber dados tabulares no formato CSV, armazená-los no sistema de arquivos e, através deste arquivo, gerar gráficos por meio do cruzamento de propriedades numéricas.

Para a execução deste desafio, será necessário desenvolver no mínimo 04 (quatro) telas contendo as seguintes informações e funcionalidades:
* **Home** - página inicial com um pequeno texto informativo sobre o que o sistema é capaz de prover.
* **Data** - local destinado ao carregamento de arquivos no formato CSV.
* **Graph** - tela que possibilitará gerar gráficos do tipo scatter plot com os dados do arquivo carregado na tela anterior.
* **Feedback** - destinado à coleta de feedback do usuário. Nome e feedback deverão ser gravados no banco de dados.

Exemplos ilustrativos para orientar como as telas do sistema podem ser organizadas e apresentadas estão na figura anexo_a.png no repositório.

## Informações adicionais:

* A aplicação deve ser disponibilizada como um [fork](https://docs.github.com/pt/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) deste repositório. 
* As bibliotecas utilizadas devem estar registradas no arquivo requirements.txt. 
* A reprodução da aplicação deve estar descrita no arquivo README.md.

## Diferenciais, mas não obrigatório:
* Utilizar o framework Bootstrap para tornar o sistema responsivo.
* Utilizar a biblioteca Javascript D3.js para construção do gráfico.
* Prover seletores para escolher quais propriedades do CSV serão plotadas nos eixos X e Y.

O arquivo CSV para desenvolver a tarefa do desafio estará disponível no repositório. Ele terá a seguinte estrutura:

| pressure | permeability | porosity | density | type            | depth |
|----------|--------------|----------|---------|-----------------|-------|
| 2600     | 0            | 1.2      | 2.94    | Amostra Lateral | 5389  |
| 2600     | 0            | 1.2      | 2.91    | Amostra Lateral | 5390  |
| 2600     | 152          | 2.1      | 2.91    | Amostra Lateral | 5391  |

Boa sorte!
