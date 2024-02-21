import secrets


# Version 0.0.9

# Things to do
# No this probably is not very secure

class LocystEncoder:

    falseSpace = '​'  # Do not add anything here as there is already something here

    @classmethod
    def generateSeed(cls, securityLevel=10):
        """
        Creates a seed used for encoding

        Parameters:
         - securityLevel (int): The higher the number the stronger the
         seed is. Do not input decimals ( Default is 10 )

        Returns:
         - List: A list with these ints.
                 - Capitals: Occournce for capitals in encrytion
                 - Banks: Used to see how much to subtract to final value
                 - Fronts: Used to see how much to add to final value
                 - Extra: Used for extra cases in the encrytion
        """
        capitals = 0
        backs = 0
        fronts = 0
        extra = 0

        highest = 9 * securityLevel

        while capitals == backs or capitals == fronts or capitals == extra or capitals == 0:
            capitals = secrets.randbelow(highest)
        while backs == capitals or backs == fronts or backs == extra or backs == 0:
            backs = secrets.randbelow(highest)
        while fronts == capitals or fronts == backs or fronts == extra or fronts == 0:
            fronts = secrets.randbelow(highest)
        while extra == capitals or extra == backs or extra == fronts or extra == 0:
            extra = secrets.randbelow(highest)

        return [capitals, backs, fronts, extra]

    @classmethod
    def encode(cls, string, seed=None):
        """
        Encodes a string using a custom encryption method

        Paramaters:
         - string (Str): The string going through the encryption method
         - seed (List[int]): The seed being used for encryption if none are used it will generate a random one

        Return:
         - Tuple(str, list[int, int, int, int]):
                - str: The encoded string
                - list[
                    - Capitals (int): Occournce for capitals in encrytion
                    - Banks (int): Used to see how much to subtract to final value
                    - Fronts (int): Used to see how much to add to final value
                    - Extra (int): Used for extra cases in the encrytion
                    ]: The seed used for encoding
        """
        if seed is None:
            seed = cls.generateSeed()
        encoded = []
        capitals = []

        encoded.append(cls.falseSpace)
        i = seed[0]

        while i < len(string):
            capitals.append(i)
            i += seed[0]
        if not capitals:
            capitals.append(seed[0])

        i += seed[0]
        for word in string:
            for character in word:
                if character == " ":
                    encoded.append(f"%{seed[3]}")
                    encoded.append(cls.falseSpace)
                else:
                    char = str(ord(character.upper()) - seed[1] + seed[2]) if i in capitals else str(
                        ord(character) - seed[1] + seed[2])
                    if character.isupper():
                        encoded.append(f"#{char}")
                    else:
                        encoded.append(char)
                    encoded.append(cls.falseSpace)
            i += 1

        returnString = ''.join(encoded)
        return returnString[::-1], seed

    @classmethod
    def decode(cls, string, seed):
        """
        Decodes a string using a custom encryption method

        Parameters:
         - string (Str): The string being decoded
         - seed (List[int]): The seed using during the encryption

        Returns:
         - Str: The decoded string
        """
        if seed is None:
            print("Cannot run without a seed")
        string = string[::-1]
        listString = string.split(cls.falseSpace)
        decoded = []
        capitals = []

        while ("" in listString):
            listString.remove("")

        i = seed[0]

        while i < len(listString):
            capitals.append(i)
            i += seed[0]
        if not capitals:
            capitals.append(seed[0])

        i = seed[0]
        for character in listString:
            if "%" in character:
                if "%" in character and character == f"%{seed[3]}":
                    decoded.append(" ")
            else:
                if "#" in character:
                    char = character.replace("#", "")
                    char = chr(int(char) + seed[1] - seed[2])
                    decoded.append(char.upper())
                else:
                    char = chr(int(character) + seed[1] - seed[2])
                    decoded.append(char.lower()) if i in capitals else decoded.append(char)
            i += 1

        return ''.join(decoded)

# ---------------------------------------------------------------#

seed = LocystEncoder.generateSeed(50)
string = "Hello World!"

encoded = LocystEncoder.encode(string, seed)
decoded = LocystEncoder.decode(encoded[0], encoded[1])

print(seed)
print(encoded[0])
print(decoded)
