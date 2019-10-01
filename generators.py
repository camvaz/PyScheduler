
lst = ["T1",1 ,2];

i=0
while i < 2:
    print(i)
    lst.pop(i)
    if i == 0:
        i-=1
    i+=1


print(lst)
# matches = [x for x in lst if x == "T1"]
# print(matches[0]);