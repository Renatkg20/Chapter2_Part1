import re
g = input ("Input the sentence ")
result = re.findall("[A-Z]", g)
final_result = ((len(result) *100) / len(g))
print(f"{round(final_result, 2)} % is capital letters in the sentence.")