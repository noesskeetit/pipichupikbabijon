import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def add_watermark_to_video(video_path, watermark_text):
    # Создаем объект VideoCapture и считываем первый кадр видео
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()

    # Получаем размер видео
    height, width, _ = frame.shape

    # Определяем количество кадров в первых 10 секундах видео
    fps = cap.get(cv2.CAP_PROP_FPS)
    num_frames = int(fps * 10)

    # Инициализируем переменную для хранения номера кадра
    frame_num = 0

    # Создаем объект ImageDraw и объект шрифта
    img = Image.fromarray(frame)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("MYRIADPRO-REGULAR.OTF", size=int(((height*width//1600)**0.5)))
    text_width, text_height = draw.textsize(watermark_text, font)

    # Цикл для добавления вотермарки на каждый кадр видео
    while ret:
        # Рисуем текстовую вотермарку на кадре
        x = 10
        y = height - text_height - 10
        draw.text((x, y), watermark_text, font=font, fill=(190, 190, 195, 255), outline=(0, 0, 0))

        # Сохраняем кадр с вотермаркой
        frame_with_watermark = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Записываем кадр в новый видеофайл
        if frame_num < num_frames:
            if frame_num == 0:
                # Создаем новый видеофайл и задаем параметры видео
                out_path = os.path.splitext(video_path)[0] + "_wm.mp4"
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

            out.write(frame_with_watermark)
        else:
            break

        # Считываем следующий кадр видео
        ret, frame = cap.read()
        frame_num += 1

    # Освобождаем ресурсы
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Возвращаем путь к новому видеофайлу с вотермаркой
    return out_path