import re, sys
from collections import Counter

def read_lines(path):
    with open(path) as f:
        return [line.strip() for line in f]
    

FAILED_RE = re.compile(r"Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})")

def count_failed(lines):
    by_ip = Counter()
    by_user = Counter()
    for line in lines:
        m = FAILED_RE.search(line)
        if m:
            username, ip = m.groups()
            by_ip[ip] += 1
            by_user[username] += 1
    return by_ip, by_user

def top_offenders(counts, n=3):
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_list[:n]

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer_using_re.py <logfile> [top_n]")
        sys.exit(1)
    path = sys.argv[1]

    try:
        lines = read_lines(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        return
    
    by_ip, by_user = count_failed(lines)

    try:
        top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    except ValueError:
        print("Usage: python log_analyzer_using_re.py <logfile> [top_n]")
        sys.exit(1)
    
    print("Top IPs:")
    for ip, count in by_ip.most_common(3):
        if count >= 4:
            print("[ALERT] ", end="")
        print(f"{ip}: {count}")

    print("Top Users:")
    for username, count in top_offenders(by_user, top_n):
        print(f"{username}: {count}")

if __name__ == "__main__":
    main()