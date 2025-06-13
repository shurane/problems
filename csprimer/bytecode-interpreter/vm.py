# Constants for opcodes
LOAD = 0x01
STORE = 0x02
ADD = 0x03
SUB = 0x04
HALT = 0xff

# Stretch goals
ADDI = 0x05
SUBI = 0x06
JUMP = 0x07
BEQZ = 0x08


def compute(memory):
    """
    Given a 256 byte array of "memory", run the stored program
    to completion, modifying the data in place to reflect the result

    The memory format is:

    00 01 02 03 04 05 06 07 08 09 0a 0b 0c 0d 0e 0f ... ff
    **        **... __
    ^==DATA===============^ ^==INSTRUCTIONS==============^
    """
    registers = [8, 0, 0]  # PC, R1 and R2

    while True:  # keep looping, like a physical computer's clock
        pc = registers[0]
        op = memory[registers[0]]
        if op == HALT:
            # print(f"{pc}: HALT")
            break

        arg1 = memory[pc+1]
        arg2 = memory[pc+2]
        offset = 3

        if op == LOAD:
            # print(f"{pc}: LOAD: {arg1=}, {arg2=}, {registers[arg1]=} <- {memory[arg2]=}")
            registers[arg1] = memory[arg2]
        elif op == STORE:
            # print(f"{pc}:STORE: {arg1=}, {arg2=}, {registers[arg1]=} -> {memory[arg2]=}")
            memory[arg2] = registers[arg1]
        elif op == ADD:
            # print(f"{pc}:  ADD: {arg1=}, {arg2=}, {registers[arg1]=} -- {registers[arg2]=}, result={registers[arg1] + registers[arg2]}")
            registers[arg1] = (registers[arg1] + registers[arg2]) % 256
        elif op == SUB:
            # print(f"{pc}:  SUB: {arg1=}, {arg2=}, {registers[arg1]=} -- {registers[arg2]=}, result={registers[arg1] - registers[arg2]}")
            registers[arg1] = ((registers[arg1] - registers[arg2]) + 256) % 256
        elif op == ADDI:
            # print(f"{pc}: ADDI: {arg1=}, {arg2=}, {registers[arg1]=} -- {arg2=}, result={registers[arg1] + arg2}")
            registers[arg1] = (registers[arg1] + arg2) % 256
        elif op == SUBI:
            # print(f"{pc}: SUBI: {arg1=}, {arg2=}, {registers[arg1]=} -- {arg2=}, result={registers[arg1] - arg2}")
            registers[arg1] = ((registers[arg1] - arg2) + 256) % 256
        elif op == JUMP:
            # print(f"{pc}: JUMP: {arg1=}")
            offset = 0 # set offset to 0 when we encounter jump
            pc = arg1
        elif op == BEQZ:
            # print(f"{pc}: BEQZ: {registers[arg1]=}, {arg2=}, if offset applied: {(pc + arg2) % 256}")
            if registers[arg1] == 0:
                pc = (pc + arg2) % 256
        else:
            raise ValueError(f"invalid opcode: {op}")

        registers[0] = pc + offset
