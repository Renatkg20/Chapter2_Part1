list_ = (input('Pls the list for coding ')).split()
step = int(input('input the step '))


def coding(list_, step):
	[int(i) for i in list_]
	new_list = []
	for i in range(step, len(list_)):
		new_list.append(list_[i])
	
	for r in list_[:step]:
    	 new_list.append(r)

	return new_list

print(coding(list_, step))