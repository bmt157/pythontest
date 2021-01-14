x = 1
y = 10
i = 0
# def x2(x):
# 	x * 2
# def giamx(x):
# 	x - 1
while x < y or x > y:
	if x < y:
		y //= 2
		i += 1
		continue
	if x > y:
		x -= 1
		i += 1
		continue
	else :
		break


print("can so buoc de x = y la:",i)