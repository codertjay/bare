list_item = [4,6,3,6,3,7,1]

def get_smallest_positive_number(list_item):
    
    small_number = min(list_item)
    sort_list =sorted(list_item)
    
    try:
        if list.count(small_number) > 1:
            for x in sort_list:
                try:
                    if sort_list.count(x) == 1:
                        return x
                except:
                    return small_number
        else:
            return small_number
    except:
        return -1



get_smallest_positive_number(list_item)