import numpy as np
from PIL import Image

def calculate_color_percentage(image):
    # Convert image to numpy array
    image_array = np.array(image)

    # Reshape the array to a 2D matrix
    matrix = image_array.reshape(-1, 3)

    # Calculate the total number of pixels
    total_pixels = matrix.shape[0]
    blue_sum = np.sum(matrix[:])
    
    green_sum = np.sum(matrix[:])
    red_sum = np.sum(matrix[:])
    print(blue_sum)
    print(green_sum)
    print(red_sum)
    # Calculate the percentage of each color channel
    red_percentage = (red_sum / (total_pixels * 255)) * 100
    green_percentage = (green_sum / (total_pixels * 255)) * 100
    blue_percentage = (blue_sum / (total_pixels * 255)) * 100
    

    return red_percentage, green_percentage, blue_percentage
# all colors function.
def count_unique_colors(image_path):
    image = Image.open(image_path)
    unique_colors = image.getcolors(image.size[0] * image.size[1])
    num_unique_colors = len(unique_colors)
    return num_unique_colors

def change_rgb(image, target_color, replacement_color):
   
    image_array = np.array(image)

    # Create a mask for pixels with the target color
    target_pixels = np.all(image_array == target_color, axis=-1)

    # Change target pixels to the replacement color
    image_array[target_pixels] = replacement_color

    # Convert the modified array back to an image
    modified_image = Image.fromarray(image_array)

    return modified_image

def main():
    image_path = input("Enter address of photo:")
    image = Image.open(image_path)

    red_percentage, green_percentage, blue_percentage = calculate_color_percentage(image)

    print(f"Red Percentage: {red_percentage}%")
    print(f"Green Percentage: {green_percentage}%")
    print(f"Blue Percentage: {blue_percentage}%")
    
    
    image.show()

    # Get RGB color values from the user for the target color
    target_red = int(input("Enter the value for target red (0-255): "))
    target_green = int(input("Enter the value for target green (0-255): "))
    target_blue = int(input("Enter the value for target blue (0-255): "))
    target_color = [target_red, target_green, target_blue]

    # Get RGB color values from the user for the replacement color
    replacement_red = int(input("Enter the value for replacement red (0-255): "))
    replacement_green = int(input("Enter the value for replacement green (0-255): "))
    replacement_blue = int(input("Enter the value for replacement blue (0-255): "))
    replacement_color = [replacement_red, replacement_green, replacement_blue]

    modified_image = change_rgb(image, target_color, replacement_color)
    modified_image.show()
     
    num_colors = count_unique_colors(image_path)
    print("Number of unique colors:", num_colors)

   

if __name__ == '__main__':
    main()