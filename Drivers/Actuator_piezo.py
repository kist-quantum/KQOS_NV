import numpy as np
from pylablib.devices import Thorlabs
import logging
import pyvisa
from tomlkit import load


class actuator:
    def __init__(self, id : str):
        try:
            self.Equipment = Thorlabs.KinesisPiezoMotor(id)
            # Declare each channel
            self.M1_x_pos = self.Equipment.get_position(1)
            self.M1_y_pos = self.Equipment.get_position(2)
            self.M2_x_pos = self.Equipment.get_position(3)
            self.M2_y_pos = self.Equipment.get_position(4)
            self.current_move_channel = 1

            # channels numbers
            self.M1_x = 1
            self.M1_y = 2
            self.M2_x = 3
            self.M2_y = 4
            self.curr_move_channel = 0
            self.enable_channels = ""
        except:
            logging.warning("cant find PIEZO_MOTOR for AUTO ALIGN")

    def get_position(self) -> None:
        # get position
        self.M1_x_pos = self.Equipment.get_position(1)
        self.M1_y_pos = self.Equipment.get_position(2)
        self.M2_x_pos = self.Equipment.get_position(3)
        self.M2_y_pos = self.Equipment.get_position(4)
        return self.M1_x_pos, self.M1_y_pos, self.M2_x_pos, self.M2_y_pos

    def enable_x(self) -> None:
        self.Equipment.enable_channels((1, 2))

    def enable_y(self) -> None:
        self.Equipment.enable_channels((3, 4))

    def wait_move_all(self) -> None:
        self.Equipment.wait_move(channel=self.current_move_channel)

    def move_to_zero(self) -> None:
        self.wait_move_all()
        self.Equipment.move_to(0, channel=1)
        self.Equipment.wait_move(channel=1)
        self.Equipment.move_to(0, channel=2)
        self.Equipment.wait_move(channel=2)
        self.Equipment.move_to(0, channel=3)
        self.Equipment.wait_move(channel=3)
        self.Equipment.move_to(0, channel=4)
        self.Equipment.wait_move(channel=4)

    def move_to(self, channel, position) -> None:
        # config x axis enable
        previous_channel = self.enable_channels
        if channel == 1 or channel == 2:
            self.enable_channels = "X"
        # config y axis enable
        elif channel == 3 or channel == 4:
            self.enable_channels = "Y"

        if self.enable_channels != previous_channel:
            if self.enable_channels == "X":
                self.enable_x()
            elif self.enable_channels == "Y":
                self.enable_y()

        self.Equipment.wait_move(channel=self.curr_move_channel)
        self.Equipment.move_to(channel=channel, postiion=position)

        # update curr move channel
        self.curr_move_channel = channel

    def move_by(self, channel, distance):
        # config x axis enabled
        previous_channel = self.enable_channels
        if channel == 1 or channel == 2:
            self.enable_channels = "X"
        # config y axis enabled
        elif channel == 3 or channel == 4:
            self.enable_channels = "Y"

        if self.enable_channels != previous_channel:
            if self.enable_channels == "X":
                self.enable_x()
            elif self.enable_channels == "Y":
                self.enable_y()

        self.Equipment.move_by(channel=channel, distance=distance)
        self.Equipment.wait_move(channel=self.curr_move_channel)

        self.curr_move_channel = channel

    def move_to(self, channel, position):
        # config x axis enabled
        previous_channel = self.enable_channels
        if channel == 1 or channel == 2:
            self.enable_channels = "X"
        # config y axis enabled
        elif channel == 3 or channel == 4:
            self.enable_channels = "Y"

        if self.enable_channels != previous_channel:
            if self.enable_channels == "X":
                self.enable_x()
            elif self.enable_channels == "Y":
                self.enable_y()

        self.Equipment.wait_move(channel=self.curr_move_channel)
        self.Equipment.move_to(channel=channel, position=position)

        # update curr move channel
        self.curr_move_channel = channel

    def get_enable_channels(self) -> None:
        print(self.EquipMent.get_enabled_channels())

    def close(self):
        self.Equipment.close()
