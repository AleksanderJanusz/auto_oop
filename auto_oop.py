class Auto:
    def __init__(self, model, max_speed):
        self.model = model
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('silnik odpalony')

    def stop_engine(self):
        if self.speed == 0:
            self.engine = False
            print('silnik zgaszony')
        else:
            print('zwolnij wpierw')

    def speed_up(self, amount):
        if self.engine:
            self.speed = min(self.speed + amount, self.max_speed)
            print(f'Twoja prędkość to {self.speed}')
        else:
            print('odpal silnik wpierw')

    def slow_down(self, amount):
        self.speed = max(self.speed - amount, 0)
        print(f'Twoja prędkość to {self.speed}')


class Van(Auto):
    def __init__(self, model, max_speed, seats):
        self.seats = seats
        super().__init__(model, max_speed * 0.85 if seats >= 7 else max_speed)


fiat = Auto("Tipo", 240)
bmw = Van('e46', 160, 6)
lada = Auto('niva', 70)

# Auto.speed_up(bmw, 20)
bmw.speed_up(20)
bmw.start_engine()
bmw.speed_up(50)
bmw.speed_up(150)
bmw.speed_up(150)
bmw.stop_engine()
bmw.slow_down(50)
bmw.slow_down(200)
bmw.stop_engine()
