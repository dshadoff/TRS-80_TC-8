# TRS-80_TC-8 EPROM Folder

Documents and miscellaneous information related to the EPROM board for the JPC Products TC-8 Tape System for the TRS-80 Model I

## Overview

The TC-8 Cassette system relied on a supervisory program ("UTIL") in order to control the cassette system
and save/load at such high bitrates; initially, this UTIL program wa distributed on a 500 baud cassette,
to be loaded by the user each time they started their Model I, in order to use the higher-speed cassette.
This was a significant trade-off if the goal was simply to load a game and run it.

As a solution to this, JPC Products also made a board which could hold a ROM/EPROM containing the UTIL
program, so that no initial loading time was needed in order to gain access to the UTIL program and its
fast-load functionality; all that was needed was to initialize the EPROM by running a SYSTEM command.

This folder contains as much detailed information as possible on this EPROM board.

## How it was used

The EPROM board was designed to be mounted as a second layer to the main board, with the ribbon cable
from the Model I's expansion connector having two female connectors on the JPC side - one for the
communications board, and one for the EPROM board (which was always optional).

Based on the reverse-engineered schematic diagram, the EPROM board exposed the contents of the 2KB
EPROM in the memory range from 3000H through to 37BFH (with a cut-out, disabling the last 40H bytes
of the EPROM).

### How To Start

Like any machine-language program, starting the program by stating the memory location to jump to
is as follows:

> SYSTEM<ENTER>
> 
> *? /(address in decimal)<ENTER>

#### Main entry point

The main entry point, which registers the extended BASIC commands and makes the high-speed cassette functions
available, as well as instantiating keyboard debounce functionality is at 3000H.

The decimal version of the address is 12288

#### Second entry point

The alternate entry point, which just registers the extended BASIC commands and makes the high-speed cassette functions
available (without keyboard debounce functionality), is at 3002H.

The decimal version of the address is 12290

## KiCAD_schematic Folder

I am not aware of a schematic published by JPC Products for the EPROM daughterboard, but through
examination, a schematic diagram has been derived, and input into KiCAD, in order to study how it
works. The reverse-engineering of thes schematic appears correct and complete, but still needs
to be reviewed to catch any possible errors.

At this time, a PC Board layout has not been created in order to recreate the board.


## Contents:

| Name | Description |
| ---- | ----------- |
| []() |  |
| []() |  |
| []() |  |
| []() |  |

