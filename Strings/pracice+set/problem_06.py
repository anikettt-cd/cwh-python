# a = " hey my name is aniket, what is your name?"

# sum = 0
# vowels = ["a", "e", "i", "o", "u"]

# for char in a:
#     if(char in vowels):
#         sum+=1

# print(f" there are {sum} vowels in the string")

# str1 = "madam"

# if(str1 == str1[::-1]):
#     print("the string is a palindrome")
# else:
#     print("the string is not palindrome")
    
# import matplotlib.pyplot as plt
# import numpy as np

# # Data for plotting
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # Create the plot
# plt.plot(x, y, label='Sine Wave', color='blue')

# # Add decorations
# plt.title("Simple Sine Plot")
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.legend()

# # Show the result
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load a built-in dataset
tips = sns.load_dataset("tips")

# Create a boxplot of total bill by day
sns.boxplot(data=tips, x="day", y="total_bill", palette="Set2")

plt.show()
   
    




 