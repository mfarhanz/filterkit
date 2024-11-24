from filterkit.core import smoothing as smooth
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_all_filters():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for i in range(6):
			out = smooth.apply_smoothing(img, i, 9)
			_run_default_assertions(out, img)

def test_single_channel():
	out = smooth.apply_smoothing(image, 0, 9, channel=2)
	_run_default_assertions(out, image)
