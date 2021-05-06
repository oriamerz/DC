from PIL import Image
from math import log2, sqrt


def save_as_image(numbers=[6,45,3,434,6], file_name='pixel_map.png',max_input_num_len=24):
    print("save_as_image")
    numbers_divid=divide_the_numbers_into_fixed_patterns(numbers, 8, max_input_num_len)
    try:
        size=int(sqrt(numbers_divid.__len__()/3))
        itr= iter(numbers_divid)
        im= Image.new("RGB", (size, size+1), "#FF0000")
        for i in range(size):
            for j in range(size+1):
                im.putpixel((i, j),(next(itr), next(itr), next(itr)) )
    except StopIteration:
        im.save(file_name)
        print("finish save_as_image")


def divide_the_numbers_into_fixed_patterns(numbers1, output_num_len, max_input_num_len):
    print(numbers1)
    try:
        itr = iter(numbers1)
        result = []
        dev = 2 ** (-output_num_len)
        num = 0
        while (True):
            i = 1
            num = itr.__next__() + num * (2 ** max_input_num_len)
            while i * max_input_num_len + log2(dev) < 0:
                i += 1
                num = itr.__next__() + num * (2 ** max_input_num_len)
            dev = 2 ** (i * max_input_num_len + log2(dev))  # = i*max_present_len_len-desired_len+desired+log(dev)
            while dev >= 1:
                result.append(int(num / dev))
                num = num % dev
                dev = dev / (2 ** output_num_len)
    except StopIteration:
        result.append(num)  # The last num enters
        print("finish divide_the_numbers_into_fixed_patterns")
        return result


save_as_image()