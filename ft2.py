
def IDFT2(fourier_image):
    image = np.zeros(fourier_image.shape)
    for col in range(image.shape[1]):
        image[:, col] = IDFT1(fourier_image[:, col])

    for row in range(image.shape[0]):
        image[row, :] = IDFT1(image[row,:])

    return image
