def selection_sort(array):
  """Sorts an array using the selection sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  # Iterate over the array, finding the minimum element in the unsorted portion
  # of the array and swapping it with the first element of the unsorted portion.
  for i in range(len(array) - 1):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[j] < array[min_index]:
        min_index = j

    # Swap the minimum element with the first element of the unsorted portion.
    array[i], array[min_index] = array[min_index], array[i]

  # Return the sorted array.
  return array


# Example usage:

array = [5, 3, 8, 6, 7, 2]

# Sort the array using the selection sort algorithm.
sorted_array = selection_sort(array)

# Print the sorted array.
print(sorted_array)
