#!/usr/bin/python3
# -*- coding: UTF-8, tab-width: 4 -*-
#
#   !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!!
#   !! AUTO-GENERATED FILE !! DON NOT EDIT DIRECTLY !!
#   !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!!
#
#   Instead, edit the template (build/maike.tpl.py)
#   and re-run the generator (build/maike.gen-py-files.sh)
#
#@  { "targets": [
#@      { "name": "controlcodes.hpp",
#@        "dependencies": [
#@          { "rel": "misc", "ref": "data/control_codes.csv" },
#@          { "rel": "misc", "ref": "compile.py" }
#@          ]
#@        }
#@      ]
#@  }

import compile
compile.compile_guess_data_file(__file__)
