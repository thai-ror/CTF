def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def fermat(n):
    x = isqrt(n) + 1
    y = isqrt(x * x - n)

    while True:
        w = x * x - n - y * y
        if w == 0:
            break
        elif w > 0:
            y += 1
        else:
            x += 1
    return x - y, x + y

c = 0x42e08bb01f0cb9ba959ddcb771eb641afe87b775adfee9e02f9941d6a0f127ce3e4c794f81661295a3f6f26b5bf5b97fb244c49fe6bcebd202c337d18da4c37520461872c9e0f4d735b45f03db80288d8a4b1e2e9c8350860c0bb7bc4e461cff6e2827720450c189ff7946a48ecc234a1ad8107ed1baf3d32d4b5d678a9972e768f4f8fc854ba03c36d9f67ea1ff058c3e5390c5a3ce16e7803d6f70d2514b977911427ac92694065e1bf4f51791d0cd1e0426ced501e125fe7a03d1514b0c41dfb4c36b8c12128a84ec8bd7776089fd5918315fe4fa01a9021897f48d77ea4719f46f91ed2f07ea2cbe57214cddbccafabc2d04881ccc02cab2e6a12f9e4291
n = 1552518092300708935148979488462502555256886017116696611139052038026050952686376886330878408828646477971459063658923221258297866648143023058142446317581796810373905913084934869211153276980011573717416472395713363686571638755823503877
e = 65537

p, q = fermat(n)

print "p",p
print "q",q
a = (p - 1) * (q - 1)

x = 0
while True:
    if (a * x + 1) % e == 0:
        d = (a * x + 1) / e
        break
    x = x + 1

m = pow(c, d, n)

flag = ('%x' % m).decode('hex')
print flag
