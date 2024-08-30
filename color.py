def classify_color_hsv(bgr):
    # Convert BGR to HSV
    hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

    # Define color ranges in HSV
    colors = {
        'red': [(0, 50, 50), (10, 255, 255), (160, 50, 50), (180, 255, 255)],  # Red wraps around
        'orange': [(10, 50, 50), (25, 255, 255)],
        'yellow': [(25, 50, 50), (35, 255, 255)],
        'green': [(35, 50, 50), (85, 255, 255)],
        'cyan': [(85, 50, 50), (95, 255, 255)],
        'blue': [(95, 50, 50), (135, 255, 255)],
        'purple': [(135, 50, 50), (160, 255, 255)],
        'white': [(0, 0, 200), (180, 30, 255)],
        'gray': [(0, 0, 50), (180, 30, 200)],
        'black': [(0, 0, 0), (180, 255, 50)]
    }

    # Check which range the hue falls into
    for color, ranges in colors.items():
        for i in range(0, len(ranges), 2):
            if ranges[i][0] <= hsv[0] <= ranges[i+1][0] and ranges[i][1] <= hsv[1] <= ranges[i+1][1] and ranges[i][2] <= hsv[2] <= ranges[i+1][2]:
                return color
    return 'unknown'
