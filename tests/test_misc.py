from filterkit.core import pillow_misc as pillow
from filterkit.core import filters_misc as misc
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_pillow_duotone_tritone():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = pillow.make_duotone_or_tritone(img, (128, 55, 128), (55, 55, 128), (55, 55, 55), 120, 100, 55)
		if img.mode == 'L':
			_run_default_assertions(out, img, mode='RGB')
		else:
			_run_default_assertions(out, img)

def test_pillow_autocontrast():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = pillow.apply_autocontrast(img, (0.35, 0.8))
		_run_default_assertions(out, img)

def test_pillow_equalize_histogram():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = pillow.equalise_histogram(img)
		_run_default_assertions(out, img)

def test_pillow_bit_quantize():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = pillow.fast_bit_quantization(img, 55)
		_run_default_assertions(out, img)

def test_thresholding():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for thresh in [misc.apply_niblack_threshold, misc.apply_sauvola_threshold]:
			out = thresh(img, 7, 0.5, False)
			_run_default_assertions(out, img, mode='L')

def test_pixelize():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = misc.pixelize(img, 950)
		_run_default_assertions(out, img)

def test_matrixify():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = misc.matrixify(img, 2000, 20)
		if img.mode == 'L':
			_run_default_assertions(out, img, mode='RGB')
		else:
			_run_default_assertions(out, img)

def test_superpixelate():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = misc.superpixelate(img, 500, 90, 5)
		if img.mode == 'L':
			_run_default_assertions(out, img, mode='RGB')
		else:
			_run_default_assertions(out, img)

def test_xray():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = misc.xray(img, 10, 55)
		if img.mode == 'L':
			_run_default_assertions(out, img, mode='RGB')
		else:
			_run_default_assertions(out, img)
