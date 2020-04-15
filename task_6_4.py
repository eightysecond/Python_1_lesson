class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал(а) движение'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} двигается направо'

    def turn_left(self):
        return f'{self.name} двигается налево'

    def show_speed(self):
        return f'У автомобиля {self.name}, текущая скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'У автомобиля town car {self.name}, текущая скорость {self.speed}')

        if self.speed > 60:
            return f'Превышение скорости'
        else:
            return f'Допустимая скорость'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'У автомобиля work car {self.name}, текущая скорость {self.speed}')

        if self.speed > 40:
            return f'Превышение скорости'
        else:
            return f'Допустимая скорость'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} это машина полиции'
        else:
            return f'{self.name} это не машина полиции'


toyota = TownCar(80, 'white', 'Toyota', False)
lamborghini = SportCar(220, 'red', 'Lamborghini', False)
hyundai = WorkCar(70, 'blue', 'Hyundai', False)
ford = PoliceCar(170, 'black', 'Ford', True)
print(toyota.show_speed())
print(hyundai.show_speed())
print(ford.police())
print(f'{toyota.go()} а {lamborghini.turn_right()}')
print(f'{hyundai.name} это машина полиции? {hyundai.is_police}')
