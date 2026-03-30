# QR Code Generator

Генератор QR-кодов с поддержкой цветов.

## Установка

pip install qrcode pillow typer

## Использование

python qr.py "https://github.com/fivsky"
python qr.py "Текст" --color red --bg yellow -o myqr.png

## Пример

python qr.py "https://github.com/fivsky" --color blue --bg white