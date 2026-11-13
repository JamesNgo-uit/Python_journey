

log_lines = [
    "Nov 10 21:01:03 sshd: Failed password for root from 203.0.113.5",
    "Nov 10 21:01:07 sshd: Failed password for admin from 203.0.113.5",
    "Nov 10 21:02:15 sshd: Accepted password for dung from 198.51.100.7",
    "Nov 10 21:03:42 sshd: Failed password for root from 192.0.2.44",
    "Nov 10 21:03:45 sshd: Failed password for root from 203.0.113.5",
]

failed = {}

for line in log_lines:
    if "Failed password" in line:
        ip = line.split()[-1]  # Get the last element which is the IP address
        failed[ip] = failed.get(ip, 0) + 1  # Increment the count for this IP address

for ip, count in sorted(failed.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip}: {count} failed login attempts")
