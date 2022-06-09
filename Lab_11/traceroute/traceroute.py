import socket
import struct
import time

BASE = 16
BASIC_BYTES = 2
MAX_BYTES = 2 ** BASE - 1
MAXTTL = 63
IP_HEADER_SIZE = 20

def compute_checksum(data):
    checksum = 0
    for i in range(0, len(data), BASIC_BYTES):
        checksum += int.from_bytes(data[i:i + BASIC_BYTES], 'little')
    while checksum & MAX_BYTES != checksum:
        checksum = (checksum >> BASE) + (checksum & MAX_BYTES)
    return MAX_BYTES ^ checksum

def verify_checksum(data):
    return compute_checksum(data) == 0

def get_result(address, host):
    if address is not None:
        name = ''
        try:
            gethost = socket.gethostbyaddr(address[0])
            if len(gethost) > 0:
                name = gethost[0]
        except:
            name = ''
        print("Name:", f'{name}', f'[{address[0]}]')
        if address[0] == host:
            return True
    else:
        return False
    return False

def ping(host, sock, ttl, timeout, reqs):
    addr = None
    print(f'Time To Live: {ttl}')
    for _ in range(reqs):
        try:
            initial_header = struct.pack("bbHHh", 8, 0, 0, ttl, 1)
            checksum = compute_checksum(initial_header)
            header = struct.pack("bbHHh", 8, 0, checksum, ttl, 1)
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, ttl)
            sock.sendto(header, (host, 1))
            start_time = time.time()
            sock.settimeout(timeout)
            recv_packet, temp = sock.recvfrom(1024)

            if recv_packet is not None:
                payload = recv_packet[IP_HEADER_SIZE:]
                if not verify_checksum(payload):
                    print('Checksum is wrong.')
                icmp = recv_packet[20:28]
                type, _, checksum, pid, _ = struct.unpack('bbHHh', icmp)
                if pid == id and type != 0:
                    print('ICMP error.')
                diff = int((time.time() - start_time) * 1000.00)
                print(f'\t{diff}  ms')
            if temp is not None:
                addr = temp
        except socket.timeout:
            print('\tTimed out.')
        return get_result(addr, host)


def traceroute(host, reqs, timeout):
    try:
        addr = socket.gethostbyname(host)
    except socket.gaierror:
        print('Invalid destination')
        return
    print(f'Traceroute to {addr}', f'{host}')
    for ttl in range(1, MAXTTL + 1):
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname('icmp'))
        if (ping(addr,  icmp_socket, ttl, timeout, reqs)):
            icmp_socket.close()
            break
        icmp_socket.close()


if __name__ == '__main__':
    traceroute('yandex.ru', 2, 1)