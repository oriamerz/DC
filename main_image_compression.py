from data_sourse_image import save_as_image, get_input_list, ceil, log2, get_image_size,sqrt
from sorts import list_of_the_words_in_file_sorted_according_to_length
from words_compression import affiliation_to_groups


def main_image_compression():
    """"
    Data compression of an image without data loss
    """
    filename = "test"  # To simulation.
    length_word = 24  # Length of RGB pixel

    # Gets the data from memory in format list of numbers, each number is a different color.
    list_of_pixels = get_input_list(r"" + filename + ".png")
    image_size=get_image_size(r"" + filename + ".png")

    # Returns a list of relevant colors and in which pixels were consumed.
    list_sorted_by_color = list_of_the_words_in_file_sorted_according_to_length(list_of_pixels,
                                                                                length_word)

    # Searches for common subwords within the color word and saves them in a dictionary. Then the software changes each common subword in its index number in the dictionary.
    list_of_keywords, list_of_shortened_words, radius_len, group_number_len = affiliation_to_groups(list_sorted_by_color,
                                                                                               list_of_pixels.__len__(),
                                                                                               length_word)


    # Save as "png" format to reduce image size
    image_size=(int(ceil(image_size[0]/sqrt(length_word/(group_number_len+radius_len)))),int(ceil(image_size[1]/sqrt(length_word/(group_number_len+radius_len)))))
    save_as_image(numbers=list_of_shortened_words,
                  file_name=filename + "_pixel_map_of_short_words.png", ImageSize=image_size,
                  max_input_num_len= group_number_len+radius_len)
    image_size=(int(ceil(sqrt(list_of_keywords.__len__()))),int(ceil(sqrt(list_of_keywords.__len__()))))
    save_as_image(numbers=list_of_keywords, file_name=filename + "_pixel_map_of_keywords.png", ImageSize=image_size,
                  max_input_num_len=length_word)


if __name__ == '__main__':
    main_image_compression()
