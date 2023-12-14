import gray.cnvrt_gray as gray
import Binary_module
import splitTexts
import  text_extraction

input_image = './image/test2.jpg'
gray_image = './image/gray_image.png'
binary_image = './image/binary_image.png'
split_image = './image/split_image.png'
output_text = './output/test_output.txt'

gray.cvgray(input_image)
Binary_module.binary(gray_image)
splitTexts.detect_text_regions(binary_image)
test_text = text_extraction.extract_text_from_image(binary_image)
text_extraction.save_text_to_file(test_text, output_text)
