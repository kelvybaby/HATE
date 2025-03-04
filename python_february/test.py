import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Check Python interpreter
print("✅ Python is working!")
print("Python Executable Path:", sys.executable)

# NumPy test
array = np.random.rand(3, 3)
print("\n✅ NumPy is working! 3x3 Random Matrix:")
print(array)

# Pandas test
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df = pd.DataFrame(data)
print("\n✅ Pandas is working! Sample DataFrame:")
print(df)

# Matplotlib test
plt.figure(figsize=(4, 2))
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o', linestyle='--', color='b')
plt.title("✅ Matplotlib Test Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
