import matplotlib.pyplot as plt
import numpy as np

def problema1_normal_25_dados():
    mu, sigma = 15, 3
    s = np.random.normal(mu, sigma, 25)
    count, bins, ignored = plt.hist(s, 5, normed=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_normal_25_dados')
    plt.show()

def problema1_expo_25_dados():
    mu, sigma = 5, 5
    s = np.random.exponential(mu, 25)
    count, bins, ignored = plt.hist(s, 5, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_expo_25_dados')
    plt.show()

def problema1_triangular_25_dados():
    mu, mode, sigma = 1, 5, 7
    s = np.random.triangular(mu, mode, sigma, 25)
    count, bins, ignored = plt.hist(s, 5, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_triangular_25_dados')
    plt.show()

def problema1_uniforme_25_dados():
    mu, sigma = 10, 20
    s = np.random.uniform(mu, sigma, 25)
    count, bins, ignored = plt.hist(s, 5, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_uniforme_25_dados')
    plt.show()

problema1_normal_25_dados()
problema1_expo_25_dados()
problema1_triangular_25_dados()
problema1_uniforme_25_dados()

######################################################
#
# UNIFORME(10, 20) Represents better 25 data samples
#
######################################################
