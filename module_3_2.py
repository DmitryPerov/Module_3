def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    if recipient == sender: # проверка совпадения отправителя и получателя
        print('Нельзя отправить письмо самому себе!')
    else:
        def check_address(address_to_check):    # функция проверки корректности адреса
            last_in_string = False
            at_sign_count = address_to_check.count("@")  # проверка наличия в адреса одного символа '@'
            for i in range(len(countries)):   # перебор элементов списка кодов стран
                country_sign_position = address_to_check.find(countries[i])
                if country_sign_position + len(countries[i]) == len(address_to_check):  # проверка того, что код страны в конце строки
                    last_in_string = True
                    i = len(countries) + 1
            if last_in_string and at_sign_count == 1:   # если в адресе есть знак '@' и код страны в конце адреса, то адрес корректен
                address_ok = True
            else:
                print("Неправильный формат адреса отправителя:", end = ' ')
                address_ok = False
                if last_in_string == False:           # если в адресе не указан код страны
                    print("код страны неверный или отсутствует")
                if at_sign_count == 0:                 # если в адресе нет символа "@"
                    print("отсутствует символ' @'")
            return address_ok
        address_recipient_ok = check_address(recipient)
        address_sender_ok = check_address(sender)
        if address_recipient_ok and address_sender_ok:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса <',sender,'> на адрес <',recipient,'>')
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <', sender, '> на адрес <', recipient, '>')
        else:
            print('Невозможно отправить письмо с адреса <',sender,'> на адрес <',recipient,'>')

countries = ['.ru','.com','.net']
#send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

