COLOUR_CODES = {"burntorange":"cc5500", "burntsienna":"e97451", "cadmiumred":"e30022", "depdspacespakle":"4a646c", "denim":"1560bd", "eggshell":"f0ead6",
                "fawn":"e5aa70", "frostbite":"e936a7", "ginger":"b06500", "gold1":"ffd700"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()