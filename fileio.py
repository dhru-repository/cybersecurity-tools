import re
import collections

file = open("access.log", "r+", encoding="utf-8")


def find_unique_ips(input):
    ip_list = []
    lcounter = 0
    file.seek(0)
    for l in file:
        ip = ip_pattern.search(l)
        if ip:
            ip_list.append(ip.group())
            lcounter += 1
    unique_ips = set(ip_list)
    ip_frequency = collections.Counter(ip_list)
    print(ip_frequency.most_common())
    print("Unique ips are -> " + str(len(unique_ips)))


def find_lines_with_words(input):
    lcounter2 = 0
    file.seek(0)
    sub_string = "\\x04\\x01\\x00P\\xC6\\xCE\\x0Eu0\\x00"
    for l in file:
        if l.__contains__(sub_string):
            # print(l)
            lcounter2 += 1
    print("Number of lines that contain \"" + sub_string + "\" -> " + str(lcounter2))


total_lines = len(file.readlines())
print("Total lines in " + file.name + " -> " + str(total_lines))

ip_pattern = re.compile(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")

find_lines_with_words(file)

file.close()
