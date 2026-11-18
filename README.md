# Log analyzer 

A small Python script that reads an SSH authentication log and reports the IP addresses and usernames with the most failed login attempts. IPs with 4 or more failures are flagged with `[Alert]`, which is a simple way to spot brute-force attempts.

## Features

- Extracts the username and source IP from `Failed password` lines using a regular expression
- Handles `invalid user` lines (for example, attempts against accounts that don't exist)
- Counts failures per IP and username with `collections.Counter`
- Flags IPs at or above a configurated threshold (`ALERT_THRESHOLD`, 4)
- Accepts the log file path and number of results from the command line
- Prints a clear message for a missing file or invalid arguments

## Requirements 

- Python 3.8 or newer
- No third-party packages (standard library only)

## Usage

```
python log_analyzer_using_re.py <logfile> [top_n]
```

- `<logfile>`: path to the auth log
- `[top_n]`: optional, how many results to show in each section (default: 3)

## Examples:
 
```
python log_analyzer_using_re.py auth_sample.log
python log_analyzer_using_re.py auth_sample.log 5
```

## Sample output
 
Running it on the included `auth_sample.log`:
 
```
Top IPs:
[ALERT] 203.0.113.5: 4
192.0.2.44: 3
198.51.100.99: 1
Top Users:
root: 4
admin: 2
test: 1
```

## How it works

1. `read_lines` reads the file and strips trailing newlines.
2. `count_failed` matches each line against this pattern.
```
Failed password for (?:invalid user )?(\w+) from (\d{1,3}(?:\.\d{1,3}){3})
```
   The two capture groups are the username and the IP address.
3. Two `Counter` objects keep the totals, and `.most_common(top_n)` gives the top results.

## Notes and limitations

- The IP pattern is simplified: it would also accept values like `999.999.999.999`. That's acceptable for log triage but not for strict validation.
- Only IPv4 addresses and OpenSSH-style `Failed password` messages are recognized.
- The sample IPs come from reserved documentation ranges (RFC 5737), so the sample log contains no real addresses.

## What I learned 

- Lists, dictionaries, and tuple unpacking
- Regular expressions, including capture groups and non-capturing groups 
- Reading files, handling errors with `try/except`, and reading arguments with `sys.argv`
- Using `collections.Counter` instead of manual counting 