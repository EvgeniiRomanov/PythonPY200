from PIL import Image, ImageDraw

# Пустой желтый фон.
im = Image.new('RGB', (500, 500), (250, 250, 50))
draw = ImageDraw.Draw(im)

# Три черные линии в шириной в 1 пиксель.
draw.line(
    xy=(
        (50, 300),
        (50 + 150, 300),
        #(80, 50)
    ), fill='black')

# Три красные линии с размером в 5 пикселей.
# draw.line(
#     xy=(
#         (80, 200),
#         (180, 100),
#         (130, 50)
#     ), fill='red', width=10)

# Имея три точки и связь между ними, у нас получится синий триугольник.
# draw.polygon(
#     xy=(
#         (50, 350),
#         (130, 130),
#         (200, 200),
#         (250, 150),
#
#     ), fill='blue', outline=(25, 25, 25)
# )
# #
# Рисуем три точки.
draw.point(
    xy=(
        (350, 200),
        (450, 100),
        (400, 50)
    ), fill='black'
)

im.show()
#im.save('draw-dots.jpg', quality=95)