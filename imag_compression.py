
def affiliation_to_groups(list_sorted,list_of_union_words,radius):
    master=list_sorted[0][0]
    num_groupe=radius+1
    list_of_masters=[master]
    for list_positions_of_value in list_sorted:
        original_value=list_positions_of_value[0]
        if original_value > master + radius:
            master = original_value
            num_groupe += 1
            list_of_masters.append(master)
        compression_value=original_value-master+num_groupe
        for position in range(1,list_positions_of_value.__len__()):
            list_of_union_words[list_positions_of_value[position]]=compression_value
    return list_of_masters

def union_words(list_of_all_the_words):
    power_8=2**8
    power_16=2**16
    return [list_of_all_the_words[i]+list_of_all_the_words[i+1]*power_8+list_of_all_the_words[i+2]*power_16 for i in range(0,list_of_all_the_words.__len__(),3)]\

def find_optimal_radiuse(data,length_word):
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
                return int(radius)+1
