""""For now I do not intend to enter the field of image analysis in within the project, just basic functions."""


def convert_values_to_pointers(values, values_of_dictionary):
    """
    :param values: list to convert
    :param values_of_dictionary: list of the orginal values
    :return: pointers to the orginal values in the dictionary
    """
    return list(map(lambda v: values_of_dictionary.index(v), values))
