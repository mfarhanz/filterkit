from filterkit.core import transforms as transform
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_rotate():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = transform.rotate(img, 220)
		_run_default_assertions(out, img)

def test_flip():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = transform.flip(img, True)
		_run_default_assertions(out, img)

def test_resize_with_factor():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for scale in [(0.8, 0.4), (0.4, 0.8), (0.4, 0.4), (1.2, 1.5), (1.5, 1.2), (0.3, 1.6), (1.6, 0.3)]:
			out = transform.resize(img, scale[0], scale[1])
			_run_default_assertions(out, img, size_similar=False)

def test_resize_with_size():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for size in [(480, 240), (240, 480), (480, 480), (1080, 1920), (1920, 1080), (480, 1920), (1920, 480)]:
			out = transform.resize(img, size=size)
			_run_default_assertions(out, img, size_similar=False)

def test_shear():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		for factor in [(0.3, 0), (0, 0.3), (-0.3, 0), (0, -0.3), (1.2, -0.3), (0.3, -1.2), (2, -0.2)]:
			for stretch in [(0.3, 0.3), (-0.3, -0.3), (0.3, -0.6), (-0.3, 0.6), (0.6, -0.3), (2, -0.6), (0.6, -2)]:
				out = transform.shear(img, *factor, *stretch)
				_run_default_assertions(out, img, size_similar=False)

def test_perspective():
	h, w = image.size
	for img in [image]:
		for points in [
			[(h // 3, w // 3), (h // 1.3, w // 2.5), (h // 2, w // 1.3), (h // 1.5, w // 1.7)],
			[(h // 2, w // 3), (h / 3.3, w / 2.5), (h // 2, w / 1.3), (h // 1.5, w / 1.7)],
			[(h // 2, w // 3), (h / 3.3, w / 2.5), (h // 1.5, w / 1.7), (h // 2, w / 1.3)]
		]:
			for scaling in [0.2, 0.6, 1, 1.3, 1.8]:
				for const in [(30, 200), (200, 30), (100, 100), (1, 1), (0, 0)]:
					out = transform.perspective_transform(img, points, scaling, width_const=const[1], height_const=const[0])
					_run_default_assertions(out, img, size_similar=False)
