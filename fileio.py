import re
import collections

file = open("access.log", "r+", encoding="utf-8")

total_lines = len(file.readlines())
print("Total lines in " + file.name + " -> " + str(total_lines))


pattern = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")

ip_list = []
file.seek(0)
lcounter = 0


for l in file:
    ip = pattern.search(l)
    if ip:
        ip_list.append(ip.group())
        lcounter += 1
        # print(ip.group())
    # print(l)

# for ip in ip_list:
#     print(ip)

unique_ips = set(ip_list)
ip_frequency = collections.Counter(ip_list)
print(ip_frequency.most_common())
# for i in ip_frequency.most_common():
#     print(i)

print("Unique ips " + str(len(unique_ips)))
# print(lcounter)
file.close()
