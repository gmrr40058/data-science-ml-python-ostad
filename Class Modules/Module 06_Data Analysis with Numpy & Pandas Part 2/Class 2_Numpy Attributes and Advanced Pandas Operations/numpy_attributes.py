# Importing the tools of our heroes
import pandas as pd
import numpy as np

print("\n🎬 Scene 1: Welcome to the Data Cleaning Agency!\n")

print("Meet Pandas Paul and his robot assistant NumPy Neo. Today, they’re on a mission to clean the dirtiest dataset in the city!\n")

# Paul receives a messy dataset
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', np.nan, 'Daisy', 'Ethan'],
    'Age': [25, np.nan, 29, 22, np.nan],
    'Salary': [50000, 60000, np.nan, 58000, 62000]
})

print("📦 Incoming Data:\n", data)

print("\n😱 Paul: 'Neo! This data is full of holes!'")
print("🤖 Neo: 'Relax, Paul. Initiating drop and fill protocols.'")

# Drop rows with any NaNs
data_dropped = data.dropna()
print("\n🧹 After Dropping Rows with NaNs:\n", data_dropped)

# Fill missing data
data_filled = data.fillna({
    'Name': 'Unknown',
    'Age': data['Age'].mean(),
    'Salary': 0
})
print("\n🩹 After Filling Missing Values:\n", data_filled)

# -------------------------------
print("\n🎬 Scene 2: The Shape-Shift Battle\n")

array_rogue = np.array([[1, 2, 3], [4, 5, 6]])
print("🤖 Neo: 'A rogue array is loose!'\nOriginal Array:\n", array_rogue)
print("Shape:", array_rogue.shape)

reshaped_array = array_rogue.reshape(3, 2)
print("\n🔧 Reshaped Array (3x2):\n", reshaped_array)

# -------------------------------
print("\n🎬 Scene 3: FrankenData Monster - Stacking Mayhem!\n")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

v_stacked = np.vstack([a, b])
print("🧱 Vertical Stack:\n", v_stacked)

h_stacked = np.hstack([a, a])
print("\n🧱 Horizontal Stack:\n", h_stacked)

d_stacked = np.dstack([a, a])
print("\n🧱 Depth Stack (3D):\n", d_stacked)

# -------------------------------
print("\n🎬 Scene 4: Lost in the Matrix - Search & Split\n")

big_array = np.arange(10)
print("🧮 Big Array:\n", big_array)

# Splitting
split_arrays = np.split(big_array, 2)
print("\n✂️ Split into two parts:")
for idx, part in enumerate(split_arrays):
    print(f"Part {idx+1}:", part)

# Searchsorted: where would 25 fit?
sorted_array = np.array([10, 20, 30, 40])
pos = np.searchsorted(sorted_array, 25)
print("\n🔍 Where would 25 go in [10, 20, 30, 40]?", pos)

# Where: find all even numbers
evens = np.where(big_array % 2 == 0)
print("🕵️‍♂️ Even numbers found at indices:", evens[0])

# -------------------------------
print("\n🎬 Scene 5: The Grand Finale - Sorting the Clean Data\n")

sorted_data = data_filled.sort_values(by='Salary', ascending=False)
print("💼 Sorted by Salary (Descending):\n", sorted_data)

# -------------------------------
print("\n🎉 Paul: 'Woohoo! Clean, reshaped, stacked, and sorted!'")
print("🤖 Neo: 'Mission accomplished. The data is now strong with logic.'")
print("\n📊 And that, students, is how Pandas Paul and NumPy Neo saved the day!")

print("\n👩‍🏫 Remember: Whether you're dropping NaNs or reshaping arrays — trust in Pandas and NumPy!")



# 1D-2D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)


# 1D-3D
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)


# 2D-1D
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)



# join
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)


# Example
# Join two 2-D arrays along rows (axis=1):

import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)



# ExampleGet your own Python Server
# Split the array in 3 parts:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)



# Access the splitted arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])



# ExampleGet your own Python Server
# Sort the array:

import numpy as np

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))



# Example
# Sort the array alphabetically:

import numpy as np

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))



# Example
# Sort a boolean array:

import numpy as np

arr = np.array([True, False, True])

print(np.sort(arr))



# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

# Example
# Sort a 2-D array:

import numpy as np

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))



# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.

# Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)


# Stacking Along Columns
# NumPy provides a helper function: vstack()  to stack along columns.

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)




# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

# Example
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.dstack((arr1, arr2))

print(arr)