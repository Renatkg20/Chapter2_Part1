user_input = input("Pls type the sentence ")
result = user_input.split()
result.sort(key=len)
final_result = " ".join(result)
print(final_result)