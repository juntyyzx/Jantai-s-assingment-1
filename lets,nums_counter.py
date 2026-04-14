print('Введите ваш текст:',end = '')
text = input()
let_count = 0
num_count = 0
other_symbol_count = 0
letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбюёЁ'
numbers = '1234567890'
for i in range(len(text)):
    if text[i] in letters:
        let_count += 1
    elif text[i] in numbers:
        num_count += 1
    else:
        other_symbol_count += 1
print('Колличество цифр в вашем тексте:', num_count)
print('Колличество букв в вашем тексте:', let_count)
print('Колличество символов, не отнощясимся к буквам и цифрам в вашем тексте:', other_symbol_count)
