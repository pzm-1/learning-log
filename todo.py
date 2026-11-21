import json
import datetime
while True:
    print("\n===终端待办===")
    print("1.查看任务")
    print("2.添加任务")
    print("3.退出")
    print("4.批量导入")
    print("5.完成任务")
    choice = input("请选择操作:")
    if choice == "1":
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                all_tasks = json.load(f)
                if len(all_tasks) == 0:
                    print("没有任务呢")
                else:
                    print("\n---任务清单---")
                    for i, task_dict in enumerate(all_tasks):
                        task_name = task_dict["task"]
                        task_time = task_dict["time"]
                        if task_dict["done"] == True:
                            status = "[X]"
                        else:
                            status = "[ ]"
                        print(f"{i+1}. [{status}] {task_name}  (添加时间: {task_time})")
        except FileNotFoundError:
            print("还没有任何添加记录,请先按2添加任务")
    elif choice == "2":
        new_task = input("请输入新的任务:")
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_dict = {
            "task": new_task,
            "time": now_time,
            "done": False
        }
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                all_tasks = json.load(f)
        except FileNotFoundError:
            all_tasks = []
        all_tasks.append(task_dict)
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump(all_tasks, f, ensure_ascii=False, indent=4)
        print("任务添加完成,已保存到JSON文件中")
    elif choice == "3":
        print("退出程序")
    elif choice == "4":
        print("开始批量导入...")
        try:
            with open("batch_tasks.txt", "r", encoding="utf-8") as batch_file:
                batch_lines = batch_file.readlines()
        except FileNotFoundError:
            print("错误,找不到该文件")
            continue
        try:
            with open("tasks.json", "r", encoding="utf-8") as f:
                all_task = json.load(f)
        except FileNotFoundError:
                all_task = []
        for i, task in enumerate(batch_lines):
                task_name = task.strip()
                if task_name == "":
                    continue
                now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_dict = {
                    "task": task_name,
                    "time": now_time,
                    "done": False
                }
                all_tasks.append(new_dict)
                progress = int((i + 1) / len(batch_lines) * 100)
                print(f"\r进度: [{progress}%]已导入 {i+1}/{len(batch_lines)}条...", end="")
                with open("tasks.json", "w", encoding="utf-8") as f:
                    json.dump(all_task, f, ensure_ascii=False, indent=4)
                print("\n 批量导入并转化为JSON格式成功")
    elif choice == "5":
        print("\n---完成任务---")
        with open("tasks.json", "r", encoding="utf-8") as f:
            all_tasks = json.load(f)
        if len(all_tasks) == 0:
            print("没有任务可以完成")
            continue
        try:
            for i, task_dict in enumerate(all_tasks):
                if task_dict["done"] == True:
                    status = "[X]"
                else:
                    status = "[ ]"
                print(f"{i+1}. {status} {task_dict['task']}")
            task_num = int(input("请输入要完成的任务序号:"))
            if task_num < 1 or task_num > len(all_tasks):
                print("错误,没有这个任务序号")
                continue
            all_tasks[task_num - 1]["done"] = True
            with open("tasks.json", "w", encoding="utf-8") as f:
                json.dump(all_tasks, f, ensure_ascii=False, indent=4)
            print("状态更新成功")
        except FileNotFoundError:
                print("错误,找不到存档文件,请先按2添加任务")
        except ValueError:
                print("错误,请输入正确的数字")


       