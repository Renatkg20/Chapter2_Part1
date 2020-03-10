import re
g = input ("Input the sentence ")
result = re.findall("[A-Z]", g)
final_result = ((len(result) *100) / len(g))
final_result1 = 100 - final_result
print(f"{round(final_result, 2)} % is capital letters in the sentence.")
print(f"{round(final_result1, 2)} % is lower letters in the sentence.")
