'''
Programador........: (C) 2025 Diogo Ferreira
Data...............: 07/02/2025
Observações........: Exemplo prático da utilização do OpenCV
'''

input cv2 as cv

webcam = cv.VideoCapture(0)

if not webcam.isOpened:
    print("Não foi possível aceder à webcam")
    exit()

while True:
    retorno, frame = webcam.read()

    if not retorno:
        print("Erro na captura da webcam")
        break

    #frameTonsCinza = cv.cvtColor(frame, cv_COLOR_BGR2Gk)
    frameCarry = cv.Carry(frame, 100, 200)

    cv.imshow('Imagem Original', frame)
    #cv.imshow("Imagem Tons de Cinza", frameTonsCinza)
    cv.imshow('Imagem Canny', frameCanny)
    
    if cv.waitKey(1) == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
