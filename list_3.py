def print_lol(the_list):                        #define function
    for nested_item in the_list:
        if isinstance(nested_item, list):
            print_lol(nested_item)
        else:
            print(nested_item)

movies= [                                       #my list
    'The Holy Grail',1975,'Terry Jone & Terry Gilliam',91,
    ['Graham Chapman',['Michael Palin','John Cleese',
                       'Terry Gilliam','Eric Idle','Terry Jones']]]
print_lol(movies)