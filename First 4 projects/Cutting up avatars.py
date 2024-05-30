import os

from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "monro.jpg")

image = Image.open(image_path)
rgb_image = image.convert("RGB")

width, height = image.size

red, green, blue = rgb_image.split()

red_image = Image.new("L", rgb_image.size, color=0)
red_image.paste(red)
shifted_red = red_image.crop((50, 50, rgb_image.width, rgb_image.height)).resize(rgb_image.size)
blended_red = Image.blend(red_image, shifted_red, 0.5)

blue_image = Image.new("L", rgb_image.size, color=0)
blue_image.paste(blue)
shifted_blue = blue_image.crop((0, 0, rgb_image.width - 50, rgb_image.height)).resize(rgb_image.size)
blended_blue = Image.blend(blue_image, shifted_blue, 0.5)

green_image = Image.new("L", rgb_image.size, color=0)
green_image.paste(green)
crop_width = 50
green_cropped = green_image.crop((crop_width, 0, rgb_image.width - crop_width, rgb_image.height)).resize(rgb_image.size)

final_image = Image.merge("RGB", (blended_red, green_cropped, blended_blue))

final_image.save("final_image.jpg")
final_image.show()

final_image.thumbnail((80, 80))

avatar_image = Image.new("RGB", (80, 80), (0, 0, 0))

final_width, final_height = final_image.size
x_offset = (80 - final_width) // 2
y_offset = (80 - final_height) // 2
avatar_image.paste(final_image, (x_offset, y_offset))

avatar_image.save("image_avatar.jpg")
avatar_image.show()
