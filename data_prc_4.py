import os
os.chdir('F:\pycharm\headfirst35')
print(os.getcwd())
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
    data.close()
except:
    print('The data file is missing!')
# print(man)
# print(line_spoken)
try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)

    # man_file.close()
    # other_file.close()
except:
    print('File error.')
finally:
    man_file.close()
    other_file.close()