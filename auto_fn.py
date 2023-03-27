def auto_init(model, max_speed):
    return {
        'model': model,
        'speed': 0,
        'max_speed': max_speed,
        'engine': False
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('silnik odpalony')


def stop_engine(car):
    if car['speed'] == 0:
        car['engine'] = False
        print('silnik zgaszony')
    else:
        print('zwolnij wpierw')


def speed_up(car, amount):
    if car['engine']:
        car['speed'] = min(car['speed'] + amount, car['max_speed'])
        print(f'Twoja prędkość to {car["speed"]}')
    else:
        print('odpal silnik wpierw')


def slow_down(car, amount):
    car['speed'] = max(car['speed'] - amount, 0)
    print(f'Twoja prędkość to {car["speed"]}')


fiat = auto_init('Tipo', 240)
bmw = auto_init('e46', 160)
lada = auto_init('niva', 70)

print(bmw)
speed_up(bmw, 20)
start_engine(bmw)
speed_up(bmw, 50)
speed_up(bmw, 150)
speed_up(bmw, 150)
stop_engine(bmw)
slow_down(bmw, 50)
slow_down(bmw, 200)
stop_engine(bmw)
print(bmw)