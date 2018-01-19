List = [34,20,56,19]
New_List = []
print(List)
for i in range(len(List)):
    print("i",i)
    if (List[i]>List[i + 1]):
        print(List[i])
    #if any(List[j]>List[i] for j in range(len(List))):
        #New_List.insert(i, List[i])
