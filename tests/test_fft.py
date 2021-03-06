#!/usr/bin/python

"""
test_fft.py

"""

__author__ = "Sunil"
__copyright__ = "Copyright 2015"
__license__ = "GNU License"
__version__ = "0.1.0"
__email__ = "suba5417@colorado.edu"


import fft
import sys
import unittest
import numpy as np

class TestFFT(unittest.TestCase):
    """
    Test Fast fourier transformations
    """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_simple_fft(self):
        x = np.random.random(1024)
        self.assertTrue(np.allclose(fft.fft(x), np.fft.fft(x)))

    def test_small_odd_fft(self):
        x = np.random.random(103)
        self.assertRaises(ValueError, fft.fft, x)

    def test_large_odd_fft(self):
        x = np.random.random(103090987)
        self.assertRaises(ValueError, fft.fft, x)

    def test_invalid_points_fft(self):
        x = []
        self.assertRaises(ValueError, fft.fft, x)

    def test_long_fft(self):
        x = np.random.random(1020)
        self.assertTrue(np.allclose(fft.dft(x), np.fft.fft(x)))

    def test_ifft(self):
        # x = np.random.random(128)
        x = np.random.random(30) + 1j*np.random.random(30)
        # self.assertAlmostEquals(x , fft.ifft(fft.fft(x)))
        # self.assertTrue(np.allclose(fft.ifft(fft.fft(x)), np.fft.ifft(np.fft.fft(x))))

    def test_all_zero_fft(self):
        x = np.zeros(512)
        self.assertTrue(np.allclose(fft.fft(x), np.fft.fft(x)))

    def test_all_ones_fft(self):
        x = np.ones(1024)
        self.assertTrue(np.allclose(fft.fft(x), np.fft.fft(x)))

def main(*argv):
    unittest.main()

if __name__ == '__main__':
    main(sys.argv)
