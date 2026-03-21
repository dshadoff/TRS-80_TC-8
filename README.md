# TRS-80_TC-8
Information about JPC Products TC-8 Tape System for the TRS-80 Model I

## Introduction

In 1980, The TRS-80 Model I computer was capable of 500 baud cassette storage
from its Level II BASIC ROM.  This was quite slow (although not as slow as the
250 baud in its Level I BASIC ROM)

While floppy disks were available - and were also much faster than cassette - they
required the additional purchase of an Expansion Interface as well as at least one
floppy drive; the cost of these two things totalled more than the orgiinal computer,
so many people couldn't justify such a cost.

As a result, there were multiple companies who created many different ways of
improving cassette I/O speed. JPC Products was one such company, with their TC-8
cassette system.

## Overview

The TC-8 cassette system was a combination of software and hardware which reportedly
improved cassette I/O speeds to 2900 baud - a nearly 6-fold improvement !

The hardware consisted of a box which connected to the expansion port, which managed
both audio output/input, and the motor(s) of the casssette drive(s) - it could control
two cassette drives, which would otherwise have required the Expension Interface.

The software was a utility which needed to be loaded into the computer at start-up;
it needed to be loaded via the orginal cassette interface at 500 baud, so this was
an inconvenience which limited the value of the TC-8 unit.

In time, JPC products released an EPROM board which held a version of the UTIL program,
so that it would not need to be loaded from cassette, and could be executed at startup
with a simple SYSTEM command.

## This Repository

In this repository, I aim to recover as much information as possible about this device
and how it functioned - for users, historians, and researchers wishing to understand
the technology of the late 1970s and early 1980s.

### Cassette Folder

In this folder, I will archive all cassette recordings I can locate, and conversions to
*.CAS format (where applicable), so that they can be loaded by modern emulators or
recreated as sound via modern sources.

Where possible, I will also try to locate TC-8 format recordings so that they can also
be analyzed.

Commented disassemblies may follow at some point for any programs which operate the
TC-8 device (except UTIL, for which the latest known version is covered in the EPROM
folder).


### Documents Folder

In this folder, I will archive all of the documents available which originally came on paper:
- Assembly instructions
- Usage instructions
- Schematic diagrams
- Advertising materials
etc.

### EPROM Folder

In this folder, I will archive all information about the EPROM board and the contents of the
TC-8 EPROM, including a commented disassembly of how it worked (work in progress).

