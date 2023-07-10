from time import sleep
from sense_hat import SenseHat #this code for using hardware(sense_hat)=> sense_emu (using for program)
from PIL import Image, ImageDraw


hat = SenseHat()

hat.clear()
origin=(7, 7)
while True:
    a = hat.get_accelerometer_raw()
    img = Image.new('RGB', (15, 15))
    draw = ImageDraw.Draw(img)
    dest = (origin[0] + a ['x'] * 7.0, origin[1] + a['y'] * 7.0)
    draw.line([origin, dest], fill=(0, 0, 255), width=3)
    img = img.resize((8, 8), Image.BILINEAR)
    hat.set_pixels(list(img.getdata()))
    sleep(0.04)