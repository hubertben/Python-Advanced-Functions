
def seperate(li, key, var):
    sorted_list = []
    structured_lists = [[] for _ in range(len(key))]
    for l in li:
        lookup_val = getattr(l, var)
        if(lookup_val in key):
            structured_lists[key.index(lookup_val)].append(l)
            
    for s in structured_lists:
        sorted_list.extend(s)

    return sorted_list