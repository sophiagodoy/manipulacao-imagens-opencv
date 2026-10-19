# Processamento de Imagens com Python e OpenCV

Projeto desenvolvido para explorar conceitos fundamentais de Visão Computacional, utilizando Python e as bibliotecas OpenCV e NumPy.

A aplicação realiza a captura de imagens por câmera, identificação por texto, transformações geométricas, separação de canais de cores e conversões entre diferentes espaços de cores.

## Funcionalidades

- **Captura de imagens:** aquisição de fotografias utilizando a câmera do computador.
- **Identificação da imagem:** inserção de texto na parte superior da fotografia.
- **Manipulação de imagens:** aplicação de flip horizontal, vertical e combinado.
- **Redimensionamento:** ajuste das dimensões das imagens com `cv2.resize()`.
- **Montagem de imagens:** utilização de `np.vstack()` e `np.hstack()` para reunir quatro imagens em uma única composição.
- **Separação de canais:** geração de imagens individuais para os canais vermelho (R), verde (G) e azul (B).
- **Conversão de espaços de cores:** geração de imagens nos formatos GRAY, HSV e LAB.
- **Exportação:** salvamento automático das imagens processadas no formato JPG.

## Tecnologias utilizadas

- **Python** — linguagem de programação.
- **OpenCV (cv2)** — captura, manipulação e processamento de imagens.
- **NumPy** — operações com matrizes e montagem das imagens.

## Estrutura do projeto

```text
manipulacao-imagens-opencv/
├── processamento_imagens.py
└── README.md
```

As imagens geradas são salvas na pasta de execução do programa.

## Como executar

**1.** Instale as bibliotecas necessárias:

```bash
pip install opencv-python numpy
```

**2.** Execute o programa:

```bash
python processamento_imagens.py
```

**3.** O programa captura uma imagem pela câmera, realiza as transformações e salva os resultados automaticamente.

**Observação:** é necessário ter uma câmera disponível. Os campos de identificação no código podem ser personalizados antes da execução.

## Arquivos gerados

| Arquivo | Descrição |
|---|---|
| `selfie.jpg` | Imagem capturada com identificação |
| `quatro_imagens.jpg` | Montagem contendo quatro versões da imagem |
| `vermelho.jpg` | Canal vermelho |
| `verde.jpg` | Canal verde |
| `azul.jpg` | Canal azul |
| `gray.jpg` | Imagem em escala de cinza |
| `hsv.jpg` | Conversão para HSV |
| `lab.jpg` | Conversão para LAB |

## Objetivo

Aplicar, na prática, técnicas introdutórias de Visão Computacional, compreendendo como imagens digitais podem ser capturadas, transformadas, combinadas e representadas em diferentes canais e espaços de cores.

## Contexto acadêmico

Projeto desenvolvido como atividade prática da disciplina de Visão Computacional, com foco na aplicação dos conceitos trabalhados em aula.
