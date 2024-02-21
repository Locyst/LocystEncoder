from LocystEncoder.LocystEncoder import LocystEncoder

seed = LocystEncoder.generateSeed(50)
string = "Hello World!"

encoded = LocystEncoder.encode(string, seed)
decoded = LocystEncoder.decode(encoded[0], encoded[1])

print(seed)
print(encoded[0])
print(decoded)
