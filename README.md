# OLOP: One-Line &amp; Obfuscated Python

This repository contains useful python modules for one-line and obfuscated python.

```
pip install olop-ShadowLugia650
```

[Wiki](https://github.com/ShadowLugia650/olop/wiki): [FAQ](https://github.com/ShadowLugia650/olop/wiki/Frequently-Asked-Questions) and [OLP Tips and Tricks](https://github.com/ShadowLugia650/olop/wiki/OLP-Tips-and-Tricks)

## One-Line Python (OLP)
These files are located within [src/olp](https://github.com/ShadowLugia650/olop/tree/master/src/olp)

### [olp.py](https://github.com/ShadowLugia650/olop/blob/master/src/olp/olp.py): primitives within olp to be imported for olp scripts
```py
__import__("olp", fromlist=["olp"]).olp.primitives
```
includes: one-line while loop, one-line do while loop, inheritance

### [oldec.py](https://github.com/ShadowLugia650/olop/blob/master/src/olp/oldec.py): a one-line python decoder file which can be called from a python script. Common Usage:
```py
globals().update(oldec = __import__("olp", fromlist=["oldec"]).oldec) or oldec.beautify(oldec.parse_recursive("SOME_OLP_STRING"))
```
or, for non olp programmers
```py
from olp import oldec

code = oldec.beautify(oldec.parse_recursive("SOME_OLP_STRING"))
```
NOTE: oldec.py cannot parse all arbitrary one-line python files, as they can take numerous different forms (such as `and` OLP vs `or` OLP), and it looks for specific aspects within some one-line python programs (it doesn't work on itself either) 

### [oldec_cmd.py](https://github.com/ShadowLugia650/olop/blob/master/src/olp/oldec_cmd.py): a one-line python decoding command line utility, for decoding olp outside of a python script. Common Usage:
```
python oldec_cmd.py <olp_file.py> -r -b
```
`python oldec_cmd.py` can also be used to see usage information.

If you've `pip install`ed `olop-ShadowLugia650`, you can also use
```
python -m olp.oldec_cmd <olp_file.py> -r -b
```

## Obfuscated Python
Prototyping this is still a work in progress.
