Age of Empires 2: Definitive Edition RandomMapScript GeneratingObjects Parser
#############################################################################


Parser to extract, from AoE2 DE GeneratingObjects.inc file, the code that would be produced when ran with the constants contained in the RandomMapScript files

Installation
============
.. code-block:: bash

  pip install aoe2de_rms_genobj_parser

Basic usage
===========
.. code-block:: python

  from aoe2de_rms_genobj_parser import GeneratingObjectsParser
  # We instantiate the GeneratingObjectsParser with 2 of the 5 arguments (both are mandatory paths)
  parser = GeneratingObjectsParser("Path/to/GeneratingObjects.inc", "Path/to/SomeRandomMapScript.rms")

  # We must run the parsers each time an attribute is set, in order to update them
  parser.run_parsers()

  # We can now get the result for the parsing (done on the fly, that's why we must use run_parsers() first
  parsed_content = parser.get_result()

Advanced Usage
==============
The class GeneratingObjectsParser can be instantiate with up to 5 arguments.

Two are <<mandatory>> *(they won't have default values)*:

* ``path_gen_obj``, the path of the GeneratingObjects.inc file
* ``path_rms_file``, the path of the .rms file *(like Arabia.rms, Arena.rms ...)*

The three others are <<optional>> *(they have default values)* but must respect defined values:

* ``map_size``, must be a member of ``aoe2de_rms_genobj_parser.const.MAP_SIZE_IDX``
* ``map_resources``, must be a member of ``aoe2de_rms_genobj_parser.const.MAP_RESOURCES_IDX``
* ``game_type``, must be a member of ``aoe2de_rms_genobj_parser.const.GAME_TYPE_IDX``

By default, these are set to ``NORMAL_MAP``, ``DEFAULT_RESOURCES`` and ``RANDOM_GAME``

Because the attributes can be changed at will *(setters exposed)*, the files must be parsed first with ``run_parsers()``
before asking for a result with ``get_result()``

Information about **GeneratingObjects.inc**
====================================================
* Contains the code for the map objects generation, from buildings, to resources, with units and some terrains,
  such as Town Centers, Villagers, Scouts, Stones, Golds, Huntables, Lurables ...

* The previous code is encapsulated in various ``if, elseif, else`` statements.
  Omitting ``else``, they will have their corresponding constraint on a constant defined elsewhere *(the .rms files)*

Information about **RandomMapScript.rms**
==================================================
* Define base Land and Terrain

* Define seasons if needed/wanted

* Define the constants used by the GeneratingObjects.inc file