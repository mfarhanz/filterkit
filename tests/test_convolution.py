from filterkit.core import convolution as conv
from filterkit.tools import kernel_gen
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_normal_convolve():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, [[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
		_run_default_assertions(out, img)

def test_no_kernel():
	out = conv.apply_convolution(image)
	assert out == image

def test_midsize_kernel():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.gaussian_kernel(31))
		_run_default_assertions(out, img)

def test_separable():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.gaussian_kernel(11), separable=True)
		_run_default_assertions(out, img)

def test_box_blur():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.box_blur_kernel(11))
		_run_default_assertions(out, img)

def test_large_kernel():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.gaussian_kernel(121))
		_run_default_assertions(out, img)

def test_fft_convolve():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.gaussian_kernel(101), handle_boundary=False)
		_run_default_assertions(out, img)

def test_single_channel():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, kernel_gen.gaussian_kernel(21), channel=2)
		_run_default_assertions(out, img)

def test_invalid_kernel():
	out = conv.apply_convolution(image, [[0, 1], [-1, 1, -1]])
	_run_default_assertions(out, image)

def test_multi_kernel():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = conv.apply_convolution(img, [[1, 0, -1], [2, 0, -2], [1, 0, -1]], [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
		_run_default_assertions(out, img)

def test_oversized_kernel():
	out = conv.apply_convolution(image, kernel_gen.gaussian_kernel(240))
	assert out == image
