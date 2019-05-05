from src.constants import MESSAGE_NO_PARKING, MESSAGE_INVALID_SLOT, MESSAGE_INVALID_CREATE, MESSAGE_INVALID_SEARCH


class ParkingLot:
    def __init__(self):
        self.available_slots = list()

    def create_parking_lot(self, max_slots):
        if len(self.available_slots) == 0:
            self.available_slots.extend([None] * int(max_slots))
            return 'Created a parking lot with {0} slots'.format(len(self.available_slots))
        else:
            return MESSAGE_INVALID_CREATE

    def allocate_slot(self, car_number, car_color):
        if self.check_slot_limit():
            available_slot = self.available_slots.index(None)
            self.available_slots.pop(available_slot)
            self.available_slots.insert(available_slot, self.generate_car_info(car_number, car_color))
            return 'Allocated slot number: {0}'.format(available_slot + 1)
        else:
            return MESSAGE_NO_PARKING

    def deallocate_slot(self, slot_position):
        if int(slot_position) <= len(self.available_slots):
            slot = int(slot_position) - 1
            self.available_slots.pop(slot)
            self.available_slots.insert(slot, None)
            return 'Slot number {0} is free'.format(slot_position)
        else:
            return MESSAGE_INVALID_SLOT

    def check_slot_limit(self):
        return True if None in self.available_slots else False

    def find_cars_by_color(self, color):
        result = [x['number'] for x in self.available_slots if x and x['color'].lower() == str(color).lower()]
        if len(result) == 0:
            return MESSAGE_INVALID_SEARCH
        else:
            return ', '.join(result)

    def find_slots_by_color(self, color):
        result = [slot for slot, x in enumerate(self.available_slots) if x and x['color'].lower() == str(color).lower()]
        if len(result) == 0:
            return MESSAGE_INVALID_SEARCH
        else:
            return result[0] + 1

    def find_slots_by_number(self, number):
        result = [slot for slot, x in enumerate(self.available_slots)
                  if x and x['number'].lower() == str(number).lower()]
        if len(result) == 0:
            return MESSAGE_INVALID_SEARCH
        else:
            return result[0] + 1

    @staticmethod
    def generate_car_info(number, color):
        return dict(number=number, color=color)
