import os
os.chdir('F:\pycharm\headfirst35')
print(os.getcwd())
data=open('sketch.txt')
for each_line in data:
    try:
        (role,line_spoken)=each_line.split(':',1)
        print(role,end='')
        print(' said: ',end='')
        print(line_spoken,end='')
    except:
        pass
data.close()