from Mandlebrot import MandelbrotSet
from PIL import Image
from Viewport import Viewport
from PIL.ImageColor import getrgb

# -0.7435 + 0.1314j

def paint(mandelbrot_set, viewport, palette, smooth):
    for pixel in viewport:
        stability = mandelbrot_set.stability(complex(pixel), smooth)
        index = int(min(stability * len(palette), len(palette) - 1))
        pixel.color = palette[index % len(palette)]

def denormalize(palette):
    return [
        tuple(int(channel * 255) for channel in color)
        for color in palette
    ]

def hsb(hue_degrees: int, saturation: float, brightness: float):
    return getrgb(
        f"hsv({hue_degrees % 360},"
        f"{saturation * 100}%,"
        f"{brightness * 100}%)"
    )

hsb(180, 1, 1)

image = Image.new(mode="RGB", size=(1024, 1024))
mandelbrot_set = MandelbrotSet(max_iterations=30, escape_radius=1000)
for pixel in Viewport(image, center=-0.75, width=3.5):
    stability = mandelbrot_set.stability(complex(pixel), smooth=True)
    pixel.color = (0, 0, 0) if stability == 1 else hsb(
        hue_degrees=int(stability * 360),
        saturation=stability,
        brightness=1,
    )

image.show()
image.save("saves/mandlebrot.png", "PNG")