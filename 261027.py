def show_menu():
    print(
        '''===== 通讯录 =====
1. 添加联系人
2. 查看全部
3. 退出
''')


def add_contact(contacts):
    name = input('请输入姓名：')
    number = input('请输入电话：')
    contacts[name] = number
    print(f'已添加：{name}')


def show_all(contacts):
    if not contacts:
        print('通讯录为空')
    else:
        for key, value in contacts.items():
            print(f'{key}: {value}')


def main():
    contacts = {}
    while True:
        show_menu()
        choice = input('请选择：')
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            show_all(contacts)
        elif choice == '3':
            print('再见')
            break
        else:
            print('无效选择')


if __name__ == '__main__':
    main()
