import webcolors
from PIL import Image

image = Image.open("/Users/sainaamirimoghadam/Downloads/sinlhm.png")
newsize = (100, 100)
red_image = image.resize(newsize)


red_image_rgb = red_image.convert("RGB")
width, height = red_image_rgb.size


rowofpixel = []
pixelart2 = []
pixelart = []
colornames = []

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]



for y in range(0, height, 5):
    for x in range(0, width, 5):
        rowofpixel.append(closest_colour(red_image_rgb.getpixel((x, y))))
    pixelart2.append(tuple(rowofpixel))
    rowofpixel.clear()

for members in pixelart2:
    pixelart.append(list(members))



for n in pixelart:
    for m in n:
        if m not in colornames:
            colornames.append(m)

#print(pixelart)




def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def pixels(lst2):
    lst3 = []
    lst4 = []
    for number in lst2:
        lst4.append(number)
        if number + 1 not in lst2:
            lst3.append(tuple(lst4))
            lst4.clear()
    return lst3


def pixelrow(colorname):
    i = 0
    k = 0
    j = 0
    for row in pixelart:
        i += 1
        colorlist = duplicates(row, colorname)
        pixelcolor = pixels(colorlist)
        # print(pixelcolor)
        for items in pixelcolor:
            if len(list(items)) > 1:
                j += 1
                print('RECHTECK("r%(first)s")' % {"first": str(i) + str(j) + colorname})
                print('r%(first)s.verschiebeNach(%(second)d, %(third)d)' % {"first": str(i) + str(j) + colorname,
                                                                            "second": min(list(items)) * 5,
                                                                            "third": i * 5})
                print('r%(first)s.setzeBreite(%(second)d)' % {"first": str(i) + str(j) + colorname, "second": (max(
                    list(items)) - min(list(items)) + 1) * 5})
                print('r%(first)s.setzeHoehe(5)' % {"first": str(i) + str(j) + colorname})
                print('r%(first)s.fuellen("%(second)s")' % {"first": str(i) + str(j) + colorname, "second": colorname})

            else:
                for pixi in list(items):
                    k += 1
                    print('RECHTECK("re%(first)s")' % {"first": str(k) + colorname})
                    print('re%(first)s.verschiebeNach(%(second)d, %(third)d)' % {"first": str(k) + colorname,
                                                                                 "second": pixi * 5,
                                                                                 "third": i * 5})
                    print('re%(first)s.setzeBreite(5)' % {"first": str(k) + colorname})
                    print('re%(first)s.setzeHoehe(5)' % {"first": str(k) + colorname})
                    print('re%(first)s.fuellen("%(second)s")' % {"first": str(k) + colorname, "second": colorname})

for colors in colornames:
   print(pixelrow(colors))
