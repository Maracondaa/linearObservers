import matplotlib.pyplot as plt
from createImages import generate_synthetic_image
from linearObservers import region_of_interest_observer, non_pre_whitening_observer, region_of_interest_observer_ske, \
    pre_whitening_observer, hotelling_observer

# Variables for image generation:
image_size = (64, 64)
target_position = (32, 32)
target_amplitude = target_mean = -1.5
target_radius = 8.0
noise_std = 0.1


def generate_discriminants_for_two_images():
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
    print('ROI Observer (signal absent): ', roi_response_without_target, '\n')

    # Calculation of the linear discriminant for the NPW observer for both images
    npw_response_with_target = non_pre_whitening_observer(image_with_target, target_mean, 0, 0)
    npw_response_without_target = non_pre_whitening_observer(image_without_target, target_mean, 0, 0)

    print('NPW Observer (signal present): ', npw_response_with_target)
    print('NPW Observer (signal absent): ', npw_response_without_target, '\n')

    # Calculation of the linear discriminant for the PW observer for both images
    pw_response_with_target = pre_whitening_observer(image_with_target, target_mean, 0, 1, 0, noise_std)
    pw_response_without_target = pre_whitening_observer(image_without_target, target_mean, 0, 1, 0, noise_std)

    print('PW Observer (signal present): ', pw_response_with_target)
    print('PW Observer (signal absent): ', pw_response_without_target, "\n")

    # Calculation of the linear discriminant for the Hotelling observer for both images
    ho_response_with_target = hotelling_observer(image_with_target, target_mean, 0, 0, 1, 0,
                                                 noise_std, 0.5, 0.5)
    ho_response_without_target = hotelling_observer(image_without_target, target_mean, 0, 0, 1, 0,
                                                    noise_std, 0.5, 0.5)

    print('HO Observer (signal present): ', ho_response_with_target)
    print('HO Observer (signal absent): ', ho_response_without_target)
    return


def generate_roc_for_threshold(threshold):
    roi_ske_true_positives = 0
    roi_ske_false_positives = 0
    roi_true_positives = 0
    roi_false_positives = 0
    npw_true_positives = 0
    npw_false_positives = 0
    pw_true_positives = 0
    pw_false_positives = 0
    ho_true_positives = 0
    ho_false_positives = 0
    for i in range(0, 100):
        # Generate an image with a random background, target signal, and noise
        image_with_target = generate_synthetic_image(image_size, target_position, target_amplitude, target_radius,
                                                     noise_std)
        # Generate an image without a target signal but with a random background and noise
        image_without_target = generate_synthetic_image(image_size, noise_std=noise_std)

        # Calculation of the linear discriminant for the ROI observer (SKE) for both images
        roi_ske_response_with_target = region_of_interest_observer_ske(image_with_target, target_mean, target_position,
                                                                       target_radius)
        roi_ske_response_without_target = region_of_interest_observer_ske(image_without_target, target_mean,
                                                                          target_position, target_radius)
        # Calculation of the linear discriminant for the ROI observer for both images
        roi_response_with_target = region_of_interest_observer(image_with_target, target_mean)
        roi_response_without_target = region_of_interest_observer(image_without_target, target_mean)

        # Calculation of the linear discriminant for the NPW observer for both images
        npw_response_with_target = non_pre_whitening_observer(image_with_target, target_mean, 0, 0)
        npw_response_without_target = non_pre_whitening_observer(image_without_target, target_mean, 0, 0)

        # Calculation of the linear discriminant for the PW observer for both images
        pw_response_with_target = pre_whitening_observer(image_with_target, target_mean, 0, 1, 0, noise_std)
        pw_response_without_target = pre_whitening_observer(image_without_target, target_mean, 0, 1, 0, noise_std)

        # Calculation of the linear discriminant for the Hotelling observer for both images
        ho_response_with_target = hotelling_observer(image_with_target, target_mean, 0, 0, 1, 0,
                                                     noise_std, 0.5, 0.5)
        ho_response_without_target = hotelling_observer(image_without_target, target_mean, 0, 0, 1, 0,
                                                        noise_std, 0.5, 0.5)

        # Determine number of true positives and false positives
        if roi_ske_response_with_target > threshold: roi_ske_true_positives += 1
        if roi_ske_response_without_target > threshold: roi_ske_false_positives += 1

        if roi_response_with_target > threshold: roi_true_positives += 1
        if roi_response_without_target > threshold: roi_false_positives += 1

        if npw_response_with_target > threshold: npw_true_positives += 1
        if npw_response_without_target > threshold: npw_false_positives += 1

        if pw_response_with_target > threshold: pw_true_positives += 1
        if pw_response_without_target > threshold: pw_false_positives += 1

        if ho_response_with_target > threshold: ho_true_positives += 1
        if ho_response_without_target > threshold: ho_false_positives += 1

    print("ROC for threshold T = ", threshold)

    print("ROI-Observer (SKE): ", roi_ske_true_positives / 100, " (TPR), ", roi_ske_false_positives / 100, " (FPR)")

    print("ROI-Observer: ", roi_true_positives / 100, " (TPR), ", roi_false_positives / 100, " (FPR)")

    print("NPW-Observer (SKE): ", npw_true_positives / 100, " (TPR), ", npw_false_positives / 100, " (FPR)")

    print("PW-Observer (SKE): ", pw_true_positives / 100, " (TPR), ", pw_false_positives / 100, " (FPR)")

    print("HO-Observer (SKE): ", ho_true_positives / 100, " (TPR), ", ho_false_positives / 100, " (FPR)")
    return


def main():
    generate_discriminants_for_two_images()
    #generate_roc_for_threshold(4)
    return


if __name__ == "__main__":
    main()
