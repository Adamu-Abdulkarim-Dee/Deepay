from django.conf import settings
from .models import Account, Withdraw
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import  string
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

def generate_account_number():
    logic = '88' + ''.join(random.choices(string.digits, k=8))
    return logic

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_account(instance, created, sender, **kwargs):
    if created:
        account_number = generate_account_number()
        account_name = instance.full_name

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(f"{account_number}")
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color='black', back_color='white')

        draw = ImageDraw.Draw(qr_img)
        text = account_number
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(text, font)
        qr_width, qr_height = qr_img.size
        text_position = (( qr_width - text_width ) // 2, ( qr_height - text_height ) // 2)
        draw.text(text_position, text, fill='black', font=font)

        img_dir = os.path.join(settings.MEDIA_ROOT, 'qrcode')
        os.makedirs(img_dir, exist_ok=True)

        img_path = os.path.join(img_dir, f'{account_number}_qrcode.png')
        qr_img.save(img_path)

        Account.objects.create(
            user=instance, account_number=account_number,
            account_name=account_name,account_status='ACTIVE', 
            account_balance=0, pin=0, qr_code=os.path.relpath(img_path, settings.MEDIA_ROOT)
        )