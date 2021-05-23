

from  data_sourse import save_as_image, get_input_list
from sorts import list_of_the_words_in_file_sorted_according_to_length
from image_compression import affiliation_to_groups


def main_image_compression():
    """"
    Data compression of an image without data loss
    """
    filename = "test" #To simulation.
    length_word = 24  #lenght of RGB pixel


    #Gets the data from memory in format list of numbers, each number is a different color.
    list_of_union_the_shades_of_pixels = get_input_list(r""+filename+".png")

    #Returns a list of relvent colors and in which pixeles were consumed.
    list_sorted_by_color = list_of_the_words_in_file_sorted_according_to_length(list_of_union_the_shades_of_pixels,length_word)

    #Searches for common subwords within the color word and saves them in a dictionary. Then the software changes each common subword in its index number in the dictionary.
    list_of_masters, short_list_of_union_the_shades_of_pixels, radius=affiliation_to_groups(list_sorted_by_color,list_of_union_the_shades_of_pixels,length_word)

    #Save as "png" format to reduce image size
    save_as_image(numbers=short_list_of_union_the_shades_of_pixels,file_name=filename+"pixel_map_of_union_words.png",max_input_num_len=2*radius)
    save_as_image(numbers=list_of_masters,file_name=filename+"pixel_map_of_master.png" ,max_input_num_len=length_word)

if __name__ == '__main__':
    main_image_compression()

