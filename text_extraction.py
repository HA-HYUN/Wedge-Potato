import easyocr

def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = ' '.join([entry[1] for entry in result])
    return text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(text)