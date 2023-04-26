import os
import shutil
from PIL import Image, ImageDraw, ImageFont
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Путь к общей папке, где находятся все папки с моделями
root_dir = "C:/Users/shura/Desktop/models"

# Папки, которые содержат изображения и видео
pics_dir = "Pics"
vids_dir = "Vids"

# Удаляем файлы формата .txt и .pdf
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_extension = os.path.splitext(file_path)[1]
        if file_extension.lower() in [".txt", ".pdf", ".gif"]:
            os.remove(file_path)

# Переименовываем файлы в каждой папке
for model_dir in os.listdir(root_dir):
    print(f"Processing directory: {model_dir}")
    model_dir_path = os.path.join(root_dir, model_dir)
    if os.path.isdir(model_dir_path):
        # Создаем папки Pics и Vids, если их нет
        if not os.path.exists(os.path.join(model_dir_path, pics_dir)):
            os.mkdir(os.path.join(model_dir_path, pics_dir))
        if not os.path.exists(os.path.join(model_dir_path, vids_dir)):
            os.mkdir(os.path.join(model_dir_path, vids_dir))

        # Инициализируем переменные для хранения номеров файлов
        pic_num = 1
        vid_num = 1

        for dirpath, dirnames, filenames in os.walk(model_dir_path):
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                file_extension = os.path.splitext(file_path)[1]

                #Photos
                if file_extension.lower() in [".jpg", ".png",".jpeg", ".bmp"]:
                    # Переименовываем файлы в папке Pics
                    new_file_name = f"Image uploaded by Vaso de Sangre - Join TG @vasodesangre {pic_num}{file_extension}"
                    # Открываем изображение
                    img = Image.open(file_path)
                    # Получаем размер изображения
                    width, height = img.size
                    # Создаем объект ImageDraw и объект шрифта
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.truetype("MYRIADPRO-REGULAR.OTF", size=int(((height*width//1600)**0.5)))
                    # Вычисляем координаты для левого нижнего угла текста
                    text_width, text_height = draw.textsize("t.me/vasodesangre", font)
                    x = 10
                    y = height - text_height - 10
                    # Рисуем текстовую вотермарку в левом нижнем углу изображения
                    draw.text((x, y), "t.me/vasodesangre", font=font, fill=(190, 190, 195, 255), outline=(0, 0, 0))
                    # Сохраняем изображение с вотермаркой в папке Pics
                    # img.save(os.path.join(model_dir_path, pics_dir, new_file_name))

                    # Удаляем оригинальное изображение
                    os.remove(file_path)
                    # Сохраняем изображение с вотермаркой под тем же именем и в той же папке
                    img.save(os.path.join(model_dir_path, pics_dir, new_file_name))
                    pic_num += 1

                #Videos
                elif file_extension.lower() in [".mp4", ".mov", ".m4v", ".ts"]:
                    # Переименовываем файлы в папке Vids
                    new_file_name = f"Video uploaded by Vaso de Sangre - Join TG @vasodesangre {vid_num}{file_extension}"
                    shutil.move(file_path, os.path.join(model_dir_path, vids_dir, new_file_name))
                    vid_num += 1

        # Удаляем пустые папки
        for dirpath, dirnames, filenames in os.walk(model_dir_path, topdown=False):
            for dirname in dirnames:
                folder = os.path.join(dirpath, dirname)
                if not os.listdir(folder):
                    os.rmdir(folder)

print("The renaming process is done. Enjoy <3 :)")