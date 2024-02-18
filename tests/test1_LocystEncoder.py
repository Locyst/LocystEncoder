from LocystEncoder.LocystEncoder import LocystEncoder

seed = Encoder.generateSeed(50)
string = "Hello World!"
 
encoded = Encoder.encode(string, seed)
decoded = Encoder.decode(encoded[0], encoded[1])

print(seed)
print(encoded[0])
print(decoded)
