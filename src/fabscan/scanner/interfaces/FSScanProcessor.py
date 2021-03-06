__author__ = "Mario Lukas"
__copyright__ = "Copyright 2015"
__license__ = "AGPL"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

from pykka import ThreadingActor


class FSScanProcessorCommand(object):
    START = "START"
    STOP = "STOP"
    CALIBRATE_SCANNER = "CALIBRATE_SCANNER"
    SETTINGS_MODE_OFF = "SETTINGS_MODE_OFF"
    SETTINGS_MODE_ON = "SETTINGS_MODE_ON"
    NOTIFY_HARDWARE_STATE = "NOTIFY_HARDWARE_STATE"
    UPDATE_SETTINGS = "UPDATE_SETTINGS"
    _SCAN_NEXT_TEXTURE_POSITION = "SCAN_NEXT_TEXTURE_POSITION"
    _SCAN_NEXT_OBJECT_POSITION = "SCAN_NEXT_OBJECT_POSITION"
    GET_HARDWARE_INFO = "GET_HARDWARE_INFO"
    GET_CALIBRATION_STREAM = "GET_CALIBRATION_STREAM"
    GET_LASER_STREAM = "GET_LASER_STREAM"
    GET_TEXTURE_STREAM = "GET_TEXTURE_STREAM"

class FSScanProcessorInterface(ThreadingActor):
    def __init__(self, config, settings, eventmanager, imageprocessor, hardwarecontroller):
        super(FSScanProcessorInterface, self).__init__(self, config, settings, eventmanager, imageprocessor, hardwarecontroller)
        pass
