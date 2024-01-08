## Linear Observers:

This repository contains code to test various linear observers on synthetically generated images. The linear observers implemented are:

### 1. Region-of-Interest (ROI) Observer (2 versions, one with SKE assumption):
The Region-of-Interest (ROI) observer focuses on a specific region of the reconstructed image. It needs information about the first-order statistic of the target signal.
- image: The (reconstructed) image.
- target_mean: The first-order statistic (mean) of the target signal.
For the SKE task additional information about the signal is needed.
- target_position: Position of the target signal / region of interest (if position is not known).
- target_radius: Radius of the disk-shaped target signal / radius of circular search area (if position is not known).

### 2. Non-Prewhitening Observer:
The Non-Prewhitening observer is used to model human performance in detecting signals in the presence of noise. It needs information about the first-order statistic of the target signal, the background and the noise.
- image: The (reconstructed) image.
- target_mean: The first-order statistic (mean) of the target signal
- background_mean: The first-order statistic (mean) of the background
- noise_mean: The first-order statistic (mean) of the noise

### 3. Prewhitening Observer:

The Prewhitening observer is an extension of the Non-Prewhitening observer. It considers both the image and the noise power spectrum to calculate the observer response.
- image: The reconstructed image.
- noise_power_spectrum: The power spectrum of the noise.

### 4. Hotelling Observer:

The Hotelling observer is commonly used in medical imaging. It uses the inverse covariance matrix of the background.
- image: The flattened reconstructed image.
- covariance_matrix: The covariance matrix of the background.

## Creation of synthetic test images:
To be able to test the observers synthetic images are created by first creating a White Gaussian Background, adding an optional disk-shaped target and then adding Gaussian noise. The result is given as a matrix.

## Assumptions:
First- and second-order statistics of the target signal, the background and tne noise are known.
