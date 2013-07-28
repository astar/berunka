berunka
=======

Machine learning from astronomical data

extractor
---------

usage: extractor.py [-h] -s SOURCE -c CATEGORY [-o OUTPUT] [-D] [-n NROWS]
                    [-l LINE] [-w WIDTH] [-N]

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        specify input dir

  -o OUTPUT, --output OUTPUT
                        specify output file
  -D, --debug           enter in debugging mode
  -n NROWS, --nrows NROWS
                        limit number of processed files
  -l LINE, --line LINE  Specify spectral line position for range limit
  -w WIDTH, --width WIDTH
                        Specify spectral line range limit
  -N, --names           Include names of the star into result



100A dataset
-------------------
- 158 of each spectra type (1, 5)
- 100A around Halpha(6563A)
- file:data/1_5_100.csv

- how to generate
bin/extractor.py -s data/archive -n 158  -w 100    > data/1_5_100.csv

Whole spectrum dataset
-------------------
- 158 of each spectra type (1, 5)
- whole spectrm (1997 pixels)
- file:data/1_5_100.csv

- how to generate
bin/extractor.py -s data/input/1 -n 158    -c 1  > data/1_5_whole_spectrum.csv


some files have more datapoints. Delete them
--------------------------------------------
 sed -i '307d' archive_1_5_07072013.csv 
 sed -i '533d' archive_1_5_07072013.csv 
 sed -i '1735d' archive_1_5_07072013.csv 
 sed -i '1734d' archive_1_5_07072013.csv 
