import random

num = [0]*50
num_comp = [0]*11

i = 0
while i < 50:
	num[i] = i +1
	i = i + 1

i = 0
while i < 11:
	num_comp[i] = i +1
	i = i + 1

print num
print num_comp

result = [42]
result2 = [4]
while len(result) < 5 :
	i = random.randint(0,len(num)-1)
	if num[i] not in result :
		result.append(num[i]) 

while len(result2) < 2 :
	i = random.randint(0,len(num_comp)-1)
	if num_comp[i] not in result2 :
		result2.append(num_comp[i]) 

result.sort()
result2.sort()
print result
print result2