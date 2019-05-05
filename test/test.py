import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from unittest import TestCase, main
from src.manage_parking_lot import ParkingLot


class ParkingLotTest(TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot()
        self.fake_slots = [
            {'number': 'KA01HH1231', 'color': 'White'},
            {'number': 'KA01HH1232', 'color': 'Red'},
            {'number': 'KA01HH1233', 'color': 'Blue'},
            {'number': 'KA01HH1234', 'color': 'White'},
            {'number': 'KA01HH1235', 'color': 'Blue'},
            {'number': 'KA01HH1236', 'color': 'Black'},
            {'number': 'KA01HH1237', 'color': 'Red'},
            {'number': 'KA01HH1238', 'color': 'White'},
        ]

    def test_create_parking_lot(self):
        max_slot = 4
        self.parking_lot.create_parking_lot(max_slot)
        self.assertEqual([None] * max_slot, self.parking_lot.available_slots)

    def test_allocate_slot(self):
        self.parking_lot.available_slots = [None] * 4
        output = 'Allocated slot number: {0}'
        result = self.parking_lot.allocate_slot('KA01HH1231', 'White')
        self.assertEqual(output.format(1), result)
        result = self.parking_lot.allocate_slot('KA01HH1232', 'White')
        self.assertEqual(output.format(2), result)
        result = self.parking_lot.allocate_slot('KA01HH1233', 'Blue')
        self.assertEqual(output.format(3), result)
        result = self.parking_lot.allocate_slot('KA01HH1234', 'White')
        self.assertEqual(output.format(4), result)

    def test_deallocate_slot(self):
        self.parking_lot.available_slots = self.fake_slots
        output = 'Slot number {0} is free'
        result = self.parking_lot.deallocate_slot(2)
        self.assertEqual(output.format(2), result)
        result = self.parking_lot.deallocate_slot(4)
        self.assertEqual(output.format(4), result)

    def test_check_slot_availability(self):
        self.parking_lot.available_slots = self.fake_slots
        self.assertFalse(self.parking_lot.check_slot_availability())
        self.parking_lot.deallocate_slot(3)
        self.assertTrue(self.parking_lot.check_slot_availability())

    def test_get_current_status(self):
        self.parking_lot.available_slots = self.fake_slots
        output = [' '.join([str(index+1), x['number'], x['color']]) for index, x in enumerate(self.fake_slots)]
        self.assertEqual('\n'.join(output), self.parking_lot.get_current_status())

    def test_command_find_cars_by_color(self):
        self.parking_lot.available_slots = self.fake_slots
        output = ', '.join([x['number'] for x in self.fake_slots if x['color'].lower() == 'white'])
        self.assertEqual(output, self.parking_lot.find_cars_by_color('White'))
        output = ', '.join([x['number'] for x in self.fake_slots if x['color'].lower() == 'red'])
        self.assertEqual(output, self.parking_lot.find_cars_by_color('Red'))

    def test_find_slots_by_color(self):
        self.parking_lot.available_slots = self.fake_slots
        output = ', '.join([str(index + 1) for index, x in enumerate(self.fake_slots) if x['color'].lower() == 'blue'])
        self.assertEqual(output, self.parking_lot.find_slots_by_color('Blue'))
        output = ', '.join([str(index + 1) for index, x in enumerate(self.fake_slots) if x['color'].lower() == 'black'])
        self.assertEqual(output, self.parking_lot.find_slots_by_color('Black'))

    def test_find_slot_by_number(self):
        self.parking_lot.available_slots = self.fake_slots
        output = 3
        self.assertEqual(str(output), self.parking_lot.find_slot_by_number('KA01HH1233'))
        output = 6
        self.assertEqual(str(output), self.parking_lot.find_slot_by_number('KA01HH1236'))


if __name__ == '__main__':
    main()
