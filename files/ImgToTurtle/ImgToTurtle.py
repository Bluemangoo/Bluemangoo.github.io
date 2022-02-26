from PIL import Image

f = open('test.py', 'w')

filename = input("请输入图片的文件名（包含扩展名）：\n")
colorFormat = -1
if filename[-3:] == "png":
    colorFormat -= 5
im = Image.open(filename)
x, y = im.size
print(x, y)

f.write("import turtle as t\n\n")
f.write("canvasX = {}\n".format(x))
f.write("canvasY = {}\n".format(y))

f.write(
    '''

def d(x, y):
    return x - canvasX // 2, - y + canvasY // 2


t.screensize(canvasX, canvasY, "white")
t.penup()
t.goto(d(0, 0))
t.pendown()
t.pensize(1)
t.speed(0)
t.colormode(255)
t.delay(0)
t.tracer({}, 0)
t.hideturtle()
'''.format(x))

for y in range(im.size[1]):
    f.write("t.penup()\n")
    f.write("t.goto(d(0, {}))\n".format(y))
    f.write("t.pendown()\n")
    n = 0
    for x in range(im.size[0] - 1):
        pix = im.getpixel((x, y))
        n += 1
        if x == im.size[0] - 1 or str(im.getpixel((x, y))) != str(im.getpixel((x + 1, y))):
            f.write("t.pencolor" + str(pix)[:colorFormat] + ")" + "\n")
            f.write("t.forward(" + str(n) + ")\n")
            n = 0
f.write("t.done()\n")
