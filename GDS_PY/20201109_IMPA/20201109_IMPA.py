import sys
print(sys.path)
sys.path.append('/Users/sunyuting/Cunning/GDS&PY/module')



import CPWModule

a=CPWModule.CPW(21.8,12)
a.trans(270,'-x')
length1=a.cal()

# a.trans_change(4.6,'+x',7.4,31)
# a.trans(200,'+x')
# a.round(100,+1/2)
# a.trans(900,'+y')
# a.round(100,-1)
# a.trans(2000,'-y')
# a.round(100,1)
# a.trans(334.6)
# length4=a.cal()-length1
# print(length4)
#
# a.trans_change(7.2,'+y',14.6,16.6)
# a.trans(1765.4,'+y')
# a.round(100,-1)
# a.trans(2200,'-y')
# a.round(100,1)
# a.trans(2200,'+y')
# a.round(100,-1)
# a.trans(1000,'-y')
# a.round(100,+1/2)
# a.trans(190.043,'+x')

# length2=a.cal()-length4-length1
# print(length2)

a.pad()
# a.number('0123456')

a.save('1109_IMPA_02.gds')

