import ntpath
from typing import List

from aoe2de_rms_genobj_parser.blocks import BlockLine, BlockIf, BlockElseIf, BlockElse, _BlockCMD


class ParserGeneratingObjects:
    """Class to parse the GeneratingObjects.inc file and create a list with the equivalent Blocks
        The result can then be used with the constants from the RMS files to produce the objects the map will use.
    """

    def __init__(self, path=None):
        self._path = path
        self._gen_object = []

    def set_path(self, path):
        self._path = path

    def get_path(self):
        return self._path

    def run_parser(self):
        if self._path is None or self._path == "":
            raise Exception("You must provide the GeneratingObjects.inc file path.")

        ptr_table = self._gen_object
        ptr_block = None
        com_skip = False
        with open(self._path, "r") as fp:
            for line in fp:
                line = line.strip()
                block = None
                update_block = False

                # ### Skippable lines
                if line.startswith("#") or len(line) == 0:
                    # single com
                    continue
                elif line.find("/*") != -1 and line.find("*/") != -1:
                    # inline com /* */
                    if line.startswith("/*"):
                        continue
                elif line.startswith("/*"):
                    # multi-line com start /*
                    com_skip = True
                    continue
                elif line.endswith("*/"):
                    # multi-line com end */
                    com_skip = False
                    continue
                elif com_skip:
                    continue

                if line.startswith("if "):
                    # ### IF ###
                    cond = line.split(" ")[1].strip()
                    block = BlockIf(cond, ptr_block)
                    ptr_table.append(block)
                    update_block = True
                elif line.startswith("elseif "):
                    # ### ELSEIF ###
                    cond = line.split(" ")[1].strip()
                    block = BlockElseIf(cond, ptr_block.precedence)
                    ptr_block.counterPart = block
                    update_block = True
                elif line.startswith("else"):
                    # ### ELSE ###
                    block = BlockElse(ptr_block.precedence)
                    ptr_block.counterPart = block
                    update_block = True
                elif line.startswith("endif"):
                    # ### ENDIF ###
                    if ptr_block.precedence is None:
                        ptr_block = None
                        ptr_table = self._gen_object
                    else:
                        ptr_block = ptr_block.precedence
                        ptr_table = ptr_block.contentList
                else:
                    # ### CONTENT ###
                    block = BlockLine(line)
                    ptr_table.append(block)

                if update_block:
                    ptr_block = block
                    ptr_table = block.contentList

    def get_result(self):
        return self._gen_object


class ParserRMSFile:
    """Parsing Class for the RMS (const) files
        Produce
    """

    def __init__(self, path=None, const_list=None):
        self._path = path
        self._const_list = const_list or []
        self._table_const = []

    def set_path(self, path):
        self._path = path

    def get_path(self):
        return self._path

    def run_parser(self):
        if self._path is None or self._path == "":
            raise Exception("You must provide the GeneratingObjects.inc file path.")

        head, tail = ntpath.split(self._path)
        file_name = tail or ntpath.basename(head)
        # ### Process Const file
        with open(self._path, "r") as fp_read:
            for line in fp_read:
                line = line.strip()
                if line.startswith("#define"):
                    self._table_const.append(line.split(" ")[1])
        # ### Append const_list
        self._table_const += self._const_list

    def get_result(self) -> List[_BlockCMD]:
        return self._table_const
