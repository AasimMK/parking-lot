import os
import sys
sys.path.append(os.path.dirname(os.getcwd()))
from src.constants import MESSAGE_INVALID_INPUT
from src.manage_parking_lot import ManageParkingLot
from src.utility import print_wrapper


if __name__ == '__main__':
    system_args = sys.argv
    manage_parking_lot = ManageParkingLot()
    if len(system_args) == 1:
        manage_parking_lot.interactive_mode()
    elif len(system_args) == 3:
        input_file_path = os.path.join(os.getcwd(), system_args[1])
        output_file_path = os.path.join(os.getcwd(), system_args[-1])
        manage_parking_lot.file_mode(input_file_path, output_file_path)
    else:
        print_wrapper(MESSAGE_INVALID_INPUT)
