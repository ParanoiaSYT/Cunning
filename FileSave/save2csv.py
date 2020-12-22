import numpy as np



a=np.array([1,2,3,4,5])
print(a)

b=np.arange(0,100).reshape(10,10)

c=np.array([[1,3.1415926],[99,2818.218858817275731283]])



# delimiter设置分割符
name='20201029_CSV2File'
np.savetxt('%s.csv'%name,a,delimiter=',',encoding='utf-8')
# 设置格式化存储数据
np.savetxt('%s.csv'%name,c,fmt='%.8f',delimiter=',',encoding='utf-8')


# 如果要追加，防止覆盖
with open('%s.csv'%name,'ab') as f:
    d = np.array([[1, 3.1415926], [99, 2818.218858817275731283]])
    np.savetxt('%s.csv' % name, d, fmt='%.8f', delimiter=',', encoding='utf-8')
