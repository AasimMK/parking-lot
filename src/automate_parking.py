import os
import sys
from src.constants import COMMAND_CREATE_LOT, COMMAND_DEALLOCATE, COMMAND_FIND_BY_COLOR, COMMAND_PARK, \
    COMMAND_SLOTS_BY_COLOR, COMMAND_SLOTS_BY_NUMBER, MESSAGE_INVALID_INPUT
from src.parking_lot import ParkingLot
from src.utility import print_wrapper


def main():
    system_args = sys.argv
    parking_lot = ParkingLot()
    if len(system_args) == 1 and system_args[0] == os.path.realpath(__file__):
        cli_input = input("INPUT:\n")
        command = cli_input.split()
        if COMMAND_CREATE_LOT in command and len(command) >= 2 and command[1].isalnum():
            message = parking_lot.create_parking_lot(command[1])
            print_wrapper(message)
        else:
            print('Invalid. Create slot first')
            main()

        while True:
            input_with_args = input("INPUT:\n")
            cli_action = input_with_args.split()
            if COMMAND_PARK in cli_action and len(cli_action) >= 3:
                message = parking_lot.allocate_slot(car_number=cli_action[1], car_color=cli_action[2])
            elif COMMAND_DEALLOCATE in cli_action and len(cli_action) == 2:
                message = parking_lot.deallocate_slot(cli_action[1])
            elif COMMAND_FIND_BY_COLOR in cli_action and len(cli_action) == 2:
                message = parking_lot.find_cars_by_color(cli_action[1])
            elif COMMAND_SLOTS_BY_COLOR in cli_action and len(cli_action) == 2:
                message = parking_lot.find_slots_by_color(cli_action[1])
            elif COMMAND_SLOTS_BY_NUMBER in cli_action and len(cli_action) == 2:
                message = parking_lot.find_slots_by_number(cli_action[1])
            # elif 'exit' in cli_action and len(cli_action) == 1:
            #     sys.exit(0)
            else:
                message = MESSAGE_INVALID_INPUT
            print_wrapper(message)
    else:
        # Todo: Condition if the user initiated file mode
        pass


if __name__ == '__main__':
    main()
