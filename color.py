def preprocess_image(image):
    # Convert the image to YUV (Luminance and Chrominance) color space
    yuv_img = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    
    # Equalize the histogram of the Y channel (brightness)
    yuv_img[:, :, 0] = cv2.equalizeHist(yuv_img[:, :, 0])
    
    # Convert back to BGR
    processed_image = cv2.cvtColor(yuv_img, cv2.COLOR_YUV2BGR)
    return processed_image

image = cv2.imread('car_image.jpg')
processed_image = preprocess_image(image)

def get_dominant_color_hsv(image, k=5):
    # Convert the image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Reshape the image to be a list of pixels
    pixels = hsv_image.reshape((-1, 3))
    
    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(pixels)
    
    # Get the cluster center with the maximum count
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_
    counts = np.bincount(labels)
    dominant_index = np.argmax(counts)
    dominant_color_hsv = centers[dominant_index]
    
    # Convert the dominant color back to RGB
    dominant_color_rgb = cv2.cvtColor(np.uint8([[dominant_color_hsv]]), cv2.COLOR_HSV2BGR)[0][0]
    return dominant_color_rgb

dominant_color = get_dominant_color_hsv(processed_image, k=5)
print(f"The dominant color (RGB) is: {dominant_color}")
