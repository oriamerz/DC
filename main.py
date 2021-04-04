from math import log2
from sorts import *
from  data_sourse import open_image, save_data_compression
from imag_compression import *


def main():
    filename = 'test.PNG'
    length_word = 24
    #list_of_all_the_words=list_of_all_the_words_present_as_DEC_value( read_data(namefile), length_word )
    list_of_all_the_words=open_image(filename)
    list_of_union_words=union_words(list_of_all_the_words)
    list_sorted = list_of_the_words_in_file_sorted_according_to_lenngh(list_of_union_words,length_word )
    radius  = find_optimal_radiuse(list_sorted, length_word)
    list_of_master=affiliation_to_groups(list_sorted,list_of_union_words,radius)
    print(list_of_all_the_words.__len__()*8)
    print("radius : "+radius)
    print(list_of_master.__len__())
    print(list_sorted.__len__())
    print(list_of_union_words[0])
    print(list_of_union_words.__len__())
    print((2**24)/(radius*list_of_master.__len__()))
    save_data_compression(list_of_union_words[:100],"test.PNG",2*radius)

if __name__ == '__main__':
    main()

