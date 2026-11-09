scores_dict = {
    "a":85,
    "b":92,
    "c":59,
    "d":99,
    "e":65,
    "f":43,
    "g":99
}

print("===欢迎使用成绩分析系统===")
print(f"本次一共录入了 {len(scores_dict)} 位同学的成绩")

total = 0
max_score = 0
max_names = []

for name, score in scores_dict.items():
    total = total + score

    if score > max_score:
        max_score = score
        max_names = [name]
    elif score == max_score:
        max_names.append(name)

average = total / len(scores_dict)

print(f"全班的最高分是: {max_names}, 考了 {max_score} 分")
print(f"全班的平均分是: {average:.2f} 分")

print("===补考名单===")
fail_names = []
for name, score in scores_dict.items():
    if score < 60:
        fail_names.append(name)
if len(fail_names) > 0:
    print(f"总共有 {len(fail_names)} 位同学需要补考")
    print(f"名单如下: {fail_names}")
else:
    print("全员及格")