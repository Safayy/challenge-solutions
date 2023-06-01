def remove_every_other(my_list):
    return my_list[::2]
    # i = len(my_list) - 1
    # while i>=0:
    #     if (i%2!=0):
    #         my_list.pop(i)
    #     i-=1
    # return my_list

print( remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]) , end=" ")