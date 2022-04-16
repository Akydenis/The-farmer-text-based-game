
import json



class Store:
    money = 300000
    items_to_use = []
    cost_item = None
    ask_answer = 1
    seed_bought = False
    garden_bought = False

    def shop():
        general_goods =      {1: 'для перехода в меню покупки стройматериалов теплицы', 
                              2: 'для перехода в меню покупки семян', 
                              3: 'для перехода в меню покупки системы отопления и садовых приспособлений', 
                              4: 'для перехода в меню покупки систем орошения',
                              5: 'для перехода в меню покупки удобрений'} 
        
        items_to_buy = {}
           
        
        while input("Вы хотите что-либо купить? (да/нет): \n ").lower() == "да":
            if len(Store.items_to_use) >=1:
                print(" ")
                print('Магазин недоступен. Вам нужно завершить работы по уже купленным предетам')
                print(Store.items_to_use)
                print(" ")
                break

            for keys, values in general_goods.items():
                print("Нажмите", keys, values)

            choice = int(input("\n Выберите цифру, соответствующую категории товаров: \n "))
            if choice in general_goods.keys():
                with open('items.json', 'r', encoding = 'utf-8') as items:
                    list = json.loads(items.read())
                if choice == 1:
                    items_to_buy.update({1: list['1']['name'], 2: list['2']['name']})
                    price =  str(list['1']['cost'])+ " Рублей           "+    str(list['2']['cost']) + " Рублей"
                    print("Арочная теплица лучше держит тепло, в то время как деревянная теплица вмещает в себя гораздо больше растений")
                    Store.garden_bought = True

                elif choice == 2:
                    items_to_buy.update({3: list['3']['name'], 4: list['4']['name']})
                    price =  str(list['3']['cost'])+ " Рублей           "+    str(list['4']['cost']) + " Рублей"
                    Store.seed_bought = True
                    print("Помидоры стоят дороже на рынке, в то время как огурцы гораздо раньше приносят плоды")
                    
                elif choice == 3:
                    items_to_buy.update({5: list['5']['name'], 6: list['6']['name']})
                    price =  str(list['5']['cost'])+ " Рублей           "+    str(list['6']['cost']) + " Рублей"
                    print("Отопление работает при условии построенной теплицы. Подвязка растения улучшает плодоношение")
                    """
                elif choice == 4:
                    items_to_buy.update({1: 'Шланги', 2: 'Капельное орошение'})
                elif choice == 5:
                    items_to_buy.update({1: 'Удобрения N+P+Ca', 2: 'Удобрения Ka+Mg'})
                    """
                print()
                print(items_to_buy)
                print(price)
                print()
                

                Store.ask_answer = int(input(" \n Выберите цифру, соответствующую товару: \n "))
                if Store.ask_answer in items_to_buy.keys():
                        if Buying.buy(Buying.cost_jsn[str(Store.ask_answer)]['cost']):
                           Store.items_to_use.append({list[str(Store.ask_answer)]['name']})
                           
                else:
                    print("Товара под таким номером не существует")
                items_to_buy.clear()
                print("Вы купили: ", Store.items_to_use)


class Buying:
    cost_item = ""
    cost_jsn = {}
    with open('items.json', 'r', encoding = 'utf-8') as items:
        cost_jsn = json.loads(items.read())
        cost_item  = cost_jsn[str(Store.ask_answer)]['cost']

    def buy(cost_item):
        Store.money -= cost_item
        print(Store.money)
        return True










#На случай, если придется сделать инвентарь тоже в джейсоне
"""        
def write_json(data):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open('items.json', 'w', encoding = 'utf-8') as items:
        json.dump(data, items, indent = 4)
"""                

