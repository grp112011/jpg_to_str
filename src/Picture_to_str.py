from PIL import Image

# Открываем изображение
b = input('Enter the way for a picture\n')
image = Image.open(b)

# Проверяем, является ли изображение в режиме RGB
if image.mode == 'RGB':
    a = int(input('Enter the width of the picture (px)\n'))
    # Получаем размеры изображения
    width, height = image.size
    for y in range(0, height, width // a):
        for x in range(0, width, width // a):
            if sum(image.getpixel((x, y))) >= 256 * 3 * (7 / 8):
                print(' ', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (6 / 8):
                print('.', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (5 / 8):
                print('-', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (4 / 8):
                print('0', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (3 / 8):
                print('+', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (2 / 8):
                print('R', end=' ')
            elif sum(image.getpixel((x, y))) >= 256 * 3 * (1 / 8):
                print('*', end=' ')
            else:
                print('@', end=' ')

        print()

while True:
    input()
