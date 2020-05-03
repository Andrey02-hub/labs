# 19. Завдання на взаємодію між класами. Розробити систему «Автобаза».
# Диспетчер розподіляє заявки на Рейси між Водіями і призначає для цього Автомобіль.
# Водій може зробити заявку на ремонт. Диспетчер може відсторонити Водія від роботи. Водій робить відмітку про виконання Рейса і стані Автомобіля.
class Manager:
    def sent_driver_to_trip(self, driver, car, trip):
        driver.trip = trip
        driver.car = car
        print('водій', driver.name, 'відправився в рейс', trip.name, 'на авто', car.name)

class Trip:
    name = ''
    done = False
    def __init__(self, name ):
        self.name = name
        self.done = False

class Car:
    name = ''
    stats = ''
    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

class Driver:
    name = ''
    car = Car('', '')
    trip = Trip('')
    def __init__(self, name):
        self.name = name
        self.car = Car('', '')
        self.trip = Trip(' ')

    def make_fix_request(self):
        print('моє авто ', self.car.name, 'потребує ремонту')

    def make_report(self):
        self.trip.done = True
        print('водій', self.name, 'рейс', self.trip.name, 'завершив, стан авто ', self.car.stats)
        if self.car.stats == 'плохое':
            self.make_fix_request()
        self.trip = Trip(' ')
        self.car = Car('', '')

m = Manager()

m.sent_driver_to_trip(Driver('Анатолій'), Car('ВАЗ', 'плохое'), Trip('трип'))
Driver.make_report()


