import re, sys
from collections import Counter
ALERT_THRESHOLD = 4

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

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer_using_re.py <logfile> [top_n]")
        sys.exit(1)
    path = sys.argv[1]

    try:
        top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    except ValueError:
        print("Usage: python log_analyzer_using_re.py <logfile> [top_n]")
        sys.exit(1)
    
    try:
        lines = read_lines(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
        sys.exit(1)

    by_ip, by_user = count_failed(lines)

    print("Top IPs:")
    for ip, count in by_ip.most_common(top_n):
        prefix = "[ALERT] " if count >= ALERT_THRESHOLD else ""
        print(f"{prefix}{ip}: {count}")

    print("Top Users:")
    for username, count in by_user.most_common(top_n):
        print(f"{username}: {count}")

if __name__ == "__main__":
    main()