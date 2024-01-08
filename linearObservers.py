import numpy as np


# Implementation of various linear observers

def region_of_interest_observer(image, target_mean):
    """
    Region-of-Interest (ROI) Observer.

    Parameters:
    - image: 2D numpy array, the reconstructed image.
    - target_mean: scalar, the first-order statistic (mean) of the target signal.

    Returns:
    - scalar, the observer response within the specified ROI.
    """

    height, width = image.shape

    # Turn image matrix into M x 1 vector
    image_vector = np.ndarray.flatten(image)

    # Create template
    template = np.zeros((height, width))
    template.fill(target_mean)

    # Turn template into M x 1 vector and transpose it
    template_vector = np.ndarray.flatten(template).transpose()

    # Compute scalar product of the transposed template with the observation image
    return np.matmul(template_vector, image_vector)


def region_of_interest_observer_ske(image, target_mean, target_position, target_radius):
    """
    Region-of-Interest (ROI) Observer for SKE task.

    Parameters:
    - image: 2D numpy array, the reconstructed image.
    - target_mean: scalar, the first-order statistic (mean) of the target signal.
    - target_position: Tuple, (row, column), position of the target signal.
    - target_radius: Scalar, radius of the disk-shaped target signal.

    Returns:
    - scalar, the observer response within the specified target position.
    """

    height, width = image.shape
    row, col = target_position

    # Turn image matrix into M x 1 vector
    image_vector = np.ndarray.flatten(image)

    # Create template
    y, x = np.ogrid[-row:width - row, -col:height - col]
    mask = x * x + y * y <= target_radius * target_radius
    template = np.zeros((height, width))
    template[mask] = target_mean

    # Turn template into M x 1 vector and transpose it
    template_vector = np.ndarray.flatten(template).transpose()

    # Compute scalar product of the transposed template with the observation image
    return np.matmul(template_vector, image_vector)


def non_pre_whitening_observer(image, target_mean, background_mean, noise_mean):
    """
    Non-Prewhitening Observer.

    Parameters:
    - image: 2D numpy array, the reconstructed image.
    - target_mean: scalar, the first-order statistic (mean) of the target signal
    - background_mean: scalar, the first-order statistic (mean) of the background
    - noise_mean: scalar, the first-order statistic (mean) of the noise

    Returns:
    - scalar, the observer response.
    """

    height, width = image.shape

    # Turn image matrix into M x 1 vector
    image_vector = np.ndarray.flatten(image)

    # Create template
    mean_signal_absent = np.zeros((height, width))
    mean_signal_absent.fill(background_mean + noise_mean)

    mean_signal_present = np.zeros((height, width))
    mean_signal_present.fill(background_mean + noise_mean + target_mean)

    # Calculate template, turn it into M x 1 vector and transpose it
    template = np.subtract(mean_signal_present, mean_signal_absent)
    template_vector = np.ndarray.flatten(template).transpose()

    # Compute scalar product of the transposed template with the observation image
    return np.matmul(template_vector, image_vector)


def pre_whitening_observer(image, background_variance, noise_variance):
    """
    Prewhitening Observer.

    Parameters:
    - image: 2D numpy array, the reconstructed image.

    Returns:
    - scalar, the observer response.
    """
    return image


def hotelling_observer(image, covariance_matrix):
    """
    Hotelling Observer.

    Parameters:
    - image: 1D numpy array, the reconstructed image (flattened).
    - covariance_matrix: 2D numpy array, the covariance matrix of the background.

    Returns:
    - scalar, the observer response.
    """
    return np.dot(image, np.linalg.solve(covariance_matrix, image))
