lst=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
cnt=len(lst)
print("total noofelements in list is:",cnt)
for i in range(0,cnt):
    if lst[i]<5:
        print(lst[i])
