import easyocr

def extract_text_from_image(image_path):

    reader = easyocr.Reader(['en'], gpu=True)

    # Extract text from image
    result = reader.readtext(image_path, text_threshold=0.2)

    # Separate the extracted texts with spaces and combine them into one string
    text = ' '.join([entry[1] for entry in result])
    return text

def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write(text) 