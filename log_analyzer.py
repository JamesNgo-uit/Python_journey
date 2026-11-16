#Two new concept
#Reading a file
with open("auth_sample.log") as f:
    for line in f:
        print(line.strip())
# open(...) opens the file, and with closes it automatically when the block ends (like RAII in C++).
# Looping over f gives one line at a time.
# .strip() removes the trailing newline \n

#Function
def add(a, b):
    return a + b

print(add(2,3))

# def, a colon, an indented body, and return. There are no type declarations, 
# and a default value looks like def top(counts, n=3).

def read_lines(path):
    with open(path) as f:
        return [line.strip() for line in f] # List Comprehension


def count_failed(lines):
    failed = {}
    for line in lines:
        if "Failed password" in line:
            ip = line.split()[-1]
            failed[ip] = failed.get(ip, 0) + 1
    return failed
    # TODO: build and return a dict {ip: number_of_failed_logins}
    # Hint: this is your first script's loop
    #pass


def top_offenders(counts, n=3):
    
    top_offenders_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return top_offenders_list[:n]
    # TODO: return the n IPs with the highest counts, as (ip, count) pairs
    # Hint: sorted(..., key=lambda ..., reverse=True) and then a slice [:n]
    #pass


def main():
    lines = read_lines("auth_sample.log")
    counts = count_failed(lines)
    for ip, count in top_offenders(counts):
        print(f"{ip}: {count} failed attempts")


if __name__ == "__main__":
    main()
# if __name__ == "__main__": means “run main() only when this file is executed directly, 
# ot when it’s imported by another script.” It’s the Python version of C++’s int main(), 
# and you’ll see it in nearly every script.