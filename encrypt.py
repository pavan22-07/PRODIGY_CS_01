from PIL import Image

def encrypt_decrypt_image(input_image, output_image, key):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            # Apply XOR operation with key
            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[i, j] = (r, g, b)

    img.save(output_image)
    print(f"Saved: {output_image}")

# Main Program
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter choice: ")

input_image = input("Enter image path: ")
output_image = input("Enter output image name: ")
key = int(input("Enter numeric key (0-255): "))

encrypt_decrypt_image(input_image, output_image, key)

if choice == '1':
    print("Image Encrypted Successfully!")
elif choice == '2':
    print("Image Decrypted Successfully!")
else:
    print("Invalid choice")