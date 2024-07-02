import eel
from math import cos,sqrt
def analyze(car_list: list[list[str]]):
    text = ''
    list_t = []
    for car in car_list:        
        list_t.append(f'Автомобиль {car[3]} по адресу {round(float(car[0]),5)},{round(float(car[1]),5)}. Сигнал -- {"нет" if car[2]=="" else car[2]}\n')
        
    list_t.append('\n\n')
    for num,car in enumerate(car_list):
        for scar in car_list[num+1:]:
            list_t.append(f"Между {car[3]} и {scar[3]} -- {long(car, scar)} км\n")
    list_t.append('\n')
    return ''.join(list_t)

def long(point_A,point_B): # определние расстояния между машинами
    point_A = list(map(float,point_A[:2]))
    point_B = list(map(float,point_B[:2]))
    AD = abs(point_A[1] - point_B[1]) * 111.3 * cos(point_B[0])
    BC = abs(point_A[1] - point_B[1]) * 111.3 * cos(point_A[0])
    AB = abs(point_A[0] - point_B[0]) * 111.1
    AH = abs(AD - BC) / 2
    BH = sqrt(abs(AB ** 2 - AH ** 2))
    HD = abs(AD - AH)
    BD = sqrt(BH ** 2 + HD ** 2)
    return round(BD,3)

@eel.expose
def get_file(file:str):
    car_list = file.split('\n')[1:]
    for num, car in enumerate(car_list):
        car_list[num] = car.split(';')
    return analyze(car_list)
    
if __name__ == '__main__':
    with open('Moscow.cor','r',encoding='UTF-8') as f:
        file = f.read()
        # car_list = file.split('\n')
        # del car_list[0]
        # for num,car in enumerate(car_list):
            
        #     car_list[num] = car.split(';')
        # analyze(car_list)
        # print(get_file(file))
    eel.init('web')
    eel.start('main.html',size=(800,800),mode='edge')
    