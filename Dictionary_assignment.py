Dic={}
while True:
    key = int(input())
    value = input()
    if key==0 or value=="문자열 종료":
        print("그만")
        print(Dic)
        break
    Dic[key] = value

dict_key= list(Dic.keys())
dict_value = list(Dic.values())
dict_item = list(Dic.items())
print(dict_key, dict_value, dict_item)