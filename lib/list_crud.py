def create_an_empty_list():
    return []

def create_a_list():
    lst = [1, 2, 3, 4]
    return lst

def add_element_to_end_of_list(l, element):
    l.append(5)
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, 0)
    return l

def remove_element_from_end_of_list(l):
    remove = l.pop()
    return l

def remove_element_from_start_of_list(l):
    l.pop(0)
    return None

def retrieve_first_element_from_list(l):
    first = l[0]
    return first
pass

retrieve_first_element_from_list()

def retrieve_element_from_index(l, index):
    ret = l[2]
    return ret
pass

def retrieve_last_element_from_list(l):
    last = l.[-1]
    return last
