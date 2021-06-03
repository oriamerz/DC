from data_sourse_image import get_pixels, match_the_numbers_within_fixed_length_patterns,save_as_image
from math import log2, sqrt, ceil

def extract(file_name="test_pixel_map_of_short_words.png", sourceImageSize = (503,322), radius=2**11):
    values_less_then_256 = get_pixels(r"test_pixel_map_of_short_words.png")
    colors=get_pixels(r"test_pixel_map_of_keywords.png")
    matched_colors=match_the_numbers_within_fixed_length_patterns(colors,24,8)
    matched_numbers=match_the_numbers_within_fixed_length_patterns(values_less_then_256,int(ceil(log2(radius))),8)
    pixels= list(map( lambda i: (matched_colors[int(i/radius)]+int(i%radius)) ,matched_numbers ))
    save_as_image(pixels,"extract_"+file_name,sourceImageSize,24)



extract()
