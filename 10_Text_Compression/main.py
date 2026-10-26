text = input("Enter text using letters only: ")
if text == "":
    print("No text entered.")
else:
    compressed = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count = count + 1
        else:
            compressed = compressed + text[i - 1] + str(count)
            count = 1
    compressed = compressed + text[len(text) - 1] + str(count)
    print("Compressed text:", compressed)
