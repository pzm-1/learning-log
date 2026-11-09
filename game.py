hp = 200

print("输入人物受到的伤害:")
hurt = int(input())

hp = hp - hurt
if hp <= 0:
    hp = 1
print("当前人物的血量是:", hp)

print("输入恢复的血量:")
add = int(input())

hp = hp + add
if hp > 200:
    hp = 200

print("当前人物的血量是:", hp)
