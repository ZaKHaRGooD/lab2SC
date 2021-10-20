print('Декодирование кода Хемминга по схеме (7, 4)')
print('Введите набор из 7 цифр "0" и "1"')

# Ввод данных и проверка их корректности
while True:
    hammingCodeInput = input()
    if len(hammingCodeInput) == 7 and (hammingCodeInput.count('1') + hammingCodeInput.count('0') == 7):
        break
    else:
        print('Введенные данные некорректны\nПопробуйте в следующий раз')

# Нахождение названия ошибочного бита
def ErrorPosition(n):
        positions = ['r1', 'r2', 'i1', 'r3', 'i2', 'i3', 'i4']
        return positions[n-1]

# Замена ошибочного бита и последующая конкатенация строк цифр в единый ответ
def BitCorrection(n):
      positions = ['r1', 'r2', 'i1', 'r3', 'i2', 'i3', 'i4']
      if bits[positions[n-1]] == 1:  # нахожу название ключа в списке массива, а затем передаю его словарю
            bits[positions[n - 1]] = 0
      else:
            bits[positions[n - 1]] = 1
      return str(bits['i1']) + str(bits['i2']) + str(bits['i3']) + str(bits['i4'])

# Конкатенация строк цифр в случае ненахождения ошибки при декодирование
def HemmimgCodeWithoutError():
      return str(bits['i1']) + str(bits['i2']) + str(bits['i3']) + str(bits['i4'])

bits = { 'r1' : int(hammingCodeInput[0]),
         'r2' : int(hammingCodeInput[1]),
         'i1' : int(hammingCodeInput[2]),
         'r3' : int(hammingCodeInput[3]),
         'i2' : int(hammingCodeInput[4]),
         'i3' : int(hammingCodeInput[5]),
         'i4' : int(hammingCodeInput[6]) }

s1 = (bits['r1'] + bits['i1'] + bits['i2'] + bits['i4']) % 2
s2 = (bits['r2'] + bits['i1'] + bits['i3'] + bits['i4']) % 2
s3 = (bits['r3'] + bits['i2'] + bits['i3'] + bits['i4']) % 2

# нахождения синдрома и индекса ошибочного бита
errorPosition = 2 ** 0 * s1 + 2 ** 1 * s2 + 2 ** 2 * s3

# вывод ответа
if errorPosition != 0:
      print('Найден разряд с ошибкой\nИндекс ошибочного разряда:', errorPosition, '\nТип разряда и его номер:', ErrorPosition(errorPosition))
      print('Вы ввели:', hammingCodeInput, '\nПравильный набор цифр:', BitCorrection(errorPosition))
else:
      print('Ошибок не найдено\nИтоговое сообщение: ', HemmimgCodeWithoutError())
