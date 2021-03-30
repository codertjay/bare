list_item = [4,6,3,6,3,7,1]


def get_smallest_positive_number(list_item):
    
    small_number = min(list_item)
    sort_list =sorted(list_item)
   

    if list_item.count(small_number) > 1:
        for x in sort_list:
            print(sort_list)
            print(x)
            if sort_list.count(x) == 1:
                return x
    else:
        return small_number
   

get_smallest_positive_number(list_item)
