from filterkit.core import blending as blend
from tests.common import _load_test_image, _run_default_assertions
from PIL import Image

image = _load_test_image()

def test_blending_rgba():
	for i in range(19):
		out = blend.apply_blending(image, image.transpose(Image.FLIP_TOP_BOTTOM), i)
		_run_default_assertions(out, image)

def test_blending_rgb():
	img = image.convert('RGBA')
	for i in range(19):
		out = blend.apply_blending(img, img.transpose(Image.FLIP_TOP_BOTTOM), i)
		_run_default_assertions(out, img)

def test_blending_gray():
	img = image.convert('L')
	for i in range(19):
		out = blend.apply_blending(img, img.transpose(Image.FLIP_TOP_BOTTOM), i)
		_run_default_assertions(out, img)
	