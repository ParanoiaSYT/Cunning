import pandas as pd


# df=pd.read_table('/Users/sunyuting/Downloads/Unknown.dat',sep='::',header=None,engine='python',encoding='utf-16')
# df=pd.read_table('/Users/sunyuting/Downloads/Unknown.dat',sep='::',header=None,engine='python')



f=open('/Users/sunyuting/Downloads/Unknown.dat','r',encoding='utf-16')
lines=f.readlines()[0]
try:
    line=lines.decode('utf-16')
except:
    # f = open('/Users/sunyuting/Downloads/Unknown.dat', 'r')
    # lins = f.readlines()
    pass
print(line)