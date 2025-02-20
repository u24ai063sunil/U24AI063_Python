def decode_message(encoded_message):
    def decode(index, current_decoded, decoded_messages):
        if index == len(encoded_message):
            decoded_messages.append("".join(current_decoded))
            return

        # Decode one digit
        one_digit = int(encoded_message[index])
        if 1 <= one_digit <= 9:
            current_decoded.append(chr(one_digit + 64)) 
            decode(index + 1, current_decoded, decoded_messages)
            current_decoded.pop()  # Backtrack

        # Decode two digits (if possible)
        if index + 1 < len(encoded_message):
            two_digits = int(encoded_message[index:index + 2])
            if 10 <= two_digits <= 26:
                current_decoded.append(chr(two_digits + 64)) 
                decode(index + 2, current_decoded, decoded_messages)
                current_decoded.pop()  # Backtrack

    decoded_messages = []
    decode(0, [], decoded_messages)
    return decoded_messages


encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
print(f"Encoded message: {encoded_message}")
print("Possible decoded messages:")
for message in decoded_messages:
    print(message)

encoded_message2 = "123"
decoded_messages2 = decode_message(encoded_message2)
print(f"\nEncoded message: {encoded_message2}")
print("Possible decoded messages:")
for message in decoded_messages2:
    print(message)

encoded_message3 = "226"
decoded_messages3 = decode_message(encoded_message3)
print(f"\nEncoded message: {encoded_message3}")
print("Possible decoded messages:")
for message in decoded_messages3:
    print(message)
