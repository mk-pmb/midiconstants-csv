﻿
midiconstants-csv
=================

An unofficial MIDI SDK that aims to provide data tables about (General) MIDI
in several formats:
  * CSV: semicolon delimited text files.
  * C++ header files via Python: see the section below.
  * Node.js package: Should work out of the box by reading the CSV files
    synchronously(!!) at `require()` time.
    If you want to use asynchronous module systems, use the JSON version.
  * JSON: You can use the Node.js version to generate a plain JSON file
    and an AMD-wrapped version in the `dist/nonfree/` folder:
    run `nodejs csv2pojo.js --dist-json`


&nbsp;

Batteries not included :-(
--------------------------

This free software edition is a reboot of Torbjörn Rathsman's original
[`midiconstants` project][orig-proj]
and does not include the actual CSV data due to license issues.

Until we can find another source for these, you'll have to download
them yourself. One easy way to do so is to run:

```bash
$ ./build/download-data-files.sh
```


&nbsp;

Data files
----------

The `data/` directory has:
  * `status_codes.csv`: All MIDI status codes.
  * `control_codes.csv`: All control codes for MIDI status `0xB0`.
  * `gm_programs.csv`: The names of all General MIDI programs
    ("instruments", "patches").
  * `gm_drumkit.csv`: The names of all General MIDI percussion sounds.


### Control codes
Control codes less than 32 have a corresponding Least Significant Byte control
code obtained by adding 32 to the Most Significant Byte control code.
Therefore, these are not listed in `control_codes.csv`.


&nbsp;

C++ header files
----------------

(tl;dr: `for PY in *_*.py; do python3 $PY; done; ls dist/nonfree/*.hpp`)

To translate any of the CSV tables into a C++ header file, run its
corresponding `.py`, e.g.:<br>
`python3 -- gm_drumkit.py [dest_dir [src_dir]]`

Both options `dest_dir` (where to put the header files)
and `src_dir` (where to find the CSV) are optional.
If missing, `dest_dir` defaults to `dist/nonfree/` inside the repo
and `src_dir` defaults to guessing, which should result in `data/`.


### Support for the Maike build system

Project using [Maike][maike-about] should be able to auto-detect the paths
for this project and work out-of-the-box.
Thus, all include files can be generated by running Maike from the
top directory of the repo,
and all include files will end up in the `__targets` directory.




&nbsp;

  [orig-proj]: https://github.com/milasudril/midiconstants/
  [maike-about]: https://github.com/milasudril/maike

License
-------

Copyright (c) 2017 Torbjörn Rathsman.<br>
All rights reserved. Released under the [BSD-2-Clause license](LICENSE.txt).

A machine-readable list of contributors is kept in
the `contributors` field of `package.json`.
