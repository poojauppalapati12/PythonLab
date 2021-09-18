str1 = 'Sruthi is a girl. Sruthi is good in Math , Math is her favourite subject.'
  
print("The original string is : " + str(str1))
replace_dict = {'Sruthi' :  'She', 'Math' : 'that' }

str2 = str1.split(' ')
r = set()
for i, el in enumerate(str2):
    if el in replace_dict:
        if el in r:
            str2[i] = replace_dict[el]
        else:
            r.add(el)
r = ' '.join(str2)
  
# printing result 
print("The string after replacing : " + str(r)) 
