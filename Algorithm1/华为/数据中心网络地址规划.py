
def ip_to_int(ip_str):
    parts = list(map(int, ip_str.split()))
    return (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]

def int_to_ip(num):
    a = (num>>24) & 0xff
    b = (num>>16) & 0xff
    c = (num>>8) & 0xff
    d = num & 0xff
    return f"{a} {b} {c} {d}"

def main():
    n = int(input())
    itervals = []
    for _ in range(n):
        parts = input().split()
        s_ip = ' '.join(parts[:4])
        e_ip = ' '.join(parts[4:8])
        s = ip_to_int(s_ip)
        e = ip_to_int(e_ip)
        itervals.append((s, e))
    itervals.sort()
    merged = []

    for s, e in itervals:
        if not merged:
            merged.append((s,e))
        else:
            last_s, last_e = merged[-1]
            if s <= last_e:
                new_e = max(last_e, e)
                merged[-1] = (last_s, new_e)
            else:
                merged.append((s, e))
    for s, e in merged:
        print(f"{int_to_ip(s)}{int_to_ip(e)}")

if __name__ == "__main__":
    main()