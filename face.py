def convert(text):
    step1 = text.replace(":(", "happy")
    step2 = step1.replace(":)", "sad")
    return step2
user_input = input("请输入")
final_result = convert(user_input)
print(final_result)