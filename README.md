# sum_dirac_dfcoef : SUMMARIZE DIRAC DFCOEF COEFFICIENTS

[![sum_dirac_dfcoef_test](https://github.com/kohei-noda-qcrg/sum_dirac_dfcoef/actions/workflows/test.yml/badge.svg)](https://github.com/kohei-noda-qcrg/sum_dirac_dfcoef/actions/workflows/test.yml)

This program provides a utility to summarize the contribution of each atomic orbital per molecular orbital from the [DIRAC](http://diracprogram.org/doku.php) output file that the [*PRIVEC and .VECPRI options](http://www.diracprogram.org/doc/release-22/manual/analyze/privec.html) are used.

## Requirements

- [Python](https://python.org) (version ≧ 3.7)
  - If you don't know how to install python, I recommend you to use [pyenv](https://github.com/pyenv/pyenv)

## Install

```sh
pip install sum_dirac_dfcoef
```

## Usage

### Linux, macOS

You can use this program with the following command!

```sh
# Output to sum_dirac_dfcoef.out
sum_dirac_dfcoef -i DIRAC_OUPUT_FILE_PATH
# Specify output file name with -o option
sum_dirac_dfcoef -i DIRAC_OUPUT_FILE_PATH -o OUTPUT_FILE_NAME
```

(e.g.)

```sh
sum_dirac_dfcoef -i x2c_uo2_238.out
```

### Windows

If you want to use this program on Windows, you can use it with the following command.

```sh
python -m sum_dirac_dfcoef -i DIRAC_OUPUT_FILE_PATH
```

A part of x2c_uo2_238.out (DIRAC output file, ... represents an omission)

```out
...
    **************************************************************************
    ****************************** Vector print ******************************
    **************************************************************************



   Coefficients from DFCOEF
   ------------------------



                                Fermion ircop E1g
                                -----------------


* Electronic eigenvalue no. 17: -5.1175267254674
====================================================
       1  L Ag U  s      -0.0000003723  0.0000000000  0.0000000000  0.0000000000
       2  L Ag U  s      -0.0000008538  0.0000000000  0.0000000000  0.0000000000
       3  L Ag U  s      -0.0000014888  0.0000000000  0.0000000000  0.0000000000
       4  L Ag U  s      -0.0000025924  0.0000000000  0.0000000000  0.0000000000
       5  L Ag U  s      -0.0000043736  0.0000000000  0.0000000000  0.0000000000
       6  L Ag U  s      -0.0000074960  0.0000000000  0.0000000000  0.0000000000
...

*****************************************************
********** E N D   of   D I R A C  output  **********
*****************************************************
...
```

A part of the result (... represents an omission)

```out
Electronic no. 19 E1u -8.88244
B3uUpx        49.99917 %
B2uUpy        49.99917 %

Electronic no. 20 E1u -8.86075
B1uUpz        66.76661 %
B3uUpx        16.05235 %
B2uUpy        16.05235 %
B1uOs(1)       0.54741 %
B1uOs(2)       0.54741 %

Electronic no. 17 E1g -5.11753
B2gUdxz       35.98781 %
B3gUdyz       35.98781 %
AgUdzz        18.54868 %
AgUdxx         4.63717 %
AgUdyy         4.63717 %
AgUs           0.13729 %
...
```

If you use -c or --compress option, you can get a compressed result like this.(one line per MO)

```out
E1u 19 -8.88244 B3uUpx 49.99917 B2uUpy 49.99917
E1u 20 -8.86075 B1uUpz 66.76661 B3uUpx 16.05235 B2uUpy 16.05235 B1uOs(1) 0.54741 B1uOs(2) 0.54741
E1g 17 -5.11753 B2gUdxz 35.98781 B3gUdyz 35.98781 AgUdzz 18.54868 AgUdxx 4.63717 AgUdyy 4.63717 AgUs 0.13729
...
```

This options is useful when you want to use the result in a spreadsheet like Microsoft Excel.

## Options

optional arguments (--input is required)

- -h, --help

  show this help message and exit

- -i FILE, --input FILE

  (required) file name of DIRAC output

- -o OUTPUT, --output OUTPUT

  Output file name. Default: sum_dirac_dfcoef.out

- -c, --compress

  Compress output. Display all coefficients on one line for each MO.  
  This options is useful when you want to use the result in a spreadsheet like Microsoft Excel.

- -t THRESHOLD, --threshold THRESHOLD

  threshold. Default: 0.1 %  
  (e.g) --threshold=0.1 => print orbital with more than 0.1 % contribution

- -d DECIMAL, --decimal DECIMAL

  Set the decimal places. Default: 5  
  (e.g) --decimal=3 => print orbital with 3 decimal places (0.123, 2.456, ...). range: 1-15

- -a, --all-write

  Print all MOs(Positronic and Electronic).

- -p, --positronic-write

  Print only Positronic MOs.

- -v, --version

  Print version and exit

- --debug

  print debug output (Normalization constant, Sum of MO coefficient)

- --no-sort

  Don't sort the output by MO energy

## LICENSE

- LGPL v2.1

## Author

- Kohei Noda
