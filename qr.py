import typer
import qrcode
from pathlib import Path

app = typer.Typer()

@app.command()
def generate(
    data: str = typer.Argument(..., help="Текст или ссылка для QR-кода"),
    output: str = typer.Option("qr_code.png", "--output", "-o", help="Имя выходного файла"),
    color: str = typer.Option("black", "--color", "-c", help="Цвет точек (red, blue, green, и т.д.)"),
    bg: str = typer.Option("white", "--bg", "-b", help="Цвет фона"),
):
    """Создать QR-код с цветами"""
    
    try:
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        # Цветной QR
        img = qr.make_image(fill_color=color, back_color=bg)
        img.save(output)
        
        print(f"✅ QR-код сохранён в {output}")
        print(f"🎨 Цвет точек: {color}, фон: {bg}")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    app()