dict1 = {}
while True:
    print(
        '''===== 通讯录 =====
1. 添加联系人
2. 查看全部
3. 退出

请选择：''')
    choice = input()
    if choice == '1':
        name = input('请输入姓名：')
        number = input('请输入电话：')
        dict1[name] = number
        print('已添加姓名：', name)
    elif choice == '2':
        #空容器在 Python 里"假值"（bool({}) == False），not dict1 更简洁。
        if not dict1:
            print('通讯录为空')
        else:
            for key, value in dict1.items():
                print(key, '：', value)
    elif choice == '3':
        print('再见')
        break
    else:
        print('无效选择')
