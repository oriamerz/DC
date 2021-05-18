

from  data_sourse import save_as_image, get_input_list
from sorts import list_of_the_words_in_file_sorted_according_to_length
from image_compression import affiliation_to_groups


def main():
    filename = "test"
    length_word = 24
    list_of_union_the_shades_of_pixels = get_input_list(r""+filename+".png")
    list_sorted_by_color = list_of_the_words_in_file_sorted_according_to_length(list_of_union_the_shades_of_pixels,length_word)
    list_of_masters, short_list_of_union_the_shades_of_pixels, radius=affiliation_to_groups(list_sorted_by_color,list_of_union_the_shades_of_pixels,length_word)
    #print("radius : "+str(radius))
    #print("list_of_masters: "+ str(list_of_masters))
    #print("list_sorted_by_color: "+str(list_sorted_by_color))
    #print("List_of_Union_the_shades_of_pixels: "+str(List_of_Union_the_shades_of_pixels))
    save_as_image(numbers=short_list_of_union_the_shades_of_pixels,file_name=filename+"pixel_map_of_union_words.png",max_input_num_len=2*radius)
    save_as_image(numbers=list_of_masters,file_name=filename+"pixel_map_of_master.png" ,max_input_num_len=length_word)

if __name__ == '__main__':
    main()

