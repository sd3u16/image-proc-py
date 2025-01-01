from PIL import Image, ImageFilter
import os

img = Image.open('./pokedex/pikachu.jpg')

#filtered_img = img.filter(ImageFilter.BLUR)

#filtered_img = img.filter(ImageFilter.SMOOTH)

#filtered_img = img.filter(ImageFilter.SHARPEN)


filtered_img = img.convert('L')

filtered_img.save("grey.png", 'png')


image_path = os.path.abspath("grey.png")

os.system(f"google-chrome {image_path}")
