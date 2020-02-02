from aoe2de_rms_gen_obj_parser.const import *
from aoe2de_rms_gen_obj_parser.parsers import ParserGeneratingObjects, ParserRMSFile


class GeneratingObjectsParser:
    def __init__(self, path_gen_obj=None, path_rms_file=None,
                 map_size=get_dict_first_key(MAP_SIZE_DICT),
                 map_resources=get_dict_first_key(MAP_RESOURCES_DICT),
                 game_type=get_dict_first_key(GAME_TYPE_DICT)):
        # ### Set Paths
        self._path_gen = path_gen_obj
        self._path_rms = path_rms_file
        # ### Set Map Size, Resources and Type constants
        self._map_size = map_size
        self._map_res = map_resources
        self._game_type = game_type
        # ### Declare Parsers
        self._parser_obj: ParserGeneratingObjects = ParserGeneratingObjects(path_gen_obj)
        self._parser_rms: ParserRMSFile = ParserRMSFile(path_rms_file, [map_size, map_resources, game_type])

    def set_path_gen_obj(self, path_gen_obj):
        self._path_gen = path_gen_obj
        self._parser_obj.set_path(path_gen_obj)

    def set_path_rms_file(self, path_rms_file):
        self._path_rms = path_rms_file
        self._parser_rms.set_path(path_rms_file)

    def set_map_size(self, map_size):
        self._map_size = map_size
        self._parser_rms = ParserRMSFile(self._path_rms, [self._map_size, self._map_res, self._game_type])

    def set_map_resources(self, map_resources):
        self._map_res = map_resources
        self._parser_rms = ParserRMSFile(self._path_rms, [self._map_size, self._map_res, self._game_type])

    def set_game_type(self, game_type):
        self._game_type = game_type
        self._parser_rms = ParserRMSFile(self._path_rms, [self._map_size, self._map_res, self._game_type])

    def run_parsers(self):
        # ### Run the ParserGeneratingObjects to get the Command list
        self._parser_obj.run_parser()
        # ### Run the ParserRMSFile to get the RMS constants
        self._parser_rms.run_parser()
        return self

    def get_result(self) -> str:
        out = ""
        for cmd in self._parser_obj.get_result():
            out += cmd.display(self._parser_rms.get_result())
        return out
