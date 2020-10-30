import csv
import os


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        couple = os.path.splitext(self.photo_file_name)
        list_ext = ['.jpg', '.jpeg', '.png', '.gif']
        if (couple[1] in list_ext) and (couple[0] != '') and (couple[1] != ''):
            return couple[1]
        else:
            return ''


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl
        try:
            if (body_whl != "") and (body_whl.count("x") == 2):
                [self.body_length, self.body_width, self.body_height] = body_whl.split('x')
                if (self.body_length != "") and (self.body_width != "") and (self.body_height != ""):
                    self.body_length = float(self.body_length)
                    self.body_width = float(self.body_width)
                    self.body_height = float(self.body_height)
                else:
                    self.body_length = float(0)
                    self.body_width = float(0)
                    self.body_height = float(0)
            else:
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)
        except ValueError:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        result = float(self.body_width * self.body_height * self.body_length)
        return result


class SpecMachine(CarBase):
    
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra


def get_car_list(csv_filename):
    with open(csv_filename, 'r') as csv_f:
        car_list = []
        reader = csv.reader(csv_f, delimiter=';')
        next(reader)  # пропускаем заголовок
        for line in reader:
            try:
                if line == []:
                    continue
                elif len(line) == 7:
                    if line[0] == 'car':
                        temp = Car(brand=str(line[1]), passenger_seats_count=int(line[2]), photo_file_name=line[3], carrying=float(line[5]))
                        if (line[1] != '') and (line[2] != '') and (line[5] != '') and temp.get_photo_file_ext() != '':
                            car_list.append(Car(brand=str(line[1]), passenger_seats_count=int(line[2]), photo_file_name=line[3], carrying=float(line[5])))
                        else:
                            continue
                    elif line[0] == 'truck':
                        temp = Truck(brand=str(line[1]), photo_file_name=line[3], body_whl=line[4], carrying=float(line[5]))
                        if (line[1] != '') and (line[5] != '') and temp.get_photo_file_ext() != '':
                            car_list.append(Truck(brand=str(line[1]), photo_file_name=line[3], body_whl=line[4], carrying=float(line[5])))
                        else:
                            continue
                    elif line[0] == 'spec_machine':
                        temp = SpecMachine(brand=str(line[1]), photo_file_name=line[3], carrying=float(line[5]), extra=str(line[6]))
                        if (line[1] != '') and (line[3] != '') and (line[5] != '') and (line[6] != '') and temp.get_photo_file_ext() != '':
                            car_list.append(SpecMachine(brand=str(line[1]), photo_file_name=line[3], carrying=float(line[5]), extra=str(line[6])))
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            except ValueError:
                continue
            except IndexError:
                continue
    return car_list
