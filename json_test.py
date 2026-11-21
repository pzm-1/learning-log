import json
player_data = {
    "name": "pzm",
    "level": 99,
    "inventory": ["大剑", "血瓶", "卷轴"],
    "stats": {
        "hp": 9999,
        "mp": 5000
    }
}
with open("save_data.json", "w", encoding="utf-8") as f:
    json.dump(player_data, f, ensure_ascii=False, indent=4)
print("游戏存档已保存为 save_data.json")
with open("save_data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
print("读取存档成功")
print(f"玩家名字: {loaded_data['name']}")
print(f"当前血量: {loaded_data['stats']['hp']}")
print(f"背包里的第一件装备: {loaded_data['inventory'][0]}")
