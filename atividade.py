import cv2
import numpy as np

# 1 - CAPTURA DA IMAGEM
# Dados para identificar a imagem
nome = "Seu nome"
ra = "Seu RA"

# Abre a camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao abrir a camera")
    exit()

# Captura a foto
ret, frame = cap.read()
cap.release()

if not ret:
    print("Erro ao tirar a foto")
    exit()

# Obtém as dimensões da imagem
altura = frame.shape[0]
largura = frame.shape[1]

# Cria uma copia da imagem
img = frame.copy()

# 2 - IDENTIFICACAO DA IMAGEM
# Prepara o texto
texto = f"{nome} - RA: {ra}"

# Calcula o tamanho do texto
tamanho_texto = cv2.getTextSize(
    texto,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    2
)[0]

# Define a posicao no canto superior direito
x = largura - tamanho_texto[0] - 20

# Escreve o texto na imagem
cv2.putText(
    img,
    texto,
    (x, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.7,
    (255, 255, 255),
    2
)

# Salva a imagem identificada
cv2.imwrite("selfie.jpg", img)

# 3 - MANIPULACAO DA IMAGEM
# Flip horizontal
flip_horizontal = cv2.flip(img, 1)

# Flip vertical
flip_vertical = cv2.flip(img, 0)

# Flip horizontal e vertical
flip_hv = cv2.flip(img, -1)

# 4 - MONTAGEM DAS QUATRO IMAGENS
# Redimensiona as imagens
img = cv2.resize(img, (320, 240))
flip_horizontal = cv2.resize(flip_horizontal, (320, 240))
flip_vertical = cv2.resize(flip_vertical, (320, 240))
flip_hv = cv2.resize(flip_hv, (320, 240))

# Empilha as imagens verticalmente
numpy_vertical = np.vstack((img, flip_horizontal))
numpy_vertical2 = np.vstack((flip_vertical, flip_hv))

# Junta as imagens horizontalmente
img_final = np.hstack((numpy_vertical, numpy_vertical2))

# Exibe e salva a montagem
cv2.imshow("Quatro imagens", img_final)
cv2.imwrite("quatro_imagens.jpg", img_final)

# 5 - SEPARACAO DOS CANAIS BGR
# Separa os canais
(canal_azul, canal_verde, canal_vermelho) = cv2.split(img)

# Cria uma matriz de zeros
zeros = np.zeros(img.shape[:2], dtype="uint8")

# Canal azul
merge_azul = cv2.merge([canal_azul, zeros, zeros])

# Canal verde
merge_verde = cv2.merge([zeros, canal_verde, zeros])

# Canal vermelho
merge_vermelho = cv2.merge([zeros, zeros, canal_vermelho])

# Exibe os canais
cv2.imshow("Azul", merge_azul)
cv2.imshow("Verde", merge_verde)
cv2.imshow("Vermelho", merge_vermelho)

# Salva os canais
cv2.imwrite("azul.jpg", merge_azul)
cv2.imwrite("verde.jpg", merge_verde)
cv2.imwrite("vermelho.jpg", merge_vermelho)

# 6 - CONVERSAO DE ESPACOS DE CORES
# Escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Espaco de cores HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Espaco de cores LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Exibe as imagens
cv2.imshow("GRAY", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)

# Salva as imagens
cv2.imwrite("gray.jpg", gray)
cv2.imwrite("hsv.jpg", hsv)
cv2.imwrite("lab.jpg", lab)

# 7 - FINALIZACAO
# Aguarda uma tecla e fecha as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
