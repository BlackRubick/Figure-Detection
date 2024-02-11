

import cv2

color = (0, 0, 0)
# Cargamos la figura
image = cv2.imread('Captura de pantalla 2024-02-10 a la(s) 19.25.00.png')
# Cambiamos la escala de color a imagen en escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Dibujo de los bordes detectando los cambios en los bordes
# ((image,limiteMin, limiteMax)
canny = cv2.Canny(image, 50, 100)
# Suavizar los bordes dilantándolos
canny = cv2.dilate(canny, None, iterations=2)
# Suavizar los bordes erosionándolos
canny = cv2.erode(canny, None, iterations=2)
# Se detectan los contornos haciendo conteo de los lados usando el borde externo de la imagen
# RETR_EXTERNAL, RETR_LIST, RETR_COMP y RETR_TREE
cnts, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # OpenCV 4
cv2.imshow('image', image)
cv2.waitKey(0)
# Aplicamos un for para detectar el número de lados de cada contorno
for c in cnts:
    # Se calcula un porcentaje de error en la longitud de los arcos detectados en cada grupo de contornos
    # Calculando el error sobre el perímetro de la figura
    epsilon = 0.01 * cv2.arcLength(c, True)
    # Aproximación del contorno a un polígono de contorno cerrado
    approx = cv2.approxPolyDP(c, epsilon, True)
    # Se obtiene un rectángulo que encierra al contorno detectado
    x, y, w, h = cv2.boundingRect(approx)
    # Comparación para el número de lados detectado
    if len(approx) == 3:
        cv2.putText(image, 'Triangulo', (x, y - 5), 1, 1, color, 1)
    if len(approx) == 4:
        proporcion = float(w) / h
        print('aspect_ratio= ', proporcion)
        if proporcion > 0.85 and proporcion < 1.25:
            cv2.putText(image, 'Cuadrado', (x, y - 5), 1, 1, color, 1)
        else:
            cv2.putText(image, 'Rectangulo', (x, y - 5), 1, 1, color, 1)
    if len(approx) == 5:
        #Aqui agregue para que pudiera reconocer la estrellas de 5 landos
        cv2.putText(image, 'Pentagono', (x, y - 5), 1, 1, color, 1)
    if len(approx) == 6:
        cv2.putText(image, 'Hexagono', (x, y - 5), 1, 1, color, 1)
    if len(approx) == 10:
        #Aqui agregue para que pudiera reconocer la estrella de mi imagen que tiene 10  lados
        cv2.putText(image, 'Decagono', (x, y - 5), 1, 1, color, 1)
    # Para detección de círculos se realiza mediante la definición de un circulo
    # como un polígono de muchos lados
    if len(approx) > 10:
        cv2.putText(image, 'Circulo', (x, y - 5), 1, 1, color, 1)
    cv2.drawContours(image, [approx], 0, color, 2)
    cv2.imshow('image', image)
    cv2.waitKey(0)
cv2.destroyAllWindows()
##lA VERDAD EL CODIGO QUE USTED DIO TIENE MUCHAS FIGURAS YA DETECTADAS A LO CUAL ESTUVE PROBANDO Y HACIA FALTA PARA PODER RECONCOER 5 LADOS
##OBVIAENTE HAY UN SIN FIN DE FIGUGURAS CON MUCHOS LADOS PERO SON FIGURAS QUE MI MANO NO SABE DIBUJAR ASI QUE LA DEJE CON LAS FIGURAS QUE SI PODIA DIBUJAR :)