# Geração de Imagens para Pintura Terapeutica

## Resumo do Projeto

Geração de imagens para pintura terapeutica a partir de imagens com diferentes propriedades recebidas pelo usuário (eg: imagens fotorealistas, selfies, quadros, pinturas, desenhos animados etc).  

## Objetivo

Livros de colorir são uma uma categoria bastante comum em livrarias e bancas e possuem como público alvo desde crianças até jovens e adultos, mas nem sempre é possível encontrar um livro cujas ilustrações sejam de nosso interesse.

Pensando nisso criamos esse projeto que permite gerar, a partir de uma imagem real de qualquer natureza, uma imagem de **pintura terapeutica** que possa ser impressa e colorida com o mapeamento de cores indicado pelo grupo.

Por fim, para garantir um resultado satisfatório do projeto e que o output possua qualidade tentaremos cumprir os seguintes requisitos:

- Limitar o número de cores a serem utilizadas, pois em um cenário real uma pessoa não teria todo o espectro de cores.
- Garantir que as áreas pintáveis foram geradas de forma razoável e de fácil interpretação.

## Imagens de Teste

Para realização dos testes utilizamos imagens com diferentes propriedades de uma base de imagens com licença copyleft: [https://unsplash.com/](https://unsplash.com/) e podem ser encontradas na pasta `images/raw/`.

Buscamos imagens com diferentes propriedades propositalmente para buscar cenários cujo tipo de imagem gerasse alguma limitação ou dificuldade adicional (TODO: ainda sendo explorado :D)

## Descrição do Pipeline de Processamento

O método final ainda está sendo pensado e estudado nos arquivos da pasta `exploratory/` mas até o momento imaginamos em algo nos seguintes passos:

- **1ª Etapa - Pré-processamento**
  - Leitura da imagem no formato `png` ou `jpg`
  - Image downsampling em caso de imagens muito grandes para no máximo (1000x1000)
  - Quantitização da imagem para B bits para remover possíveis ruídos
  - Uso ou não de alguma técnica de suavização (em estudo)
- **2ª Etapa - Segmentação da Imagem**
  - Quebra da imagem em regiões de cores similares
  - Agrupamento de regiões para diminuição do número de cores (algumas ideias de métodos:
    - Selecioanr as cores mais utilizadas via histogramas
    - Selecionar cores considerando objetos em foco (centrais)
    - Outros métodos a serem pesquisados :3
  - **3ª Etapa - Geração de Imagem Colorível**
    - A partir da imagem anterior, gerar a imagem preto e branco com as bordas das regiões coloríveis
    - Gerar uma versão colorida para preview
    - Se possível inserir os números que indicam o mapeamento cor -> região na primeira imagem.

## Participantes

Gabriel Van Loon

Giovani Decico Lucafó

Tamiris Fernandes Tinelli

Projeto para Disciplina de Processamento de Imagens (2021.1)
