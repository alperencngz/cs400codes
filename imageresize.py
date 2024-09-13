from PIL import Image
import os

sourcePath = "/Users/alperencngzz/Desktop/pythonimageresize/images"
outputPath = "/Users/alperencngzz/Desktop/pythonimageresize/resizedimages"

def resize(im, size_scale):
    width, height = im.size

    new_height = int(height * size_scale)
    new_width = int(width * size_scale)
    resized_image = im.resize((new_width, new_height))
    return resized_image

files = os.listdir(sourcePath)
extensions = ["jpg", "jpeg", "png"]
for file in files:
    ext = file.split(".")[-1]
    if ext in extensions:
        im = Image.open(os.path.join(sourcePath, file))

        im_resized = resize(im, 0.7)

        filepath = os.path.join(outputPath, file)  # Save in the outputPath
        im_resized.save(filepath)
