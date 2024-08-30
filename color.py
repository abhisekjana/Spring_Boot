def classify_color(rgb):
    colors = {
        'black': [0, 0, 0],
        'white': [255, 255, 255],
        'red': [255, 0, 0],
        'green': [0, 255, 0],
        'blue': [0, 0, 255],
        'yellow': [255, 255, 0],
        'gray': [128, 128, 128],
        'silver': [192, 192, 192],
        'maroon': [128, 0, 0],
        'orange': [255, 165, 0],
        'purple': [128, 0, 128],
        'brown': [165, 42, 42],
        'pink': [255, 192, 203],
        'gold': [255, 215, 0],
        'dark green': [0, 100, 0],
        'navy blue': [0, 0, 128],
        'light blue': [173, 216, 230],
        'beige': [245, 245, 220],
        'burgundy': [128, 0, 32],
        'teal': [0, 128, 128],
        'dark gray': [64, 64, 64],
        'light gray': [211, 211, 211],
        'lime green': [50, 205, 50],
        'aqua': [0, 255, 255],
        'dark blue': [0, 0, 139],
        'charcoal': [54, 69, 79],
        'pearl': [242, 242, 242],
        'champagne': [247, 231, 206],
        'rose gold': [183, 110, 121],
        'cream': [255, 253, 208],
        'turquoise': [64, 224, 208],
        'plum': [142, 69, 133],
        'sand': [194, 178, 128],
        'mint': [189, 252, 201],
        'coral': [255, 127, 80],
        'olive': [128, 128, 0]
    }

    # Calculate Euclidean distance to find the closest predefined color
    min_dist = float('inf')
    color_name = 'unknown'
    for name, color in colors.items():
        dist = np.sqrt(sum((rgb - np.array(color)) ** 2))
        if dist < min_dist:
            min_dist = dist
            color_name = name

    return color_name

# Example usage
dominant_color = [120, 100, 80]  # Replace with detected RGB color
car_color = classify_color(dominant_color)
print(f'The car color is: {car_color}')
