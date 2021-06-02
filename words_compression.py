from math import log2, ceil


def affiliation_to_groups(list_of_data, total_words, length_word):
    """Finds the keyword and associates each of the words with the keyword closest to it.

        :param list_of_data: All the words in the format: [[value1, position1, position2...],[value2, position1, position2...]...].  , total_words: All the words in the file, length_word: Length of word in the file.
        :returns: list_of_keyword: keywords, list_of_shortened_words: All the words , radius: The maximum distance between the word to the keyword.
    """
    list_of_shortened_words = [None for i in range(total_words)]
    #print("affiliation_to_groups")
    radius = find_optimal_radius(list_of_data,
                                 length_word)  # radius: The maximum distance between the word to the keyword
    keyword = list_of_data[0][0]
    radius = 2 ** int(ceil(log2(radius)))

    keyword_group_number = 0
    list_of_keywords = [keyword]
    for list_positions_of_value in list_of_data:
        original_value = list_positions_of_value[0]
        if original_value > keyword + radius:  # Move on to the next keyword.
            keyword = original_value
            keyword_group_number += radius # Must be greater than the radius for indentify what the group name of each word is.
            list_of_keywords.append(keyword)
        compression_value = original_value - keyword + keyword_group_number
        for position in range(1, list_positions_of_value.__len__()):
            list_of_shortened_words[list_positions_of_value[position]] = compression_value
    #print("finish affiliation_to_groups")
    return list_of_keywords, list_of_shortened_words, radius


def find_optimal_radius(data, length_word):
    #print("find_optimal_radius")
    values = [i[0] for i in data]
    radius = 2 ** (length_word / 2)
    x = 2 ** (length_word / 2)
    while (True):
        counter_of_companies = 0
        keyword = values[0] + radius
        for i in values:
            if i > keyword:
                counter_of_companies += 1
                keyword = i + radius
        case = log2(radius) - log2(counter_of_companies)
        x = x / 2
        if int(case) == 0 or x < 1:
            #print("finish find_optimal_radius")
            return 2 ** int(ceil(log2(radius)))
        if case >= 1:
            radius = radius - x
        else:
            if case < -1:
                radius = radius + x
