__author__ = "Mario Lukas"
__copyright__ = "Copyright 2015"
__license__ = "AGPL"
__maintainer__ = "Mario Lukas"
__email__ = "info@mariolukas.de"

import logging
import os
import json
from fabscan.FSConfig import Config
from fabscan.util.FSSingleton import SingletonMixin

class Settings(SingletonMixin):


    def __init__(self, settings=os.path.dirname(__file__)+"/config/default.settings.json", first=True):

        if first:

            with open(settings) as file:
                settings = file.read()

            settings = json.loads(settings)

        def _traverse(key, element):
            if isinstance(element, dict):
                return key, Settings(element, first=False)
            else:
                return key, element


        object_dict = dict(_traverse(k, v) for k, v in settings.iteritems())
        self.config = Config.instance()
        self.__dict__.update(object_dict)


    def saveAsFile(self, filename):

        filename = self.config.folders.scans+filename+"/"+filename+".fab"
        current_settings = self.todict(self.__dict__)
        with open(filename, 'w+') as outfile:
            json.dump(current_settings, outfile)

    def update(self, settings):
        self.threshold = settings.threshold
        self.camera.brightness = settings.camera.brightness
        self.camera.contrast = settings.camera.contrast
        self.camera.saturation = settings.camera.saturation
        self.resolution = settings.resolution
        self.laser_positions = settings.laser_positions
        self.color = settings.color
        self.led.blue = settings.led.blue
        self.led.green = settings.led.green
        self.led.red = settings.led.red


    def todict(self, obj, classkey=None):
        if isinstance(obj, dict):
            data = {}
            for (k, v) in obj.items():
                data[k] = self.todict(v, classkey)
            return data
        elif hasattr(obj, "_ast"):
            return self.todict(obj._ast())
        elif hasattr(obj, "__iter__"):
            return [self.todict(v, classkey) for v in obj]
        elif hasattr(obj, "__dict__"):
            data = dict([(key, self.todict(value, classkey))
                for key, value in obj.__dict__.iteritems()
                if not callable(value) and not key.startswith('_')])
            if classkey is not None and hasattr(obj, "__class__"):
                data[classkey] = obj.__class__.__name__
            return data
        else:
            return obj