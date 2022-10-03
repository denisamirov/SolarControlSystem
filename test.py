from datetime import datetime
from time import sleep
from pyfirmata import Arduino, util
'Turn on Arduino in serial port № 3'
board = Arduino('COM3')
iterator = util.Iterator(board)
iterator.start()
'Read sensor value from A0'
v = board.get_pin('a:0:i')
c = board.get_pin('a:3:i')
r = board.get_pin('a:2:i')

while True:
       'Time out'
       sleep(30.0)
       'Sensor Value'
       voltage = v.read()
       current = c.read()
       resistence = r.read()
       v0 = ((voltage * 5) / 1024) / (7500 / (30000 + 7500)) * 1000
       c0 = ((current * 5000 / 1024) - 2500) / 185



       r0 = resistence * 7.5
       print(f' Напряжение {v0},\n Сила тока {current},\n Сопротивление {r0}')
       'Write in shell'
       # print(current)
       # print(f' Напряжение {v0}\n Сила тока {c0}\n Сопротивление {r0}')
       'Create .txt file'
       name = ('./log/'
               + str(datetime.now())[0:10]) \
              + '_' + (str(datetime.now())[11:13]) \
              + '_' + (str(datetime.now())[14:16]) \
              + '_' + (str(datetime.now())[17:19]) \
              + '.txt'
       'Open file for write sensor value'
       a = open(name, 'w', encoding='utf-8')
       'Write in .txt file - current date, current time and sensor value'
       a.write('Напряжение, В ' + str(v0) + '\n'+
               'Сила тока, А ' + str(c0) + '\n'+
               'Сопротивление, Ом ' + str(r0) + '\n')
       'Close .txt file'
       a.close()

