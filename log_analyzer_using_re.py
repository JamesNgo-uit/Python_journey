import re

def read_lines(path):
    with open(path) as f:
        return [line.strip() for line in f]
    

FAILED_RE = re.compile(r"Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})")

def count_failed(lines):
    by_ip = {}
    by_user = {}
    for line in lines:
        m = FAILED_RE.search(line)
        if m:
            username, ip = m.groups()
            by_ip[ip] = by_ip.get(ip, 0) + 1
            by_user[username] = by_user.get(username, 0) + 1
    return by_ip, by_user

def top_offenders(counts, n=3):
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:n]

def main():
    path = "auth_sample.log"
    try:
        lines = read_lines(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    by_ip, by_user = count_failed(lines)

    print("Top IPs:")
    for ip, count in top_offenders(by_ip):
        print(f"{ip}: {count}")
    print("Top Users:")
    for username, count in top_offenders(by_user):
        print(f"{username}: {count}")

if __name__ == "__main__":
    main()