import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = int(input('請從0~100中猜一個數字: '))
	print('你猜了第', count, '次')
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	