source ~/peda-arm/peda-arm.py
set architecture arm
file ch50
target remote localhost:1234
b *0x00010b0c
b *0x000107cc
b *0x000108ac
