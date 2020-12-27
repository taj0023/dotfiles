# from PIL import Image

# img = Image.open('resources/chall7.png')

# width = 629
# height = 95

# y = 48

# for x in range(0,608,7):
#     print(chr(img.getpixel((x,y))[0]), end = '')

nlist = [105, 110, 116, 101, 103, 114, 105, 116, 121]
thenga = ''.join([chr(i) for i in nlist])
print(thenga)
#this is second part