import sys
from src.constants import MESSAGE_INVALID_INPUT
from src.parking_lot import ManageParkingLot
from src.utility import print_wrapper


def main():
    system_args = sys.argv
    manage_parking_lot = ManageParkingLot()
    if len(system_args) == 1:
        manage_parking_lot.interactive_mode()
    elif len(system_args) == 4:
        manage_parking_lot.file_mode(system_args[1], system_args[3])
    else:
        print_wrapper(MESSAGE_INVALID_INPUT)


if __name__ == '__main__':
    main()
