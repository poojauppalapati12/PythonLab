list = [1,4,5,6,1,2,5,6,2,4,5]
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print("% s -> % d" % (key, value))
