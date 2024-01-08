# Creation of random sample images
# Background is normal distributed and Gaussian noise is added automatically
# Target signal can only be a 2d disk

import numpy as np


def generate_synthetic_image(size, target_position=None, target_amplitude=None, target_radius=None, noise_std=1.0):
    """
    Generate a synthetic 2D image with a normal distributed background, optional circular target signal,
    and added Gaussian noise.

    Parameters:
    - size: Tuple, (height, width), dimensions of the image.
    - target_position: Tuple, (row, column), position of the target signal. If None, no target signal.
    - target_amplitude: Scalar, amplitude of the target signal. If None, no target signal.
    - target_radius: Scalar, radius of the disk-shaped target signal. If None, no target signal.
    - noise_std: Scalar, standard deviation of Gaussian noise.

    Returns:
    - 2D numpy array, the generated image.
    """

    # Generate a random background
    random_background = np.random.normal(0, 1, size)

    # Add target signal if specified
    if target_position is not None and target_amplitude is not None and target_radius is not None:
        row, col = target_position
        height, width = size
        y, x = np.ogrid[-row:width - row, -col:height - col]
        mask = x * x + y * y <= target_radius * target_radius
        random_background[mask] += target_amplitude

    # Add noise
    noise = np.random.normal(0, noise_std, size)
    image = random_background + noise

    return image
