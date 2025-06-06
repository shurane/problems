# protobuf uses this internally
# slightly useful tool to compare hex encoding of varint to its decimal
# representation: https://bluecrewforensics.com/varint-converter/
# apache avro uses a variant of this called variable-length zig-zag -- maps from natural numbers to integers
# https://protobuf.dev/programming-guides/encoding/#signed-ints
# a link moosh found on different varint representations: https://dcreager.net/2021/03/a-better-varint/

"""""""""
# decoding 32896 from varint
number: 32896
In [32]: bin(0x808102)
Out[32]: '0b 10000000 10000001 00000010'
              0000000  0000001  0000010 # drop the MSB
              0000010  0000001  0000000 # reverse the order of words
              00000 1000 0000 1000 0000 # reassemble to grab the expected value
"""

def encode(num: int) -> bytes:
    print(f"encode(): num: {num}, binary: {bin(num)}")
    word_list: list[int] = []

    while num > 0:
        # get last 7 bits, and then set msb to true
        encoded_byte = (num & 0b0111_1111) | 0b1000_0000
        word_list.append(encoded_byte)
        print(f"encoded byte: bin={encoded_byte:08b}|dec={encoded_byte}|hex={encoded_byte:02x}")
        num = num >> 7

    # unset msb for the last byte
    word_list[-1] = word_list[-1] & 0b0111_1111

    byte_list: bytes = bytes(word_list)
    print(f"big endian: {word_list}")
    print(f"byte list: {byte_list}")

    return byte_list

encode(150)
encode(127)
encode(32896)
encode(0b1000_0001)
# encode(-1) # should fail

