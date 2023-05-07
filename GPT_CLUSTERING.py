import cv2
import numpy as np
from sklearn.cluster import DBSCAN

# Путь к папке с фотографиями
path_to_images = 'YOUR_PATH_TO_IMAGES_HERE'

# Загружаем все изображения из папки
images = []
for filename in os.listdir(path_to_images):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        img = cv2.imread(os.path.join(path_to_images, filename))
        images.append(img)

# Преобразуем каждое изображение в вектор признаков
features = []
for img in images:
    # Преобразуем изображение в ч/б и изменяем его размер до 100x100
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (100, 100), interpolation=cv2.INTER_AREA)
    # Вычисляем гистограмму градиентов (HOG) для каждого пикселя
    hog = cv2.HOGDescriptor((100, 100), (10, 10), (5, 5), (5, 5), 9)
    hist = hog.compute(resized)
    # Добавляем вектор признаков в список
    features.append(hist.flatten())

# Применяем метод DBSCAN для кластеризации векторов признаков
dbscan = DBSCAN(eps=0.5, min_samples=2, metric='euclidean')
labels = dbscan.fit_predict(features)

# Выводим результаты кластеризации
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print('Number of clusters: {}'.format(n_clusters))
for i in range(n_clusters):
    print('Cluster {}: {}'.format(i, np.array(images)[labels == i]))