print('1. Сформуйте стрінг, в якому міститься інформація про певне слово. "Word [тут слово] has [тут довжина слова,'
      ' отримайте з самого сдлва] letters", наприклад "Word Python has 6 letters". Для отримання слова для аналізу '
                                                                   'скористайтеся константою або функцією input().')
print('Input a world:')
a= input()
l= len (a)
print ('World ' + a + ' has ' + str(l)+ ' letters')

print('1. Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати '
      'константу або функцію input(), на екран має бути виведено лише одне повідомлення, також подумайте над '
      'варіантами, коли введені невірні дані). якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?" '
      'якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"'
      'якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"'
      'якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"'
      'у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"')

v=input('Введіть свій вік:')
result=v.isdigit()
if result is True:
    k=int(v)
    if k % 7 == 0:
        print('Вам сьогодні пощастить!')
    elif k < 7:
        print('Де твої батьки?')
    elif 16 > k > 7:
        print('Це фільм для дорослих')
    elif 65 < k:
        print('Покажіть пенсійне посвідчення')
    else:
        print('A білетів вже немає')
else: print('Неправильний формат данних')


