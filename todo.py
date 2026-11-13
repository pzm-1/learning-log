while True:
    print("\n===终端待办===")
    print("1.查看任务")
    print("2.添加任务")
    print("3.退出")

    choice = input("请选择操作:")
    if choice == "1":
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                print("---任务清单---")
                tasks = f.readlines()
                if len(tasks) == 0:
                    print("没有任务呢")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task.strip()}")
        except FileNotFoundError:
            print("还没有任何添加记录,请先按2添加任务")
    elif choice == "2":
        new_tesk = input("请输入新的任务:")
        with open("tasks.txt", "a", encoding="utf-8") as f:
            f.write(new_tesk + "\n")
    elif choice == "3":
        print("退出程序")
        break
    else:
        print("输入错误,请重新选择")
