.section .text
.global _start
.code 32
_start:
    ldr r0, =string
    mov r1, #10
    bl write_r0_to_stdout
    blx get_pc

branch:
    mov r7, #0xdf
    mov r0, #1
    mov r1, #42
    mov r2, #42
    mov r3, #0x41
    push {r3}
    mov r3, sp
    svc 0
    mov r0, sp
    mov r1, #1
    bl write_r0_to_stdout
    bl exit

write_r0_to_stdout:
    MOV R7, #4
    MOV R2, R1
    MOV R1, R0
    MOV R0, #1
    SWI 0
    MOV PC, LR

exit:
    MOV R7, #1
    SWI 0

.thumb
.thumb_func
get_pc:
    blx branch

.data
string:
    .ascii "Hey man !\n"
