#14.7
# class House:
#      def __init__(self, flats_amount):
#           self.flats_amount = flats_amount
#
#      def guard (self):
#           print(f'в доме есть вахтёрша')
#
# if __name__ == '__main__':
#      flats = House(110)
#      flats.guard()
#      print(flats.__dict__)
###  ЗДЕСЬ НЕ ПОЛУЧИЛОСЬ У МЕНЯ ПРОПИСАТЬ ТЕКСТОМ В ПРИНТЕ

#14.8, 14.9
class Houses:
     pass
class Salon:
     def __init__(self, manicure, haircut):
          pass
          # self.manicure = manicure
          # self.haircut = haircut
class BeautySalonMixin(Salon, Houses):
     def salon_opening_hours(self, open_time, close_time):
          current_time = int(input('Сколько сейчас времени: '))
          if current_time > open_time and current_time < close_time:
               print('Салон открыт')
          else:
               print('Салон закрыт')

if __name__ == '__main__':
###