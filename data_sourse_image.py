from math import log2, sqrt, ceil
from PIL import Image


def get_input_list(filename):
    """returning a list of the pixels in a 24-bit numbers"""
    return Union_the_shades_of_pixels(get_pixels(filename))


def Union_the_shades_of_pixels(list_of_all_the_words):
    """converting the RGB pixels to a 24-bit single number"""
    power_8 = 2 ** 8
    power_16 = 2 ** 16
    return [list_of_all_the_words[i] + list_of_all_the_words[i + 1] * power_8 + list_of_all_the_words[i + 2] * power_16
            for i in range(0, list_of_all_the_words.__len__(), 3)]

def get_image_size(filename):
    return (Image.open(filename)).size

def get_pixels(filename):
    """returning a list of all pixels in 8-bit format"""
    #print("get_pixels")
    im = Image.open(filename)
    pixel_values = list(im.getdata())
    result = []
    for i in pixel_values:
        result.append(i[0])
        result.append(i[1])
        result.append(i[2])
    #print("finish get_pixels")
    return result


def save_as_image(numbers=[], file_name='pixel_map_test.png',ImageSize = (503,322), max_input_num_len= 24):
    #print("save_as_image")
    matched_numbers = match_the_numbers_within_fixed_length_patterns(numbers, 8, max_input_num_len)
    save_image(matched_numbers, file_name, ImageSize)

def save_image(numbers=[], file_name='pixel_map_test.png',ImageSize = (503,322)):
    try:
        itra = iter(numbers)
        im = Image.new("RGB", (ImageSize[0], ImageSize[1]), "#000000")
        pixels = im.load()
        for i in range(ImageSize[1]):
            for j in range(ImageSize[0]):
                color= (int(next(itra)), int(next(itra)), int(next(itra)))
                pixels[j, i]=color

        while (True):
            print(next(itra))

    except StopIteration:
        im.save(file_name)
        print("finish save_as_image")


def match_the_numbers_within_fixed_length_patterns(numbers, fixed_patterns_len, max_input_num_len):
    try:
        #print("match_the_numbers_within_fixed_length_patterns")
        itr = iter(numbers)
        result = []
        num = 0
        dev=2**(-fixed_patterns_len)
        while (True): #Run until there is the StopIteration
            i = 1
            num = itr.__next__() + num * (2 ** max_input_num_len)
            while i < fixed_patterns_len/(max_input_num_len+fixed_patterns_len+log2(fixed_patterns_len)):
                i += 1
                num = itr.__next__() + num * (2 ** max_input_num_len)
            dev = dev * (2 ** (i * max_input_num_len))
            while dev >= 1:
                result.append(int(num / dev))
                num = num % dev
                dev = dev / (2 ** fixed_patterns_len)
    except StopIteration:
        result.append(num)  # The last num enters
        #print("finish match_the_numbers_within_fixed_length_patterns")
        return result



