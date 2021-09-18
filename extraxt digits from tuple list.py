l1=[(67, 2), (34, 65), (212, 23), (17, 67), (18, )]
print("The list is: ")
print(l1)
N=2
print("The value of N is: ")
print(N)
res=[sub for sub in l1 if all(len(str(ele))==N for ele in sub)]
print("The extracted tuples are: ")
print(res)
