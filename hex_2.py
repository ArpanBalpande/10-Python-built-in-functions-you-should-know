def rgb_to_hex(rgb_triple):
    """Function that maps a RGB tuple representation to a hexadecimal string
    Parameters:
    rgb_triple (tuple): RGB tuple representation (red, green, and blue)
    Returns:
    hex_string (string): Hexadecimal string representation '0xRRGGBB'
    """
    hex_string = ''
    # we loop through the red, green, blue values of the tuple rgb_tuple
    for integer in rgb_triple:
        hexadecimal = hex(integer)[2:] # string slicing to elimininate the prefix '0x'
        if len(hexadecimal) == 1:
            hexadecimal = '0' + hexadecimal # pad the string to the left with a 0
        hex_string += hexadecimal
    return '#' + hex_string

# call the function
color_1 = (255, 255, 255)
color_2 = (255, 255, 0)
color_3 = (70, 90, 200)

color_1_hex = rgb_to_hex(color_1)
print(color_1_hex)
# '#ffffff'

color_2_hex = rgb_to_hex(color_2)
print(color_2_hex)
# '#ffff00'

color_3_hex = rgb_to_hex(color_3)
print(color_3_hex)
# '#465ac8'