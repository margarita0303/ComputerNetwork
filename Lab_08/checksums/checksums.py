base = 16

def is_pow2(number):
    return (number != 0 and ((number - 1) & number == 0))
    
def get_checksum(data):
    step = base // 8
    summ = 0
    for i in range(0, len(data), step):
        next_number = int.from_bytes(data[i:i+step], 'big')
        summ = (summ + next_number) % (2 ** base)
    return summ ^ (2 ** base - 1)

def verify_checksum(data, checksum):
    step = base // 8
    summ = 0
    for i in range(0, len(data), step):
        next_number = int.from_bytes(data[i:i+step], 'big')
        summ = (summ + next_number) % (2 ** base)
    summ += checksum
    return is_pow2(summ + 1)
