from math import log2,sqrt
from PIL import Image



def get_pixels(name):
    print("get_pixels")
    im = Image.open(name)
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

    numbers_divid=divide_the_numbers_into_fixed_patterns(numbers, 8, max_input_num_len)
    try:
        size=int(sqrt(numbers_divid.__len__()/3))
        itr= iter(numbers_divid)
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

def divide_the_numbers_into_fixed_patterns_for_bigest_numbers(numbers1,output_num_len,max_input_num_len): #Work, but if condition: max_present_len>=desired_len
    result=[]
    dev=2**(-output_num_len)
    num=0
    for j in numbers1:
        num= j+num*(2**max_input_num_len)
        dev = 2**(max_input_num_len+log2(dev))#= log(dev)-desired_len+max_present_len-desired_len
        while dev>=1:
            result.append(int(num/dev))
            num=num%dev
            dev=dev/(2**output_num_len)
    result.append(num) #The last num enters without change
    return result


#divide_the_numbers_into_fixed_patterns([4,9,4,15],8,4)