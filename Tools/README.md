# TRS-80_TC-8 Tools Folder

Tools for reading tapes written by the TC-8 Tape System for the TRS-80 Model I

## Overview

I was able to locate some tapes I had created using TC-8 back in the early 1980s,
and wanted to investigate the recording format, and why it was so superior to the
native TRS-80 format.

(For a deeper dive into that, more information will appear later)

Based on a partial disassembly of the TC-8 UTIL program, the schematic diagram of the
TC-8 board, and some cassette recordings, I was able to piece together enough
information to decode binary (machine language) files.

I wrote a program in Python to be able to decode WAV files and display output
of the data contained therein.

You can find more information about the actual tape encoding in the [Theory_of_Operation](Theory_of_peration.md) file.


### Prerequisites:

The TC-8 cassette recording must be recorded into a WAV file, using an audio program;
something like 'Audactiy' will work fine.

The program currently only supports WAV files with the following parameters:
* 44100 samples per second (like a CD)
* Mono (1-channel) recording
* 16-bit samples

Files like this should be easy to create, but I may add support for stereo files in the future.

### Supported file types:

While the TC-8 supported files of 3 types, they have not all been tested yet.
TC-8 supports the following file types:
* BINARY (SUPPORTED)
* BASIC (NOT YET SUPPORTED/TESTED)
* SOURCE (NOT YET SUPPORTED/TESTED)

### Command-line:

The program can be invoked by using:
```
python readtc8.py <filename>
```

### Output:

Currently, the program only displays the data it reads; it does not currently reformat
it into CAS or other data formats, but that should now be possible for BINARY files, as
all of the relevant data is decoded and displayed.

Both Header and internal data are displayed, byte-by-byte, along with what data is actually
held (at least for binary files).

I have included several "WAV" files and their corresponding output "log" files in this folder
for illustration purposes.


**HEADER INFORMATION is as follows:**
```
PCM
Number of channels: 1
Sample Rate (Hz): 44100
Bytes Per Second: 88200
Bits Per Sample: 16

Found leader and start bit

Byte #01 = 0xB3
Byte #02 = 0x9D
Byte #03 = 0x25 ('%') = type  BINARY

Byte #04-#11 = 0x47 0x41 0x4C 0x41 0x58 0x49 0x41 0x4E  ('GALAXIAN')
Byte #12 = 0x00

Byte #13-#14 = 0x00 0x4B  (START = 0x4B00)
Byte #15-#16 = 0xB0 0x6F  (END   = 0x6FB0)
Byte #17-#18 = 0x23 0x58  (ENTRY = 0x5823)

Byte #19 = 0xEC (checksum, match against 0xEC)
-->o MATCH !
```

This is followed by a data dump of the actual program data.

**PROGRAM DATA (excerpt)**:
```
Found second leader and start bit

Block 2 Byte #01 = 0xB3

0x4B00: 80 80 80 80 BC 83 83 83 8C 80 B0 8C 83 8C B0 80    ................
0x4B10: BF 80 80 80 80 80 B0 8C 83 8C B0 80 BF 80 80 80    ................
     .
     .
     .
0x6F90: 01 0A 07 0A 01 0A 06 0A 01 0A 05 0A 01 0A 04 0A    ................
0x6FA0: 03 0A 02 0A 01 37 81 20 01 37 00 00 FF FF FF FF    .....7. .7......
0x6FB0: 00

Block 2 Final Byte = 0x35  (checksum, match against 0x35)
--> MATCH !

END of FILE. fileptr =  3033724
```

