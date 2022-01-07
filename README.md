# olop
OLOP: One-Line &amp; Obfuscated Python

This repository contains useful python modules for one-line and obfuscated python.

One-Line python (olp) files are in ./olp, and include:
 * olp.py: primitives within olp to be imported 
   * `__import__("olp").primitives`
   * includes: one-line while loop, one-line do while loop,
 * oldec.py: a one-line python decoder file which can be called from a python script. Common Usage:
```
globals().update(oldec = __import__("oldec")) or oldec.beautify(oldec.parse_recursive("SOME_OLP_STRING"))
```
or, for non olp programmers
```
import oldec

code = oldec.beautify(oldec.parse_recursive("SOME_OLP_STRING"))
```
 * oldec_cmd.py: a one-line python decoding command line utility, for decoding olp outside of a python script. Common Usage:
```
python oldec_cmd.py <olp_file.py> -r -b
```
`python oldec_cmd.py` can also be used to see usage information.