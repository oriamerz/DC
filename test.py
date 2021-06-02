from data_sourse_image import get_pixels

def extract(filename="test_pixel_map_of_short_words", sourceImageSize = (503,322), radius=24):
    values_less_then_256 = get_pixels(filename)



