def print_lol(the_list,level=0):
    '''
    :BIF isinstance()
    :param the_list:
    :return:
    '''

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)
movies= [                                       #my list
    'The Holy Grail',1975,'Terry Jone & Terry Gilliam',91,
    ['Graham Chapman',['Michael Palin','John Cleese',
                       'Terry Gilliam','Eric Idle','Terry Jones']]]
print_lol(movies)