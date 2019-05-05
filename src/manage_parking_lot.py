import sys
from src.constants import MESSAGE_NO_PARKING, MESSAGE_INVALID_SLOT, MESSAGE_INVALID_CREATE, MESSAGE_INVALID_SEARCH, \
    COMMAND_CREATE_LOT, COMMAND_DEALLOCATE, COMMAND_FIND_BY_COLOR, COMMAND_PARK, COMMAND_SLOTS_BY_COLOR, \
    COMMAND_SLOTS_BY_NUMBER, MESSAGE_INVALID_INPUT, COMMAND_STATUS, MESSAGE_NOT_FOUND
from src.utility import print_wrapper, load_file_commands, write_to_file


class ParkingLot:
    """
    Class that performs actions for parking lot
    """
    def __init__(self):
        self.available_slots = list()

    def create_parking_lot(self, max_slots):
        """
        Create empty slots in parking by given number of slots by user
        :param max_slots: Maximum number of slots to be created
        :return: String
        """
        if len(self.available_slots) == 0:
            self.available_slots.extend([None] * int(max_slots))
            return 'Created a parking lot with {0} slots'.format(len(self.available_slots))
        else:
            return MESSAGE_INVALID_CREATE

    def allocate_slot(self, car_number, car_color):
        """
        Allocate slot to a car with given number and color
        :param car_number: Car number
        :param car_color: Car color
        :return: String
        """
        if self.check_slot_availability():
            available_slot = self.available_slots.index(None)
            self.available_slots.pop(available_slot)
            self.available_slots.insert(available_slot, self.generate_car_info(car_number, car_color))
            return 'Allocated slot number: {0}'.format(available_slot + 1)
        else:
            return MESSAGE_NO_PARKING

    def deallocate_slot(self, slot_position):
        """
        Deallocate slot by given slot number
        :param slot_position: Slot number of car
        :return: String
        """
        if int(slot_position) <= len(self.available_slots):
            slot = int(slot_position) - 1
            self.available_slots.pop(slot)
            self.available_slots.insert(slot, None)
            return 'Slot number {0} is free'.format(slot_position)
        else:
            return MESSAGE_INVALID_SLOT

    def check_slot_availability(self):
        """
        Check if the slot is available
        :return: Boolean
        """
        return True if None in self.available_slots else False

    def get_current_status(self):
        """
        Get current status of all slot positions
        :return: String
        """
        parked_cars = [' '.join([str(slot+1), x['number'], x['color']])
                       for slot, x in enumerate(self.available_slots) if x]
        return '\n'.join(parked_cars)

    def find_cars_by_color(self, color):
        """
        Find car's number by a specific color
        :param color: Color given by user
        :return: String
        """
        result = [x['number'] for x in self.available_slots if x and x['color'].lower() == str(color).lower()]
        if len(result) == 0:
            return MESSAGE_INVALID_SEARCH
        else:
            return ', '.join(result)

    def find_slots_by_color(self, color):
        """
        Find slots by car's color
        :param color: Color given by user
        :return: String
        """
        result = [str(slot+1) for slot, x in enumerate(self.available_slots)
                  if x and x['color'].lower() == str(color).lower()]
        if len(result) == 0:
            return MESSAGE_INVALID_SEARCH
        else:
            return ', '.join(result)

    def find_slots_by_number(self, number):
        """
        Find car's slot by number
        :param number: Number given by user
        :return: String
        """
        result = [slot for slot, x in enumerate(self.available_slots)
                  if x and x['number'].lower() == str(number).lower()]
        if len(result) == 0:
            return MESSAGE_NOT_FOUND
        else:
            return str(result[0] + 1)

    @staticmethod
    def generate_car_info(number, color):
        return dict(number=number, color=color)


class ManageParkingLot(ParkingLot):
    """
    Class inherited from ParkingLot for managing and separating the running command logic
    """
    def __init__(self):
        self.interactive = False
        super().__init__()

    def interactive_mode(self):
        """
        Method for interactive mode running endlessly until 'exit' command is supplied
        :return: None
        """
        self.interactive = True
        cli_input = input("INPUT:\n")
        if len(self.available_slots) == 0:
            print_wrapper(self.initiate_parking_lot(cli_input.split()))

        while True:
            input_with_args = input("INPUT:\n")
            print_wrapper(self.execute_commands(input_with_args))

    def file_mode(self, input_file, output_file):
        """
        Method for file mode when user supply both Input and Output file
        :param input_file: Input filename given by user
        :param output_file: Output filename given by user
        :return: None
        """
        commands = load_file_commands(input_file)
        output = list()
        output.append(self.initiate_parking_lot(commands[0].split()))
        output.extend([str(self.execute_commands(x)) for x in commands[1:]])
        write_to_file(output_file, '\n'.join(output))

    def initiate_parking_lot(self, commands):
        """
        Check if the parking lot is not created initially. If yes then prompt user to create it first or exits
        unsuccessfully when running in file mode
        :param commands: List containing command with arguments
        :return: String
        """
        if COMMAND_CREATE_LOT in commands and len(commands) >= 2 and commands[1].isalnum():
            message = self.create_parking_lot(commands[1])
        elif self.interactive:
            message = 'Invalid Command. Create slot first'
            print_wrapper(message)
            self.interactive_mode()
        else:
            print_wrapper('Invalid Command. Create slot first')
            sys.exit(1)
        return message

    def execute_commands(self, command):
        """
        Method for executing command only
        :param command: List containing command with arguments
        :return: String
        """
        cli_action = command.split()
        if COMMAND_PARK in cli_action and len(cli_action) >= 3:
            message = self.allocate_slot(car_number=cli_action[1], car_color=cli_action[2])
        elif COMMAND_DEALLOCATE in cli_action and len(cli_action) == 2:
            message = self.deallocate_slot(cli_action[1])
        elif COMMAND_FIND_BY_COLOR in cli_action and len(cli_action) == 2:
            message = self.find_cars_by_color(cli_action[1])
        elif COMMAND_SLOTS_BY_COLOR in cli_action and len(cli_action) == 2:
            message = self.find_slots_by_color(cli_action[1])
        elif COMMAND_SLOTS_BY_NUMBER in cli_action and len(cli_action) == 2:
            message = self.find_slots_by_number(cli_action[1])
        elif COMMAND_STATUS in cli_action and len(cli_action) == 1:
            message = self.get_current_status()
        elif 'exit' in cli_action and len(cli_action) == 1:
            sys.exit(0)
        else:
            message = MESSAGE_INVALID_INPUT
        return message
