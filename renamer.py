import os
import shutil

# Путь к общей папке, где находятся все папки с моделями
root_dir = "C:/Users/shura/Desktop/test"

# Папки, которые содержат изображения и видео
pics_dir = "Pics"
vids_dir = "Vids"

# Переименовываем файлы в каждой папке
for model_dir in os.listdir(root_dir):
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
                if file_extension.lower() in [".jpg", ".png",".jpeg", ".bmp"]:
                    # Переименовываем файлы в папке Pics
                    new_file_name = f"Image uploaded by Vaso de Sangre - Join TG @vasodesangre {pic_num}{file_extension}"
                    shutil.move(file_path, os.path.join(model_dir_path, pics_dir, new_file_name))
                    pic_num += 1
                elif file_extension.lower() in [".mp4", ".mov", ".m4v", ".ts", ".gif"]:
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