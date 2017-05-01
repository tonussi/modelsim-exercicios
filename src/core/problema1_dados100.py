import matplotlib.pyplot as plt
import numpy as np

def problema1_normal_100_dados():
    mu, sigma = 15, 3
    s = np.random.normal(mu, sigma, 100)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_normal_100_dados')
    plt.show()

def problema1_expo_100_dados():
    mu, sigma = 5, 5
    s = np.random.exponential(mu, 100)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_expo_100_dados')
    plt.show()

def problema1_triangular_100_dados():
    mu, mode, sigma = 1, 5, 7
    s = np.random.triangular(mu, mode, sigma, 100)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_triangular_100_dados')
    plt.show()

def problema1_uniforme_100_dados():
    mu, sigma = 10, 20
    s = np.random.uniform(mu, sigma, 100)
    count, bins, ignored = plt.hist(s, 30, normed=True)
    plt.plot(bins, 1 / (mu * np.sqrt(2 * np.pi)) * np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)), linewidth = 2, color = 'r')
    plt.title('problema1_uniforme_100_dados')
    plt.show()

problema1_normal_100_dados()
problema1_expo_100_dados()
problema1_triangular_100_dados()
problema1_uniforme_100_dados()

######################################################
#
# NORMAL(15, 3) Represents better 100 data samples
#
######################################################
