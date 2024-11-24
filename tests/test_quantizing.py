from filterkit.core import quantizing as quant
from tests.common import _load_test_image, _run_default_assertions

image = _load_test_image()

def test_normal_quantize_no_args():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = quant.apply_quantization(img, 0)
		_run_default_assertions(out, img)

def test_normal_quantize():
	for i in range(10):
		out = quant.apply_quantization(image, 0, palette=[(8, 24, 32), (52, 104, 86), (136, 192, 112), (224, 248, 208)],
		                               metric=i)
		_run_default_assertions(out, image, color_count=4)

def test_single_channel():
	for i in range(10):
		out = quant.apply_quantization(image, 0, palette=[(8, 24, 32), (52, 104, 86), (136, 192, 112), (224, 248, 208)],
		                               metric=i, channel=1)
		_run_default_assertions(out, image)

def test_grayscale_quantize_no_args():
	for img in [image, image.convert('RGBA')]:
		out = quant.apply_quantization(img, 1)
		_run_default_assertions(out, img)

def test_grayscale_quantize():
	for i in range(10):
		out = quant.apply_quantization(image, 1, num_colors=8, metric=i, levels_range_adjusted=True)
		_run_default_assertions(out, image, color_count=8)

def test_kmean_quantize_no_args():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = quant.apply_quantization(img, 2)
		_run_default_assertions(out, img)

def test_kmean_quantize():
	for i in range(3):
		out = quant.apply_quantization(image, 2, num_colors=8, clustering_iterations=6, cluster_init_method=i,
		                               flipped_centroid_orient=True)
		_run_default_assertions(out, image, color_count=8)

def test_blur_quantize_no_args():
	for img in [image, image.convert('RGBA'), image.convert('L')]:
		out = quant.apply_quantization(img, 3)
		_run_default_assertions(out, img)

def test_blur_quantize():
	out = quant.apply_quantization(image, 3, num_colors=16, blur_radius=11)
	# the number of colors in the result here != 16 actually, blur quantize only approximates quantizing
	_run_default_assertions(out, image)
