# IMM-Monitoring
A starter hardware project using the Raspberry Zero is hooking up the Injection Mould Machine I/O Box to the Raspberry GPIO and detecting the machine parameters in Python

## Hardware Design
Design IO Box to getting the Machine parameter with 24V data signal that are need to convert to 3.3V for Rasp Pi

### Concept design
Design1:
  1. Voltage divider
  2. Opto couple

Design2:
  1. Apply Logic level Shifter. There are 2 components used for this, ie Transistor BSS138 and R10K

