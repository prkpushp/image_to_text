from PIL import Image
import pytesseract

# Path to the image file
image_path = "/path/of/the/image/png"

# Open the image using Pillow (PIL)
image = Image.open(image_path)

# Use Tesseract to extract text from the image with English language
text = pytesseract.image_to_string(image, lang='eng')

# Print the extracted text
print(text)
