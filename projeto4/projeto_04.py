import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(1)
rastreador_maos = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()
    cordenadas, imagem_maos = rastreador_maos.findHands(imagem)

    cv2.imshow("Projeto 4 - IA", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()

