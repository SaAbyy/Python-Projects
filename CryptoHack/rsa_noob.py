from Crypto.Util.number import inverse
import binascii

# Datas

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# From factordb, n = p * q

p = 416064700201658306196320137931
q = 590872612825179551336102196593

# coprimality

phi = (p-1) * (q-1)

d = inverse(e,phi)

m = c**d**n
print(m)
hex_str = hex(m)[2:] # Removing '0x'
print(binascii.unhexlify(hex_str))
