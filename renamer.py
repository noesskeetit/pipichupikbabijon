import os
import re
import shutil
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from PIL import ImageDraw, ImageFont, Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import time



# Путь к общей папке, где находятся все папки с моделями
root_dir = "C:/Users/shura/Desktop/models"

processed_folders_file = "C:/Users/shura/PycharmProjects/telegram_bot_test/processed.txt"

# Папки, которые содержат изображения и видео
pics_dir = "Pics"
vids_dir = "Vids"

# Удаляем файлы формата .txt и .pdf and so on
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        file_path = os.path.join(dirpath, file)
        file_extension = os.path.splitext(file_path)[1]
        if file_extension.lower() in [".txt", ".pdf", ".gif", ".json", ".html", ".js", ".css"]:
            os.remove(file_path)
        if str(file) == "@nsfwcherry [TG].png" or "thumb" in str(file) or str(file) == "cherrylekz.com.JPEG":
            os.remove(file_path)

# Переименовываем файлы в каждой папке
for model_dir in os.listdir(root_dir):
    if model_dir.lower() in open(processed_folders_file, 'r')\
            .read()\
            .lower():
        print(f"Skipping directory {model_dir}, already processed")
        continue
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

            for file in tqdm(filenames):
                print(file)
                try:
                    file_path = os.path.join(dirpath, file)
                    file_extension = os.path.splitext(file_path)[1]
                    #Photos
                    if file_extension.lower() in [".jpg", ".png",".jpeg", ".bmp", ".jfif"]:
                        # Переименовываем файлы в папке Pics
                        new_file_name = f"Image uploaded by Vaso de Sangre - Join TG @vasodesangre - {pic_num}{file_extension}"
                        # Открываем изображение
                        img = Image.open(file_path)
                        # Получаем размер изображения
                        width, height = img.size
                        if width > 600 and height > 600:
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
                            # img.save(os.path.join(model_dir_path, pics_dir, new_file_name))
                            img.save(os.path.join(dirpath, new_file_name))
                            pic_num += 1
                        else:
                            img.close()
                            os.remove(file_path)
                            pic_num += 1
                    #Videos
                    elif file_extension.lower() in [".mp4", ".mov", ".m4v", ".ts", ".mkv"]:
                            if os.path.getsize(file_path) > 3145700:
                                # Переименовываем файлы в папке Vids
                                new_file_name = f"Video uploaded by Vaso de Sangre - Join TG @vasodesangre - {vid_num}{file_extension}"
                                # shutil.move(file_path, os.path.join(model_dir_path, vids_dir, new_file_name))
                                shutil.move(file_path, os.path.join(dirpath, new_file_name))
                                vid_num += 1
                            else:
                                os.remove(file_path)
                                vid_num += 1
                except OSError as o:
                    print(f"Removing file {file}, error: {o}")
                    os.remove(os.path.join(dirpath, file))
                    continue
                except TypeError as t:
                    print(f"Removing file {file}, error: {t}")
                    os.remove(os.path.join(dirpath, file))
                    continue
                except ValueError as v:
                    print(f"Removing file {file}, error: {v}")
                    os.remove(os.path.join(dirpath, file))
                    continue
                except:
                    print(f"Removing file {file}, Unexpected error")
                    os.remove(os.path.join(dirpath, file))
                    continue




    with open(processed_folders_file, 'a') as f:
        f.write(model_dir + '\n')

        # Удаляем пустые папки
        for dirpath, dirnames, filenames in os.walk(model_dir_path, topdown=False):
            for dirname in dirnames:
                folder = os.path.join(dirpath, dirname)
                if not os.listdir(folder):
                    os.rmdir(folder)

print("The renaming and watermarking process is done. Enjoy <3 :)")