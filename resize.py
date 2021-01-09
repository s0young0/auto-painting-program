from PIL import Image

image = Image.open('1.png')

area = (100,100, 400, 400)
crop_image = image.crop(area)
crop_image.save('cut_image.png')