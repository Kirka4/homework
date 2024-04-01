import requests
from PIL import Image
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/core",
    headers={
        "authorization": f"Bearer sk-mtNWVwdAut6jw7f0BU8qSgrgXwThpecM9YUOFzQUAoVrbaCO",
        "accept": "image/*"
    },
    files={
        "none": ''
    },
    data={
        "prompt": "A majestic castle with artillery on its walls and moats all around and woods beyond",
        "output_format": "png",
    },
)

# Проверяем статус ответа
if response.status_code == 200:
    # Открываем изображение из бинарных данных
    image = Image.open(BytesIO(response.content))
    
    # Преобразуем изображение в массив NumPy для matplotlib
    image_array = np.array(image)
    
    # Выводим изображение с помощью matplotlib
    plt.imshow(image_array, cmap='gray')
    plt.axis('off')  # Отключаем оси
    plt.show()
else:
    print(f"Ошибка при загрузке изображения: {response.status_code}")

# Код вы проверить не сможете так как у меня кончились бесплатные промты, так что остается либо поверить в то что оно работает либо
# зарегаться на https://dreamstudio.ai
# Кстати, изначально когда я еще не дошел до этого варианта, а код предложенный сайтом не работал
# (он должен был в репозитории где и код создавать файл и в него пихать картинку)
# Но почему то он файл не создавал, а если я его создавал то просто ничего не делал, поэтому
# я придумал гениальную вещь - брать картику и превращать ее в asci пиксель-арт, это было забавно но все же не то что бы хотелось
# вот такой код был:
    
    # Проверяем статус ответа
# if response.status_code == 200:
#     # Создаем объект BytesIO из бинарных данных
#     image_data = BytesIO(response.content)
    
#     # Открываем изображение из BytesIO
#     image = Image.open(image_data)
    
#     # Преобразуем изображение в оттенки серого
#     image = image.convert('L')
    
#     # Уменьшаем размер изображения
#     width, height = image.size
#     aspect_ratio = height / width
#     new_width = 120
#     new_height = aspect_ratio * new_width * 0.55
#     image = image.resize((int(new_width), int(new_height)))
    
#     # Преобразуем пиксели в строки ASCII-символов
#     pixels = np.array(image)
#     chars = "@%#*+=-:. "
#     new_pixels = (pixels / 255 * (len(chars) - 1)).astype(int)
#     ascii_image = "\n".join("".join(chars[pixel] for pixel in row) for row in new_pixels)
    
#     # Выводим ASCII-арт на экран
#     print(ascii_image)
# else:
#     print(f"Ошибка при загрузке изображения: {response.status_code}")

# Потом мне пришла в голову идея просто брать картинку и по сути делать тоже самое что и изначальный код что там предлагают 
# только просто сохранять ее в репозитории с кодом
  
    # Проверяем статус ответа
# if response.status_code == 200:
#     # Открываем изображение из бинарных данных
#     image = Image.open(BytesIO(response.content))
     # Сохраняем изображение в файл
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     image_path = os.path.join(script_dir, 'received_image.webp')
#     image.save(image_path)
    
#     print(f"Изображение сохранено в: {image_path}")
# else:
#     print(f"Ошибка при загрузке изображения: {response.status_code}")

# Оно в целом хорошо работало, но все же хотелось чтобы сразу все на экран выводилось и вот так получился последний код
# Кстати, мне вот что интересно - хоть кто нибудь кроме меня сделал самую первую домашку где надо было репозиторий для домашек сделать
# и туда все домашки закидывать? Или я один такой особо одаренный который это все таки сделал и им пользовался? геморно это особенно 
# когда вот забыл какую нибудь мелочь добавить и весь репозиторий во всяких этих file modifiyed. Ну, уду думать что мне это
# хотя бы в карму зачтется чтобы не так обидно было если никто этого даже не увидит