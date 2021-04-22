def get_link(city):
    print('Прекрасно.')
    print('Какая цена автомобиля для Вас приемлема?')

    while True:
        print('♦️ Выберите из списка')
        print('1. 0-500000')
        print('2. 500000-1000000')
        print('2. больше 1000000')
        price = input()

        if price == '1':
            print('Найдено более 500 автомобилей! Посмотри их на сайте:' \
                              f' https://auto.ru/{city}/cars/all/?price_to=500000')

        elif price == '2':
            print('Найдено более 600 автомобилей! Посмотри их на сайте:'\
                f' https://auto.ru/{city}/cars/all/?price_to=1000000&price_from=500000')

        elif price == '3':
            print('Найдено 300 автомобилей! Посмотри их на сайте' \
                           f' https://auto.ru/{city}/cars/all/?price_from=1000000')
        
        else:
            continue

        break


def search():
    print('Сейчас мы подберем для Вас идеальный автомобиль.' \
                     ' В каком городе вы хотите искать авто? Самара или Тольятти')
    while True:
        print('1. Самара')
        print('2. Тольятти')
        city = input('')
        
        if city == '1':
            get_link('samara')
        elif city == '2':
            get_link('tolyatti')
        else:
            print('К сожалению я не могу найти авто в выбранном городе, выберите' \
                                            ' один из городов Тольятти, Самара ')
            continue
        
        break

def sell():
    print('Супер! Отправьте мне ваш номер телефона, менеджер свяжется с Вами' \
                                                    ' для уточнения подробностей')
    
    while True:
        phone_number = input()
        if phone_number != '':
            print('Спасибо! Ожидайте звонка менеджера!')
            break
        else:
            print('Введите номер')
            continue        




if __name__ == "__main__":
    print('Привет! Лучший робот по покупке-продаже авто приветствует тебя!' \
                                                  ' Выбирайте, что будем делать?')
    
    
    while True:
        print('1. Найти')
        print('2. Продать')
        action = input()
        
        if action == "1":
            search()
        elif action == "2":
            sell()
            break
        else:
            print("Такого пункта нет в списке моих действий, попробуйте еще раз.")
            continue