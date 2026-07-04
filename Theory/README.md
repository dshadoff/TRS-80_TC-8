# TRS-80_TC-8 Theory Folder

## Overview

### Filetypes

### Commands

## Tape Format

### Bit-level Encoding

#### TRS-80 Native Format

#### TC-8 Format

### File Level - BINARY

Binary files are saved as two consecutive blocks, each with it own leader & sync byte:

**BLOCK 1 - HEADER INFO**

1) **Lead-in**:

The lead-in consists of 0x2000 iterations of '0' bits (long halfwave) - just over 3 seconds.
This is followed by a single short halfwave as a sync bit.

2) **Sync Bytes** (Bytes 01-02):

The lead-in is followed by a sync byte of 0xB3 ('Byte 01'), and then a follow-up byte of 0x9D ("Byte 02"),
to ensure that the following data is actually a file that can be trusted.  If either of these bytes is
read in with a different value, the reading program will simply revert back to trying to read in the
lead-in from the start (a long train of zeroes terminated by a short half-wave).

It is important to note that there is an additional bit (a '0' or long halfwave) in-between each byte in the
file, as there are some pointer calculations which need to take place for each byte, which would likely exceed
the time needed to detect a short halfwave, causing a misread.  This additional bit is essentially made to
be ignored and trown away.

3) **File Type** (Byte 3):

The next byte to be read identifies which type of file it is:
* 0x24 = BASIC
* 0x25 = BINARY/Machine-language
* 0x26 = Source Code (i.e. EDTASM source)

4) **Filename** (Bytes 04-11):

The filename for the file on tape canbe up to 8 characters in length, stored in ASCII, and with trailing
spaces if the name is shorted than 8 characters.

5) **Zero Byte** (Byte 12):

Byte 12 is intended to be a zero.  Perhaps this is intended to act as a filename terminator (unclear).

6) **Start Address** (Bytes 13-14):

These two bytes are stored in LSB / MSB order and hold the starting address of the program, where
the first byte of the payload should be loaded.

7) **End Address** (Bytes 15-16):

These two bytes are stored in LSB / MSB order and hold the ending address (or final address) of the
program, where the last byte of the payload should be loaded.

8) **Entry Address** (Bytes 17-18):

These two bytes are stored in LSB / MSB order and hold the entry address of the program, where the
user should jump to, in order to start executing the program.

9) **Checksum** (Byte 19):

This byte is used to compare against a running tally of the bytes so far, in order to validate whether
there have been any errors during reading/writing.

The checksum is calculated by adding the values of bytes #2 through #18, and using only the
least-significant byte of this sum for comparison against the checksum.

Test Table:

| Bytes | Usage | Description |
|-------|-------|-------------|
| -- | Lead-In | The lead-in consists of 0x2000 iterations of '0' bits (long halfwave) - just over 3 seconds. This is followed by a single short halfwave as a sync bit. |
| 01-02 | Sync Bytes | The lead-in is followed by a sync byte of 0xB3 ('Byte 01'), and then a follow-up byte of 0x9D ("Byte 02"), to ensure that the following data is actually a file that can be trusted.  If either of these bytes is read in with a different value, the reading program will simply revert back to trying to read in the lead-in from the start (a long train of zeroes terminated by a short half-wave).<P>It is important to note that there is an additional bit (a '0' or long halfwave) in-between each byte in the file, as there are some pointer calculations which need to take place for each byte, which would likely exceed the time needed to detect a short halfwave, causing a misread.  This additional bit is essentially made to be ignored and trown away.|
| 03 | File Type | The next byte to be read identifies which type of file it is:<br>0x24 = BASIC<br>0x25 = BINARY/Machine-language<br>0x26 = Source Code (i.e. EDTASM source) |
| 04-11 | Filename | The filename for the file on tape can be up to 8 characters in length, stored in ASCII, and with trailing spaces if the name is shorted than 8 characters. |
| 12 | Zero Byte | Byte 12 is intended to be a zero.  Perhaps this is intended to act as a filename terminator (unclear). |
| 13-14 | Start Address | These two bytes are stored in LSB / MSB order and hold the starting address of the program, where the first byte of the payload should be loaded. |
| 15-16 | End Address | These two bytes are stored in LSB / MSB order and hold the ending address (or final address) of the program, where the last byte of the payload should be loaded. |
| 17-18 | Entry Address | These two bytes are stored in LSB / MSB order and hold the entry address of the program, where the user should jump to, in order to start running the program. |
| 19 | Checksum | This byte is used to compare against a running tally of the bytes so far, in order to validate whether there have been any errors during reading/writing.<p> The checksum is calculated by adding the values of bytes #2 through #18, and using only the least-significant byte of this sum for comparison against the checksum. |





