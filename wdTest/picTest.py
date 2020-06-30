from PIL import Image
import pytesseract


image = Image.open("img/test5.png")
content = pytesseract.image_to_string(image)

print(content)
