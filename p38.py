name_list=[]
ave_list=[]
for i in range(6):
    name_list.append(input('Enter the name '))
    ave_list.append(int(input('Enter the average ')))
maxave=ave_list[0]
minave=ave_list[0]
index_1=0
index_2=0
for i in range(6):
    if ave_list[i]>maxave:
        maxave=ave_list[i]
        index_1=i
    elif ave_list[i]<minave:
        minave=ave_list[i]
        index_2=i
print(name_list[index_1],'has the highest average.')
print(name_list[index_2],'has the lowest average.')
