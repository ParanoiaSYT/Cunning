import re

f=open('过滤字段.txt')

res=[]
content=[]
number=1

def export(res):
    for i in range(len(res)):
        res[i]=(''.join(res[i]))
        print(res[i])

for each_line in f:
    if each_line[0]!='#':
        content.append(each_line)
    elif re.match(r"[\u4E00-\u9FA5]",each_line[1]):
        if number:
            res.append(content)
            content = []
            content.append(each_line)
        else:
            number = 1
            content.append(each_line)
    else:
        if number:
            number=0
            res.append(content)
            content=[]
            content.append(each_line)
        else:
            content.append(each_line)
res.append(content)

print(res)
export(res)


# print(','.join(res[1]))
# print(res)
# print(res[1])
# print(res[2])
# print(res[3])
#
# print(res)