
def affiliation_to_groups(list_sorted_by_color,list_of_union_words,length_word):
    print("affiliation_to_groups")
    radius=find_optimal_radiuse(list_sorted_by_color,length_word)
    master=list_sorted_by_color[0][0]
    num_groupe=radius+1
    list_of_masters=[master]
    for list_positions_of_value in list_sorted_by_color:
        original_value=list_positions_of_value[0]
        if original_value > master + radius:
            master = original_value
            num_groupe += 1
            list_of_masters.append(master)
        compression_value=original_value-master+num_groupe
        for position in range(1,list_positions_of_value.__len__()):
            list_of_union_words[list_positions_of_value[position]]=compression_value
    print("finish affiliation_to_groups")
    return list_of_masters, list_of_union_words, radius


def find_optimal_radiuse(data,length_word):
    print("find_optimal_radiuse")
    relevant_values=[i[0] for i in data]
    radius=2**(length_word/2)
    index=0
    while(True):
        #index+=1
        counter_of_companies = 0
        master=relevant_values[0]+radius
        for i in relevant_values:
            if i>master:
                counter_of_companies+=1
                master=i+radius
        case= radius-counter_of_companies
        if case>=1:
            radius=radius*0.5
        else:
            if case<-1:
                radius=radius*1.5
            else:
                print("finish find_optimal_radiuse")
                return int(radius)+1
