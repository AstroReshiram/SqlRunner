# This file loads the configuration from the files.
import json


class Configuration:

    def __init__(self, filename):
        self._file = open(filename)
        self._config = json.load(self._file)
        self._db_settings = self._config['DatabaseSettings']

        # Load authorization tokens
        self.connection_string = self._db_settings['ConnectionString']

    def _str2bool(self, v):
        return v.lower() in ("yes", "true", "t", "1")
