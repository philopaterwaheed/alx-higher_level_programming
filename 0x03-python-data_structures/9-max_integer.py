def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    ax = my_list[0]
    for x in my_list:
        ax = max(ax, x)
    return (ax)
