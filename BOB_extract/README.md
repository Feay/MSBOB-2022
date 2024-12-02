requierments: 
UPIC.mbd from msbob or whatever mdb version 1.1
python 2.7x
more python scripts to strip junk sections from seeemingly invalid files. or 
possibly a hex editor i use XVI32

Unpacker useage: place UPIC.mdb into the same folder as a bobunpack python script, open a command prompt type: python bobunpack_v2.py
wmffixer usage: click the plexer.bat this calls in a loop bobwmffixer python script for every wmf file in that folder then outputs into a new directory called output
		some wmf may need to have this done twice, move the files you want to fix into a new folder and try again. 

IF you can see a thumbnail in windows, then you have valid files. 
Any that do not have thumbnails still have valid data, OR look corrupt.
WHY? i am not sure, however utopia.dll, of msbob, auto genorates thumbnails for viewed items and inserts them into the data base

These will need to be processed by turniciting starting at the begining
of the file to the next wmf header and saving and waiting a few seconds to see if 
windows shows a thmbnail as it scans a file change in the background. THEN trying again.
if that doesn't work, i am not sure, possibly stack adjacent files, in insert mode in your hex editor.

WMF notes: wmf can have mulpltie stacked WMF "files" that make a composite image
if a file doesn't look right there could be a junk section at the begining.

WMF structure:
ALL wmf renders STOP reading the file when they see 
hex: 03 00 00 00 00 00 
the signature at the start of each file, and or section is: 
hex:
D7 CD C6 9A
text:
×ÍÆš

bobunpak v2 and v3 work best..try all three in seperate folders, then open an invlid file and try the above method to make them valid.

EXAMPLE:
strip the frist two sections
3764282bob.WMF
result:
REALbob.WMF
a telephone!


