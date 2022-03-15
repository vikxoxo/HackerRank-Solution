"""
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

An identification number for devices connected to the internet. An IPv4 addresses written in dotted quad notation consists of four 8-bit integers separated by periods.

In other words, it's a string of four numbers each between 0 and 255 inclusive, with a "." character in between each number. All numbers should be present without leading zeros.

Examples:

192.168.0.1 is a valid IPv4 address
255.255.255.255 is a valid IPv4 address
280.100.92.101 is not a valid IPv4 address because 280 is too large to be an 8-bit integer (the largest 8-bit integer is 255)
255.100.81.160.172 is not a valid IPv4 address because it contains 5 integers instead of 4
1..0.1 is not a valid IPv4 address because it's not properly formatted
17.233.00.131 and 17.233.01.131 are not valid IPv4 addresses because they contain leading zeros
"""
def solution(inputString):
    l = inputString.split('.')
    flag = True
    if len(l) == 4:
        
        for i in l:
            if i.isdigit() and len(i)>0:
                if int(i)>255:
                    flag = False
                    break
                else:
                    il = list(i)
                    if il[0]=='0' and len(il)>1:
                        flag = False
                        break
            elif len(i)<1:
                flag = False
            elif (i.isdigit())!=True:
                flag = False
    else:
        flag = False
    return flag
 
def solution2(s):
"""
will fail when input = inputString: "0.001.90.87"
"""
    p = s.split('.')

    return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)
