from math import log2
from sorts import *
from  data_sourse import save_as_image, get_pixels
from imag_compression import union_words, affiliation_to_groups,find_optimal_radiuse


def main():
    filename = r"test.png"
    length_word = 24
    list_of_all_the_words=get_pixels(filename)
    list_of_union_words=union_words(list_of_all_the_words)
    list_sorted = list_of_the_words_in_file_sorted_according_to_lenngh(list_of_union_words,length_word)
    radius  = find_optimal_radiuse(list_sorted, length_word)
    list_of_masters=affiliation_to_groups(list_sorted,list_of_union_words,radius)
    #print("radius : "+str(radius))
    #print("list_of_masters: "+ str(list_of_masters))
    #print("list_sorted: "+str(list_sorted))
    #print("list_of_union_words: "+str(list_of_union_words))
    save_as_image(numbers=list_of_union_words,file_name="pixel_map_of_union_words.png",max_input_num_len=2*radius)
    save_as_image(numbers=list_of_masters,file_name="pixel_map_of_master.png" ,max_input_num_len=length_word)

if __name__ == '__main__':
    main()

