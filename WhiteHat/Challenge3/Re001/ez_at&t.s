.global main

main:
    mov $?, %eax
    mov $13, %ebx
    mov $666, %ecx
    mov $0x666,%edx
my_loop:
    test %eax, %eax
    jz check
    push %ebx
    push %ecx
    push %edx
    pop %ebx
    pop %edx
    pop %ecx
    add %edx,%ecx
    add %ecx,%ebx
    add %ebx,%edx
    dec %eax
    jmp my_loop
check:
    cmp $0xcb714b, %ebx
    je goodboy
    mov $0xdead, %eax
    jmp end
goodboy:
    mov $0xbeef, %eax
end:
    ret
