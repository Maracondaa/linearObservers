import matplotlib.pyplot as plt
from createImages import generate_synthetic_image
from linearObservers import region_of_interest_observer, non_pre_whitening_observer, region_of_interest_observer_ske


def main():
    # Variables for image generation:
    image_size = (64, 64)
    target_position = (32, 32)
    target_amplitude = target_mean = -1.5
    target_radius = 8.0
    noise_std = 0.1

    # Generate an image with a random background, target signal, and noise
    image_with_target = generate_synthetic_image(image_size, target_position, target_amplitude, target_radius,
                                                 noise_std)

    # Generate an image without a target signal but with a random background and noise
    image_without_target = generate_synthetic_image(image_size, noise_std=noise_std)

    # Display the generated images
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image_with_target, cmap='gray', interpolation='none')
    plt.title('Image with Target Signal')

    plt.subplot(1, 2, 2)
    plt.imshow(image_without_target, cmap='gray', interpolation='none')
    plt.title('Image without Target Signal')

    plt.show()

    # Calculation of the linear discriminant for the ROI observer (SKE) for both images
    roi_ske_response_with_target = region_of_interest_observer_ske(image_with_target, target_mean, target_position,
                                                                   target_radius)
    roi_ske_response_without_target = region_of_interest_observer_ske(image_without_target, target_mean,
                                                                      target_position, target_radius)

    print('ROI Observer (SKE, signal present): ', roi_ske_response_with_target)
    print('ROI Observer (SKE, signal absent): ', roi_ske_response_without_target, "\n")

    # Calculation of the linear discriminant for the ROI observer for both images
    roi_response_with_target = region_of_interest_observer(image_with_target, target_mean)
    roi_response_without_target = region_of_interest_observer(image_without_target, target_mean)

    print('ROI Observer (signal present): ', roi_response_with_target)
    print('ROI Observer (signal absent): ', roi_response_without_target, "\n")

    # Calculation of the linear discriminant for the ROI observer for both images
    npw_response_with_target = non_pre_whitening_observer(image_with_target, target_mean, 0, 0)
    npw_response_without_target = non_pre_whitening_observer(image_without_target, target_mean, 0, 0)

    print('NPW Observer (signal present): ', npw_response_with_target)
    print('NPW Observer (signal absent): ', npw_response_without_target)

    # PW & Hotelling Observer

    return


if __name__ == "__main__":
    main()
