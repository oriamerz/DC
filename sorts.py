from math import log2
def sort_by_bucket_list(data,length_word):
    print("sort_by_bucket_list")
    t= 2**length_word
    bucket_list = [None for i in range (t)]
    index=-1
    for value in data:
        index+=1
        #position = value.__index__()
        if bucket_list[value]==None:
            bucket_list[value] = [value,index]
        else:
            bucket_list[value].append(index)
    sorted_list = []
    for i in bucket_list:
        if i != None:
            sorted_list.append(i)
    print("finish sort_by_bucket_list")
    return sorted_list


def standard_sort(data):
    print("standard_sort")
    data=[(i, data[i]) for i in range(data.__len__())]
    data.sort(key=lambda a:a[1])
    sorted_list=[[data[0][1],data[0][0]]]
    index_sorted_list=0
    for i in range(1,data.__len__()):
        if sorted_list[index_sorted_list][0] == data[i][1]:
            sorted_list[index_sorted_list].append(data[i][0])
        else:
            index_sorted_list+=1
            sorted_list.append([data[i][1],data[i][0]])
            #sorted_list[index_sorted_list]=[data[i][1],data[i][0]]
    print("finish standard_sort")
    return sorted_list

def list_of_the_words_in_file_sorted_according_to_lenngh(data,length_word):
    if (data.__len__()*log2(data.__len__()) > 2**length_word):
        return (sort_by_bucket_list(data,length_word))
    else:
        return (standard_sort(data))
