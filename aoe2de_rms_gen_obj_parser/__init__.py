import argparse

from aoe2de_rms_gen_obj_parser.genobj import (
    GeneratingObjectsParser,
)

if __name__ == '__main__':
    # Can be run from command line with two mandatory arguments `gen_obj_path` and `rms_file_path`
    arg_p = argparse.ArgumentParser(description="Parser for Age of Empire 2: Definitive Edition GeneratingObjects "
                                                "accordingly to the RandomMapScript file provided for the constants",
                                    epilog="")

    arg_p.add_argument("gen_obj_path", metavar="\"Path/to/GeneratingObjects.inc\"",
                       help="Path of the GeneratingObjects.inc file from AoE2DE")
    arg_p.add_argument("rms_file_path", metavar="\"Path/to/.rms file\"",
                       help="List of path of the RMS files to parse")
    # Always optional args
    arg_p.add_argument("-map_resources", "--res", metavar="One of the possible Map Resources",
                       default="DEFAULT_RESOURCES", help="Available attributes are: LOW_RESOURCES, MEDIUM_RESOURCES, "
                                                         "HIGH_RESOURCES, DEFAULT_RESOURCES, RANDOM_RESOURCES, "
                                                         "INFINITE_RESOURCES")
    arg_p.add_argument("-map_size", "--size", metavar="One of the possible Map Sizes", default="NORMAL_MAP",
                       help="Available attributes are: TINY_MAP, SMALL_MAP, MEDIUM_MAP, NORMAL_MAP, LARGE_MAP, "
                            "HUGE_MAP, GIGANTIC_MAP, LUDIKRIS_MAP")
    arg_p.add_argument("-game_type", "--type", metavar="One of the possible Game Types", default="RANDOM_GAME",
                       help="Available attributes are: RANDOM_GAME, KING_OT_HILL, EMPIRE_WARS, BATTLE_ROYALE, "
                            "REGICIDE, DEATH_MATCH, CAPTURE_THE_RELIC, WONDER_RACE, DEFEND_WONDER, SUDDEN_DEATH")
    args_dict = arg_p.parse_args()

    #
    gen_obj_parser = GeneratingObjectsParser(args_dict.gen_obj_path, args_dict.rms_file_path,
                                             args_dict.size,
                                             args_dict.res,
                                             args_dict.type)
    gen_obj_parser.run_parsers()
    print(gen_obj_parser.get_result())
