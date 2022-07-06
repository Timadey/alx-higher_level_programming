def search_replace(my_list, search, replace):
    new_list = list(map(lambda elem, s=search: elem if s != elem else replace, my_list))
    return new_list
