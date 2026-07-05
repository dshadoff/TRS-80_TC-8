# TRS-80_TC-8 Theory Folder

## Background

Cassette tapes were chosen as a recording medium in the late 1970s because of how common and inexpensive they
had become by then - NOT because of their fidelity or recording quality.

### Problems with cassettes:

**Frequency Response**: While cassettes were beginning to become HiFi/stereo equipment around this time,
the units they chose for computers were portable low-cost units with much lower fidelity. And people were
interested in buying the least expensive casssettes that would work. Assume, for minimum standards, a
slightly better frequency response than AM radio: perhaps 40Hz-10,000Hz.

**Dropouts**: Inconsistent application of the ferric oxide particles often caused volume level variations
during playback.

![Picture of a dropout](../images/TRS-80-Mod1_TC-8_Dropout.JPG)


### Background Noise

Along with the limitations in frequency response, the amplifier stage in the cassette recorder may have a
certain level of noise during ampliification. Noise is also dependent on the actual recording and playback
levels - lower reqording levels could have a perceptible background noise level, whereas higher recording
and playback levels may seem to have a lower level of background noise. But too much amplification could lead
to distortion (also noise, but a differnt type).

### Dropouts

Cassette tapes of this era were not always 100% consistent with how the magnetic particles were applied (or
how well they stayed attached to the tape). It was not uncommon for tapes - especiall lower-quality tapes - to
have vaolume levels which suddenly dropped for no apparnet reason (and then recovered).


### 60Hz Line Hum


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

| Bytes | Usage | Description |
|-------|-------|-------------|
| -- | Lead-In | The lead-in consists of 0x2000 iterations of '0' bits (long halfwave) - just over 3 seconds. This is followed by a single short halfwave as a sync bit. |
| 01-02 | Sync Bytes | The lead-in is followed by a sync byte of 0xB3 ('Byte 01'), and then a follow-up byte of 0x9D ("Byte 02"), to ensure that the following data is actually a file that can be trusted.  If either of these bytes is read in with a different value, the reading program will simply revert back to trying to read in the lead-in from the start (a long train of zeroes terminated by a short half-wave).<P>It is important to note that there is an additional bit (a '0' or long halfwave) following each byte in the file, as there are some calculations which need to take place following each byte, which would likely exceed the time needed to detect a short halfwave, potentially causing a misread.  This additional bit is essentially made to be ignored and thrown away. |
| 03 | File Type | The next byte to be read identifies which type of file it is:<br>0x24 = BASIC<br>0x25 = BINARY/Machine-language<br>0x26 = Source Code (i.e. EDTASM source) |
| 04-11 | Filename | The filename for the file on tape can be up to 8 characters in length, stored in ASCII, and with trailing spaces if the name is shorted than 8 characters. |
| 12 | Zero Byte | Byte 12 is intended to be a zero.  Perhaps this is intended to act as a filename terminator (unclear). |
| 13-14 | Start Address | These two bytes are stored in LSB / MSB order and hold the starting address of the program, where the first byte of the payload should be loaded. |
| 15-16 | End Address | These two bytes are stored in LSB / MSB order and hold the ending address (or final address) of the program, where the last byte of the payload should be loaded. |
| 17-18 | Entry Address | These two bytes are stored in LSB / MSB order and hold the entry address of the program, where the user should jump to, in order to start running the program. |
| 19 | Checksum | This byte is used to compare against a running tally of the bytes so far, in order to validate whether there have been any errors during reading/writing.<p> The checksum is calculated by adding the values of bytes #2 through #18, and using only the least-significant byte of this sum for comparison against the checksum. |





