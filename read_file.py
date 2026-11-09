with open('data.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()

max_score = 0
max_name = ""
total = 0
count = 0

for line in lines:
    parts = line.strip().split(",")
    name = parts[0]
    score = int(parts[1])
    total = total + score
    count = count + 1
    if score > max_score:
        max_score = score
        max_name = name

print(f"一共读取了{count}位同学的成绩")
print(f"平均分是: {total / count:.2f} 分")
print(f"最高分是 {max_name}, {max_score} 分")