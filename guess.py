import random

print("猜数字")
print("想一个一到一百的数字")

secret = random.randint(1, 100)
count = 0  # 记录猜的次数

max_try = 10
while True:
    if count >= max_try:
        print(f"失败了,正确答案是 {secret}")
        break
    count += 1
    guess = int(input("请猜一个数字:"))

    if guess > secret:
        print("太大了")
    elif guess < secret:
        print("太小了")
    else:
        print(f"答对了!你一共猜了 {count} 次")
        break
