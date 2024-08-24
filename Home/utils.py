from PIL import Image, ImageDraw, ImageFont
import qrcode
from io import BytesIO
from django.contrib.staticfiles import finders

def make_rounded_image(image, radius):
    # Create a mask to make the image rounded
    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    rounded_image = Image.new('RGBA', image.size)
    rounded_image.paste(image, (0, 0), mask)
    return rounded_image


def Generate_id_card(Url: str,full_name: str, status: str, date_joined: str, profile_picture: object):
    template = Image.open(finders.find(r'usables/id_card.png'))
    data = Url

    # Create QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used
        box_size=10,  # controls how many pixels each box is
        border=4,  # controls how many boxes thick the border should be
    )


    qr.add_data(data)
    qr.make(fit=True)
    qr_code = qr.make_image(fill='black', back_color='white')
    qr_code = qr_code.convert("RGBA")

    datas = qr_code.getdata()

    new_data = []
    for item in datas:
        # Change all white (also shades of whites)
        # to transparent
        if item[:3] == (255, 255, 255):
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    qr_code.putdata(new_data)

    qr_code = qr_code.resize((236, 237))
    template.paste(qr_code, (179, 664), qr_code)
    Full_name = full_name
    Poppins = ImageFont.truetype(finders.find(r'usables/Poppins-Bold.ttf'), 37)
    draw = ImageDraw.Draw(template)
    Full_name_width , Full_name_height = draw.textsize(Full_name, Poppins)
    x = (591 - Full_name_width) // 2
    y = 563
    draw.text((x,y), Full_name, font=Poppins, fill='black')
    Position = status
    Montserrat = ImageFont.truetype(finders.find(r'usables/Montserrat-Regular.ttf'),25)
    Position_width , Position_height = draw.textsize(Position, Montserrat)
    x = (591 - Position_width) // 2
    y = 618
    draw.text((x,y), Position, font=Montserrat, fill='black')
    join = date_joined
    draw.text((301,932), join, font=Montserrat, fill='black')
    profile = Image.open(profile_picture)
    profile = profile.convert('RGBA')
    profile = profile.resize((310,310))
    radius = min(profile.size) // 2
    profile = make_rounded_image(profile, radius)
    template.paste(profile, (140,224), profile)
    buffer = BytesIO()
    template.save(buffer, format='png')
    buffer.seek(0)
    return buffer
