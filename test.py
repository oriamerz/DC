from data_sourse_image import get_pixels, match_the_numbers_within_fixed_length_patterns, save_as_image1
from math import log2, sqrt, ceil

def extract(file_name=r"test_pixel_map_of_short_words.png", sourceImageSize = (503,322), radius=22):
    values_less_then_256 = get_pixels(file_name)
    matched_numbers=match_the_numbers_within_fixed_length_patterns(values_less_then_256,radius,8)
    save_as_image1(matched_numbers,"extract_"+file_name,sourceImageSize)



extract()
