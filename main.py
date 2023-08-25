import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Загрузка видео с веб-камеры
cap = cv2.VideoCapture("video2.mp4")

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        # Чтение кадра из видеопотока
        ret, frame = cap.read()

        # Перевод цвета кадра из BGR в RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Обнаружение позы на кадре
        results = pose.process(image)
        # results.pose_landmarks - координаты

        # Отображение результатов на кадре
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Вывод кадра на экран
        cv2.imshow('MediaPipe Pose Detection', image)

        # Выход по нажатию клавиши 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
