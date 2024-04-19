import sys
from glob import glob

from PIL import Image, ImageDraw, ImageFont
from pygments import highlight
from pygments.formatters import ImageFormatter
from pygments.lexers import PythonLexer


def render_python_file(input_file, output_file):
    # Read Python source code from file
    with open(input_file, 'r') as file:
        code = file.read()

    # Create ImageFormatter with desired style
    formatter = ImageFormatter(style='rrt', line_numbers=True)

    # Highlight Python code
    image = highlight(code, PythonLexer(), formatter)

    with open(output_file, "wb") as f:
        f.write(image)


if __name__ == "__main__":

    max_width = 0
    max_height = 0

    for f in glob("history/*.py"):
        out_name_tmp = f"{f}_tmp.png"
        out_name = f"{f}.png"
        render_python_file(f, out_name_tmp)
        img_tmp = Image.open(out_name_tmp)

        # Max dimensions (in my case) are below 1080 x 1920 so I do not need any rescaling

        img = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0))
        img.paste(img_tmp, (0, 0))
        img.save(out_name, 'PNG')

        if img_tmp.width > max_width:
            max_width = img_tmp.width

        if img_tmp.height > max_height:
            max_height = img_tmp.height

print(max_width)
print(max_height)
