*Assignments in this class are individual. While you may discuss ideas with others, you must submit your own individual effort.*

# Goal
The goal of this assignment is to exercise your understanding of key Python components, such as assignments, expressions, if and loop statements, functions, lists, libraries, and basic programming patterns.

You will write Python code to perform basic image processing tasks on grayscale images. You will implement functions to perform the following image processing tasks:

- Horizontal flip
- Removing noise
- Blurring
- Thresholding
- Center crop

You will be using pytest to test your code.

1. Accept the invitation from the link in Canvas.
2. Clone your repository using `git`. Refer to the lecture for detailed instructions.
3. Copy the `*jpg`, `*py` and  `*ipynb` files from https://github.com/yanneta/msds501/tree/main/hws/hw2 to your repository.
4. Fill the functions in `image_util.py`.
5. Refer to `images.ipynb` for guidense on expected results on real images. 
6. Ensure that your solutions pass the unit tests by running:
`pytest`
7. Commit and push your files to github.com.

You should get something like this from running `pytest`:

> ============================== test session starts ===============================
> platform darwin -- Python 3.11.8, pytest-7.4.0, pluggy-1.0.0
> rootdir: /Users/yinterian/teaching/computation/msds501_p/hws/hw2
> plugins: anyio-4.2.0
> collected 8 items

> test_image_util.py ........                                                [100%]

> =============================== 8 passed in 0.13s ================================

Refer to`test_image_util.py` for guidense on expected results for test examples.

## Taks 1: Horizontal flip

For this task, you will fill in the function `horizontal_flip` in the `image_util.py` file. You should create a new image, then create a nested for loop to iterate over all x and y values within the width and height of the image. Within the inner loop, set pixels in the copied image to the corresponding pixels copied from the original image. Finally, return the flipped image at the end of the function. 


## Task 2: Removing noise

The first step in this task is to write the function `region_avg` that calculates the average pixel value within the a kxk rectangular region centered at the specified coordinates. The second step is to write the function `blur` that uses the `region_avg` function on every pixel on the input image.


## Task 3: Blurring

The first step in this task is to write the function `region_median` that calculates the median  pixel value within the a kxk rectangular region centered at the specified coordinates. The second step is to write the function `denoise` that uses the `region_median` function on every pixel on the input image.

## Task 4: Thresholding
For this task, you will fill in the function `thresholding`. Given an image, it should return a new image with just two values. Pixels above the threshold in the original image will be set to 255 (white), while pixels below the threshold will be set to 0 (black) in the new image.

## Task 5: Center Crop
For this task, you will fill in the function `center_crop`.
Given an image, the function should return a center crop of the image with the specified size. 
When working with NumPy matrices, to extract a submatrix of `im`, you use the following syntax: `im[start_x:end_x, start_y:end_y]`.

