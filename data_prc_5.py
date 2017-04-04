import os

import sys

os.chdir('F:\pycharm\headfirst35')
print(os.getcwd())

def print_lol(the_list,indent=False,level=0,fh= sys.stdout):
    '''
    :BIF isinstance()
    :param the_list:
    :return:
    '''

    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end='',file=fh)
            print(each_item,file=fh,end='')



# if os.path.exists('sketch.txt'):
man=[]
other=[]
try:
    data=open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken)=each_line.split(':',1)
            # print(role,end='')
            if role=='Man':
                man.append(line_spoken)
            elif role=='Other Man':
                other.append(line_spoken)
        except:
            pass
except IOError as err:
    print('File error:'+str(err))
    # print('The data file is missing!')
finally:
    if 'data' in locals():
        data.close()
# print(man)
# print(line_spoken)
try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')

    print_lol(man,fh=man_file)
    print_lol(other,fh=other_file)

    # man_file.close()
    # other_file.close()
except :
    print('File error.')
finally:
    if man_file in locals():
        man_file.close()
    if other_file in locals():
        other_file.close()