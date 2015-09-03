# 201301037_cloud_assignments
My assignments for cloud computing :D

Assignment1

A simple python translator that converts 32bit assembly code to 64bit assembly code

To run:

nasm -f elf 32_bit.asm

ld -m elf_i386 -s -o 32_bit 32_bit.o

./32_bit

python translator.py

nasm -f elf64 -o 64_bit.o 64_bit.asm

ld -o 64_bit 64_bit.o

./64_bit

ASSIGNMENT2:
Create a custom topology of Y switches where each switch has two hosts and the switches are connected in a circular fashion.All odd hosts are able to ping each other and all even hosts are able to ping each other.Odd hosts have bandwidth of 1MBPS and all even hosts have a bandwidth of 2MBPS

TO RUN:
sudo python mini.py
