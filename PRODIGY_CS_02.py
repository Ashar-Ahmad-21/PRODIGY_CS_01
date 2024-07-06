from PIL import Image

# Function to swap pixel values in an image
def swap_pixels(image):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            # Example of swapping RGB values
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, r, g)  # Swapping RGB values

    return image

# Function to apply a basic mathematical operation on each pixel
def apply_operation(image, operation):
    pixels = image.load()
    width, height = image.size

    for x in range(width):
        for y in range(height):
            # Example: Multiply RGB values by a factor
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                int(r * operation),
                int(g * operation),
                int(b * operation),
            )

    return image

# Function to encrypt an image using XOR
def encrypt_image(image, key):
    pixels = image.load()
    width, height = image.size

    encrypted_image = Image.new(image.mode, image.size)

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            encrypted_image.putpixel((x, y), (r ^ key, g ^ key, b ^ key))

    return encrypted_image

# Function to decrypt an encrypted image using XOR
def decrypt_image(encrypted_image, key):
    return encrypt_image(encrypted_image, key)  # XOR is its own inverse

# Example usage:
if __name__ == "__main__":
    # Load an image
    original_image = Image.open("example.jpg")

    # Example 1: Swap pixel values
    swapped_image = swap_pixels(original_image)
    swapped_image.show()
    swapped_image.save("swapped_image.jpg")

    # Example 2: Apply a mathematical operation (e.g., darken)
    darkened_image = apply_operation(original_image, 0.5)
    darkened_image.show()
    darkened_image.save("darkened_image.jpg")

    # Example 3: Encrypt and decrypt using XOR (for demonstration purposes, use a key)
    encryption_key = 128
    encrypted_image = encrypt_image(original_image, encryption_key)
    encrypted_image.show()
    encrypted_image.save("encrypted_image.jpg")

    decrypted_image = decrypt_image(encrypted_image, encryption_key)
    decrypted_image.show()
    decrypted_image.save("decrypted_image.jpg")
