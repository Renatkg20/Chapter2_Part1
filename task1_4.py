list_ = (input('Pls the list for coding ')).split()
new_list = [int(i) for i in list_]
result = max(new_list) - 1

if max(new_list) < 0:
	result = abs(max(new_list))
elif result in new_list:
	result = result + 2

print(result)

# def max1(new_list):
# 	result = max(new_list) - 1

# 	elif max(new_list) < 0:
# 		result = abs(max(new_list))

# 	return (result)

# print(max1(new_list))