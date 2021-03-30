list_item = [4,6,3,6,3,7,1]

def get_smallest_positive_number(list):
    
    small_number = min(list)
    if list.count(small_number) > 1:
        for x in list:
            try:
                if min(list.count(x)) == 1:
                    return x
            except:
                return small_number
    else :
        return small_number


get_smallest_positive_number(list_item)