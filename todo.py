while True:
    print("\n===终端待办===")
    print("1.查看任务")
    print("2.添加任务")
    print("3.退出")
    print("4.批量导入")
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
    elif choice == "4":
        print("开始批量导入...")
        try:
            with open("batch_tasks.txt", "r", encoding="utf-8") as batch_file:
                batch_lines = batch_file.readlines()
            with open("tasks.txt", "a", encoding="utf-8") as main_file:
                for i, task in enumerate(batch_lines):
                    main_file.write(task.strip() + "\n")
                    progress = int((i + 1) / len(batch_lines) * 100)
                    print(f"\r进度: [{progress}%]已导入 {i+1}/{len(batch_lines)}条...", end="")
            print("\n 批量导入完成")
        except FileNotFoundError:
            print("错误,无文件")
    else:
        print("输入错误,请重新选择")
