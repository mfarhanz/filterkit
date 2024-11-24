from PIL import Image
from io import BytesIO
from time import perf_counter
from os import path

def _load_test_image():
    current_dir = path.dirname(__file__)
    test_img_path = path.join(current_dir, '_sample_image.txt')
    with open(test_img_path, 'r') as f:
        hex_data = f.read()
    binary_data = bytes.fromhex(hex_data.replace('\\x', '').replace('\n', ''))
    image_bytes_stream = BytesIO(binary_data)
    image = Image.open(image_bytes_stream)
    return image

def _run_default_assertions(result, original, size_similar=True, mode_similar=True, mode=None, color_count=None):
    assert list(result.getdata()) != list(original.getdata())
    assert type(result) == Image.Image
    if size_similar:
        assert result.size == original.size
    else:
        assert result.size != original.size
    if mode is None:
        if mode_similar:
            assert result.mode == original.mode
        else:
            assert result.mode != original.mode
    else:
        assert result.mode == mode
    if color_count is not None and isinstance(color_count, int):
        count = len(set(list(result.getdata())))
        assert count == color_count

def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        stop = perf_counter()
        print(f"{func.__name__} executed in {(stop - start) * 1000}ms")
        return result
    return wrapper
