from filterkit.core import dithering as dither
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_default_dither():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = dither.apply_dithering(img)
		_run_default_assertions(out, img)

def test_all_dithers_no_args():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for i in range(4):
			out = dither.apply_dithering(img, i)
			_run_default_assertions(out, img)

def test_all_dithers():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for i in range(4):
			out = dither.apply_dithering(img, i, kernel=((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0.25, 0.125),
			                            (0.0625, 0.125, 0.25, 0.125, 0.0625), (0, 0, 0, 0, 0)), threshold=150, theta=0.9,
			                method=7, pattern=7, palette=[(8, 24, 32), (52, 104, 86), (136, 192, 112), (224, 248, 208)])
			_run_default_assertions(out, img)

def test_directional_dithers():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for i in range(2):
			out = dither.apply_dithering(img, 3, method=i)
			_run_default_assertions(out, img)
