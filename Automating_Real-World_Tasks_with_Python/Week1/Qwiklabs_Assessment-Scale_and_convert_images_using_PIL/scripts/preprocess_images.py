from PIL import Image
import os

old_folder = "../images/"
new_folder = "../icons/"

files = os.listdir(old_folder)
files = [file for file in files if not file.startswith(".")]
for file in files:
    image = Image.open(old_folder + file)
    image = image.convert('RGB').rotate(90).resize((128, 128))
    image.save(new_folder + file + ".jpeg")

files = os.listdir(new_folder)
files = [file for file in files if not file.startswith(".")]
image = Image.open(new_folder + files[0])
print((image.format, image.size))