import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

width = image.size[0]
height = image.size[1]

img = Image.new('RGB', (width, height + 60), (0, 0, 0))
images = []
intensity = [0.1, 0.5, 0.9]

x = 20
y = height
word_size = 50
word_css = "readonly/fanwood-webfont.ttf"
setFont = ImageFont.truetype(word_css, word_size)

for i in range(3):
    for j in range(3):
        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))
                if i == 0:
                    r = int(pixel[0] * intensity[j])
                    g = pixel[1]
                    b = pixel[2]
                    img.putpixel((x, y), (r, g, b))
                if i == 1:
                    r = pixel[0]
                    g = int(pixel[1] * intensity[j])
                    b = pixel[2]
                    img.putpixel((x, y), (r, g, b))
                if i == 2:
                    r = pixel[0]
                    g = pixel[1]
                    b = int(pixel[2] * intensity[j])
                    img.putpixel((x, y), (r, g, b))

        draw = ImageDraw.Draw(img)
        strs = "channel " + str(i) + " intensity " + str(intensity[j])
        draw.text((0, height), strs, font=setFont, fill=(255, 255, 255), direction=None)

        images.append(img)
        img = Image.new('RGB', (width, height + 60), (0, 0, 0))

# create a contact sheet from different brightnesses
first_image = images[0]
contact_sheet = PIL.Image.new(first_image.mode, (first_image.width * 3, first_image.height * 3))
x = 0
y = 0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y))
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x + first_image.width == contact_sheet.width:
        x = 0
        y = y + first_image.height
    else:
        x = x + first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width / 2), int(contact_sheet.height / 2)))
display(contact_sheet)
