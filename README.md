# filterkit

This library contains optimized implementations for various methods/algorithms in the following domains of image
processing:
- Convolutions (linear time/constant time methods for any kernel)
- Dithering (assorted constant time dithering methods for any kernel)
- Smoothing (sliding histogram/rank based filters and constant time median filtering)
- Blending (image compositing and assorted blend modes)
- Quantization (includes various techniques)
- Transforms (implementations for basic geometric transforms)
- Miscellaneous (collection of random, interesting filters)
  
Additionally, the library provides some useful helper methods when working images/matrices in `filterkit.tools`.

## Installation
```
pip install filterkit 
```  

Please note that this will install `pillow`, `numba`, and `numpy` as well as any additional packages needed by these.
As `numba` needs a specific version of `numpy` for itself, it will attempt to remove any existing version of `numpy`
before it installs the version of `numpy` it is compatible with. For this reason, it is *highly recommended* to only
install `filterkit` in a [**virtual environment**](https://docs.python.org/3/library/venv.html), so as not to interfere
with any global installations of these libraries.

## Importing
For image processing methods,
```
import filterkit.core
```
For accessing additional helper functions,
```
import filterkit.tools
```  

## Example Usage
```
from filterkit.core import convolution as conv
from filterkit.core import dithering as dither
from filterkit.tools import kernel_gen
from PIL import Image

image = Image.open("image.png")

# Convolution
result = conv.apply_convolution(image, kernel_gen.gaussian_kernel(11), separable=True)
result.show()

# Dithering
result = dither.apply_dithering(image, style=1, kernel=((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0.25, 0.125), 
                                                     (0.0625, 0.125, 0.25, 0.125, 0.0625), (0, 0, 0, 0, 0)), 
                                              palette=[(8, 24, 32), (52, 104, 86), (136, 192, 112), (224, 248, 208)])
result.show()
```

## Requirements
- Python v.3.8+
- [Pillow](https://pypi.org/project/pillow/)
- [Numpy](https://pypi.org/project/numpy/)
- [Numba](https://pypi.org/project/numba/)  


##  Notes
`filterkit` uses:
- [Pillow](https://pypi.org/project/pillow/) for opening/saving images
- [Numpy](https://pypi.org/project/numpy/) for handling image matrices
- [Numba](https://pypi.org/project/numba/) for fast/parallelized array indexing/traversal operations  


When using a `core` method directly, the image is expeected to be in numpy's `ndarray` format, as well as any other
matrices/palettes/kernels passed alongside.  

Each module that can be accessed from `filterkit.core` comes with its own 'apply_function' method, which can be used to
directly apply the selected function from the module to a given image after specifying the function's id in the
corresponding `style` or `method` parameter and any other parameters, without needing to ensure the parameters are in
the correct format or have been preprocessed correctly. This is because majority of the core functions use
[Numba](https://pypi.org/project/numba/) for speeding up processing, and the function parameters must be of a specific
type and structure/shape.  

<br>

As of now, `filterkit` is a work in progress, and further refinements/documentation will be produced in the future.
<br>

Author: Farhan Zia ([mfarhan@mun.ca](mailto:mfarhan@mun.ca))  
Code is currently hosted at https://github.com/mfarhanz/filterkit
