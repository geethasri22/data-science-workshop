import numpy as np

print("--- Demonstrating 50 NumPy Operations ---")
print("-" * 40)

# I. Array Creation and Initialization

print("\n--- I. Array Creation and Initialization ---")
# 1. np.array([1, 2, 3]): Create a NumPy array from a Python list.
arr_from_list = np.array([1, 2, 3, 4, 5])
print(f"1. np.array([1,2,3,4,5]): {arr_from_list}")

# 2. np.zeros((3, 3)): Create an array filled with zeros with a given shape.
zeros_array = np.zeros((3, 3))
print(f"2. np.zeros((3,3)):\n{zeros_array}")

# 3. np.ones((2, 4)): Create an array filled with ones with a given shape.
ones_array = np.ones((2, 4))
print(f"3. np.ones((2,4)):\n{ones_array}")

# 4. np.empty((2, 2)): Create an uninitialized array of a given shape.
empty_array = np.empty((2, 2))
print(f"4. np.empty((2,2)) (values are random):\n{empty_array}")

# 5. np.arange(10): Create an array with evenly spaced values within a given interval.
arange_1 = np.arange(10)
print(f"5. np.arange(10): {arange_1}")

# 6. np.arange(0, 10, 2): arange with start, stop, step.
arange_2 = np.arange(0, 10, 2)
print(f"6. np.arange(0,10,2): {arange_2}")

# 7. np.linspace(0, 1, 5): Create an array with a specified number of evenly spaced values.
linspace_array = np.linspace(0, 1, 5)
print(f"7. np.linspace(0,1,5): {linspace_array}")

# 8. np.full((2, 2), 7): Create a full array of a specified shape and fill value.
full_array = np.full((2, 2), 7)
print(f"8. np.full((2,2), 7):\n{full_array}")

# 9. np.eye(3): Create a 2-D identity array.
identity_array = np.eye(3)
print(f"9. np.eye(3):\n{identity_array}")

# 10. np.random.rand(3, 2): Create an array of random numbers from a uniform distribution.
rand_array = np.random.rand(3, 2)
print(f"10. np.random.rand(3,2):\n{rand_array}")

# 11. np.random.randn(3, 2): Create an array of random numbers from a standard normal distribution.
randn_array = np.random.randn(3, 2)
print(f"11. np.random.randn(3,2):\n{randn_array}")

# 12. np.random.randint(0, 10, size=(2, 2)): Create an array of random integers.
randint_array = np.random.randint(0, 10, size=(2, 2))
print(f"12. np.random.randint(0,10,size=(2,2)):\n{randint_array}")


# II. Array Information and Attributes

print("\n--- II. Array Information and Attributes ---")
my_array = np.array([[1, 2, 3], [4, 5, 6]])

# 13. arr.shape: Get the dimensions of the array.
print(f"13. my_array.shape: {my_array.shape}")

# 14. arr.ndim: Get the number of array dimensions.
print(f"14. my_array.ndim: {my_array.ndim}")

# 15. arr.size: Get the total number of elements in the array.
print(f"15. my_array.size: {my_array.size}")

# 16. arr.dtype: Get the data type of the elements in the array.
print(f"16. my_array.dtype: {my_array.dtype}")

# 17. arr.itemsize: Get the size in bytes of each element of the array.
print(f"17. my_array.itemsize: {my_array.itemsize} bytes")

# 18. arr.nbytes: Get the total bytes consumed by the elements of the array.
print(f"18. my_array.nbytes: {my_array.nbytes} bytes")


# III. Array Manipulation and Indexing

print("\n--- III. Array Manipulation and Indexing ---")
arr_manip = np.arange(1, 10).reshape(3, 3)
print(f"Original array for manipulation:\n{arr_manip}")

# 19. arr[0]: Access the first element (for 1D array).
one_d_arr = np.array([10, 20, 30])
print(f"19. one_d_arr[0]: {one_d_arr[0]}")

# 20. arr[0, 1]: Access an element at a specific row and column (for 2D array).
print(f"20. arr_manip[0, 1]: {arr_manip[0, 1]}")

# 21. arr[1:3]: Slice an array.
print(f"21. arr_manip[1:3]:\n{arr_manip[1:3]}")

# 22. arr[:, 0]: Select all rows, first column.
print(f"22. arr_manip[:, 0]: {arr_manip[:, 0]}")

# 23. arr[arr > 5]: Boolean indexing (select elements based on a condition).
print(f"23. arr_manip[arr_manip > 5]: {arr_manip[arr_manip > 5]}")

# 24. arr.reshape(2, 5): Reshape an array without changing its data.
arr_to_reshape = np.arange(10)
reshaped_arr = arr_to_reshape.reshape(2, 5)
print(f"24. arr_to_reshape.reshape(2,5):\n{reshaped_arr}")

# 25. arr.flatten(): Return a copy of the array collapsed into one dimension.
flattened_arr = arr_manip.flatten()
print(f"25. arr_manip.flatten(): {flattened_arr}")

# 26. arr.ravel(): Return a flattened view of the array (if possible).
raveled_arr = arr_manip.ravel()
print(f"26. arr_manip.ravel(): {raveled_arr}")

# 27. np.concatenate((arr1, arr2), axis=0): Join a sequence of arrays along an existing axis.
arr_cat1 = np.array([[1, 2], [3, 4]])
arr_cat2 = np.array([[5, 6], [7, 8]])
concatenated_arr_0 = np.concatenate((arr_cat1, arr_cat2), axis=0)
print(f"27. np.concatenate(axis=0):\n{concatenated_arr_0}")
concatenated_arr_1 = np.concatenate((arr_cat1, arr_cat2), axis=1)
print(f"   np.concatenate(axis=1):\n{concatenated_arr_1}")

# 28. np.vstack((arr1, arr2)): Stack arrays in sequence vertically (row wise).
vstack_arr = np.vstack((arr_cat1, arr_cat2))
print(f"28. np.vstack:\n{vstack_arr}")

# 29. np.hstack((arr1, arr2)): Stack arrays in sequence horizontally (column wise).
hstack_arr = np.hstack((arr_cat1, arr_cat2))
print(f"29. np.hstack:\n{hstack_arr}")

# 30. np.split(arr, 2): Split an array into multiple sub-arrays.
split_arr = np.array([10, 20, 30, 40, 50, 60])
split_result = np.split(split_arr, 2)
print(f"30. np.split(split_arr, 2): {split_result}")

# 31. np.transpose(arr) or arr.T: Transpose an array.
transposed_arr = arr_manip.T
print(f"31. arr_manip.T:\n{transposed_arr}")

# 32. arr.copy(): Create a deep copy of the array.
original_for_copy = np.array([1, 2, 3])
copied_arr = original_for_copy.copy()
copied_arr[0] = 99 # Modify copy to show it's independent
print(f"32. original_for_copy: {original_for_copy}, copied_arr (modified): {copied_arr}")


# IV. Mathematical Operations (Element-wise and Aggregations)

print("\n--- IV. Mathematical Operations (Element-wise and Aggregations) ---")
math_arr1 = np.array([[1, 2], [3, 4]])
math_arr2 = np.array([[5, 6], [7, 8]])
print(f"math_arr1:\n{math_arr1}")
print(f"math_arr2:\n{math_arr2}")

# 33. arr + 5: Scalar addition.
add_scalar = math_arr1 + 5
print(f"33. math_arr1 + 5:\n{add_scalar}")

# 34. arr1 + arr2: Element-wise addition of two arrays.
add_arrays = math_arr1 + math_arr2
print(f"34. math_arr1 + math_arr2:\n{add_arrays}")

# 35. arr * 2: Scalar multiplication.
multiply_scalar = math_arr1 * 2
print(f"35. math_arr1 * 2:\n{multiply_scalar}")

# 36. arr1 * arr2: Element-wise multiplication.
multiply_arrays = math_arr1 * math_arr2
print(f"36. math_arr1 * math_arr2 (element-wise):\n{multiply_arrays}")

# 37. np.sqrt(arr): Element-wise square root.
sqrt_arr = np.sqrt(math_arr2)
print(f"37. np.sqrt(math_arr2):\n{sqrt_arr}")

# 38. np.exp(arr): Element-wise exponential.
exp_arr = np.exp(math_arr1)
print(f"38. np.exp(math_arr1):\n{exp_arr}")

# 39. np.log(arr): Element-wise natural logarithm.
log_arr = np.log(math_arr2) # Use math_arr2 to avoid log(0) if arr1 had zeros
print(f"39. np.log(math_arr2):\n{log_arr}")

# 40. arr.sum(): Sum of all elements in the array.
sum_all = math_arr1.sum()
print(f"40. math_arr1.sum(): {sum_all}")

# 41. arr.sum(axis=0): Sum along a specific axis (e.g., columns).
sum_axis_0 = math_arr1.sum(axis=0)
print(f"41. math_arr1.sum(axis=0): {sum_axis_0}")
sum_axis_1 = math_arr1.sum(axis=1)
print(f"   math_arr1.sum(axis=1): {sum_axis_1}")

# 42. arr.mean(): Mean of all elements.
mean_all = math_arr1.mean()
print(f"42. math_arr1.mean(): {mean_all}")

# 43. arr.std(): Standard deviation of all elements.
std_all = math_arr1.std()
print(f"43. math_arr1.std(): {std_all}")

# 44. arr.max(): Maximum element.
max_val = math_arr1.max()
print(f"44. math_arr1.max(): {max_val}")

# 45. arr.min(): Minimum element.
min_val = math_arr1.min()
print(f"45. math_arr1.min(): {min_val}")

# 46. arr.argmax(): Index of the maximum element.
argmax_val = math_arr1.argmax()
print(f"46. math_arr1.argmax(): {argmax_val}") # Flattened index

# 47. arr.argmin(): Index of the minimum element.
argmin_val = math_arr1.argmin()
print(f"47. math_arr1.argmin(): {argmin_val}") # Flattened index

# 48. np.dot(arr1, arr2) or arr1 @ arr2: Dot product of two arrays (matrix multiplication).
dot_product = np.dot(math_arr1, math_arr2)
# Or using the @ operator: dot_product = math_arr1 @ math_arr2
print(f"48. np.dot(math_arr1, math_arr2):\n{dot_product}")


# V. Linear Algebra

print("\n--- V. Linear Algebra ---")
# For inverse and determinant, the matrix must be square and non-singular.
la_matrix = np.array([[4, 7], [2, 6]])
print(f"Linear Algebra matrix:\n{la_matrix}")

# 49. np.linalg.inv(matrix): Compute the (multiplicative) inverse of a matrix.
try:
    inv_matrix = np.linalg.inv(la_matrix)
    print(f"49. np.linalg.inv(la_matrix):\n{inv_matrix}")
except np.linalg.LinAlgError as e:
    print(f"49. Could not compute inverse: {e}")

# 50. np.linalg.det(matrix): Compute the determinant of an array.
det_matrix = np.linalg.det(la_matrix)
print(f"50. np.linalg.det(la_matrix): {det_matrix}")

print("\n--- End of Demonstration ---")
