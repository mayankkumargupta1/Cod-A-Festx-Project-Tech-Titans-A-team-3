from django.shortcuts import render, HttpResponse, redirect
from .forms import cert_verify
from .models import certificate
from PIL import Image, ImageDraw, ImageFont
import qrcode
from io import BytesIO
from django.contrib.staticfiles import finders
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def generate_certificate(Full_name, text, url, date, v_id):
    template = Image.open(finders.find('certificate.png'))
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_code = qr.make_image(fill='black', back_color='white')
    qr_code = qr_code.convert("RGB")

    # qr_code = qr_code.crop((40, 40, 290, 290))
    qr_code = qr_code.resize((217, 217))
    template.paste(qr_code, (1010, 1085, 1227, 1302))
    Font = ImageFont.truetype(finders.find('Poppins-Bold.ttf'), 120)
    draw = ImageDraw.Draw(template)

    Full_name_width, Full_name_height = draw.textsize(Full_name, Font)
    x = (2000 - Full_name_width) // 2
    y = 374
    draw.text((x, y), Full_name, font=Font, fill='black')
    Font = ImageFont.truetype(finders.find('Montserrat-Regular.ttf'), 45)
    max_width = 1480
    max_height = 250

    text_width, text_height = draw.textsize(text, font=Font)
    lines = []
    line = ""
    for word in text.split():
        if draw.textsize(line + word, font=Font)[0] <= max_width:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())
    line_height = draw.textsize("A", font=Font)[1]
    total_text_height = line_height * len(lines)

    x = (template.width - max_width) / 2
    y = (template.height - total_text_height) / 2
    for line in lines:
        line_width, _ = draw.textsize(line, font=Font)
        line_x = x + (max_width - line_width) / 2
        draw.text((line_x, y - 40), line, fill=(0, 0, 0), font=Font)
        y += line_height
    Font = ImageFont.truetype(finders.find('Montserrat-Regular.ttf'), 35)
    draw.text((1010, 1340), v_id, fill=(0, 0, 0), font=Font)
    draw.text((967, 1027), date, fill=(0, 0, 0), font=Font)
    buffer = BytesIO()
    template.save(buffer, format='png')
    buffer.seek(0)
    return buffer

@login_required
def generate(request, id):
    exists = certificate.objects.filter(pk=id).exists()
    if exists:
        c = certificate.objects.get(pk=id)
        Full_name = c.Full_name
        Description = c.Description
        Date = c.Date
        relative_Url = reverse('certificates:verify', kwargs={'id': id})
        Url = str(request.build_absolute_uri(relative_Url))
        print(Url)
        buffer = generate_certificate(
            Full_name=Full_name, text=Description, url=Url, date=str(Date), v_id=str(id)
        )

        response = HttpResponse(buffer, content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="{}.png"'.format(str(id))
        return response
    else:
        messages.success(request, 'ENTERED UID DOES NOT EXISTS')
        redirect('/')



def verify(request, id):
    context = {
        'Exist': False,
        'Name': '',
        'Description': '',
        'Date': '',
        'id': 'Does Not Exists'
    }
    if certificate.objects.filter(pk=id).exists():
        c = certificate.objects.get(pk=id)
        context['Exist'] = True
        context['Name'] = str(c.Full_name)
        context['Description'] = str(c.Description)
        context['Date'] = str(c.Date)
        context['id'] = str(c.id)
    else:
        context['Exist'] = False

    return render(request, 'verify.html', context=context)
