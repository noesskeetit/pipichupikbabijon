import os
#Enter the path of directory

dir_name = "C:/Users/shura/Downloads/desiree/DSR/pics"


test = os.listdir(dir_name)
counter = 1

# for item in test:
#     if item.endswith("001.jpg") or item.endswith("002.jpg"):
#     # if "t" in str(item).lower():
#         print(item)
#         counter += 1
#         os.remove(os.path.join(dir_name, item))

# for model in test:
#     dir_name_inner = os.path.join(dir_name, model)
#     spisok = os.listdir(dir_name_inner)
#     for item_directory in spisok:
#         print(f"Переименование файла: {item_directory} в {str(model)}-{item_directory.replace('.', ' ')}")
#         os.rename(os.path.join(dir_name_inner, item_directory), os.path.join(dir_name_inner, str(str(model) + '-' + str(item_directory).replace('-', ' ').replace('.', ' ').replace('#', ' '))))


print(counter)
print("---thumb_deleting is ready---")

