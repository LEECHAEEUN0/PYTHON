List=[]
for i in range(15): # range(15) : 0~14, range(1,16): 1~15
    number = int(input())
    List.append(number)
    if i==14:
        print(List)

for i in List:
    if i%2==0:
        List.remove(i)
print(List)

for i in List:
    if i%3==0:
        List.remove(i)
print(List)       

print(List.pop(0))
List.insert(0,2)
List.insert(1,3)
List.sort()
print(List)