from checksums import get_checksum, verify_checksum

text = b'n;wjbt;wt;lbnw;lkb'
checksum = get_checksum(text)
print("Must be True:", verify_checksum(text, checksum))

text = b'n;wjbt;wt;lbnw;lkb'
checksum = 857603486 # random
print("Must be False:", verify_checksum(text, checksum))

text1 = b'n;wjbt;wt;lbnw;lkb'
text2 = b'n;wjbt;wt;lbnw;lkbb'
print("Must be False:", verify_checksum(text2, get_checksum(text1)))
