from unittest import TestCase
from src.manage_parking_lot import ParkingLot


class ParkingLotTest(TestCase):
    def setUp(self):
        self.parking_lot = ParkingLot()
        self.max_slot = 4

    def test_create_parking_lot(self):
        self.parking_lot.create_parking_lot(self.max_slot)
        self.assertEqual([None] * self.max_slot, self.parking_lot.available_slots)

    def test_aa(self):
        self.assertEqual(0, 0, 'ZERO')
