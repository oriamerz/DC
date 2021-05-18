from math import log2,sqrt
from PIL import Image

def get_input_list(filename):
    """returning a list of the pixels in a 24-bit numbers"""
    return Union_the_shades_of_pixels (get_pixels(filename))


def Union_the_shades_of_pixels(list_of_all_the_words):
    """converting the RGB pixels to a 24-bit single number"""
    power_8=2**8
    power_16=2**16
    return [list_of_all_the_words[i]+list_of_all_the_words[i+1]*power_8+list_of_all_the_words[i+2]*power_16 for i in range(0,list_of_all_the_words.__len__(),3)]\

def get_pixels(filename):
    """returning a list of all pixels in 8-bit format"""
    print("get_pixels")
    im = Image.open(filename)
    pixel_values = list(im.getdata())
    result = []
    for i in pixel_values:
        result.append(i[0])
        result.append(i[1])
        result.append(i[2])
    print("finish get_pixels")
    return result

def save_as_image(numbers=[], file_name='pixel_map_test.png',max_input_num_len=2**24):
    print("save_as_image")
    max_input_num_len=log2(max_input_num_len)
    if max_input_num_len%1>0:
        max_input_num_len=int(max_input_num_len)+1
    else:
        max_input_num_len = int(max_input_num_len)
    numbers_divided=divide_the_numbers_into_fixed_patterns(numbers, 8, max_input_num_len)
    try:
        size=int(sqrt(numbers_divided.__len__()/3))
        itr= iter(numbers_divided)
        im= Image.new("RGB", (size, size+1), "#000000")
        for i in range(size):
            for j in range(size+1):
                im.putpixel((i, j),(next(itr), next(itr), next(itr)))
        while (next(itr)):
            pass
    except StopIteration:
        im.show()
        im.save(file_name)
        print("finish save_as_image")


def divide_the_numbers_into_fixed_patterns(numbers1,output_num_len,max_input_num_len):
     try:
        print("divide_the_numbers_into_fixed_patterns")
        itr = iter(numbers1)
        result=[]
        dev=2**(-output_num_len)
        num=0
        while (True):
            i=1
            num= itr.__next__()+num*(2**max_input_num_len)
            while i*max_input_num_len+log2(dev)<0:
                i+=1
                num = itr.__next__() + num * (2 ** max_input_num_len)
            dev = 2 ** (i*max_input_num_len + log2(dev))#= i*max_present_len_len-desired_len+desired+log(dev)
            while dev>=1:
                result.append(int(num/dev))
                num=num%dev
                dev=dev/(2**output_num_len)
     except StopIteration:
        result.append(num)  # The last num enters
        print("finish divide_the_numbers_into_fixed_patterns")
        return result




#divide_the_numbers_into_fixed_patterns([4,9,4,15],8,4)