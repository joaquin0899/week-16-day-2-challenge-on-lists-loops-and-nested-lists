# # School Supply Order Tracking – Logic Challenge

# ## Objective
# Students will apply their understanding of lists, nested lists, slicing, sorting, list grouping, and logical decision-making to solve a real-world data organization problem without using code.

# ---

# ## Scenario
# You are helping the main office organize student supply requests for the week. Each request includes:

# - Student name  
# - Item requested  
# - Quantity requested  

# All requests must be stored together in one organized system.

# ---

# ## Student Tasks (No Coding – Logic Only)

# ### 1. Create Student Requests
# Create a collection that stores information for **3 different student requests**.  
# Each student request must include:
# - Student name  
# - Item requested  
# - Quantity requested  

# ---

name = input("What is your name? ")

item = input("What is the item requested? ")

amount = int(input("How many did you request? "))

list1 = [name, item, amount]

name2 = input("What is your name? ")

item2 = input("What is the item requested? ")

amount2 = int(input("How many did you request? "))

list2 = [name2, item2, amount2]

name3 = input("What is your name? ")

item3 = input("What is the item requested? ")

amount3 = int(input("How many did you request? "))

list3 = [name3, item3, amount3]

all_list = list1, list2, list3


# ### 2. Identify Key Information
# From your collection:
# - Identify the **first student’s name**
# - Identify the **last student’s requested item only**

# ---

print(all_list[0][0])
print(all_list[-1][1])


# ### 3. Quantity Extraction
# Create a **separate list that contains only the quantities requested** by the students.

# ---

second_position_items = [sublist[1] for sublist in all_list]
print(second_position_items)

# ### 4. Order Size Analysis
# Analyze the quantities:
# - If **any quantity is greater than 5**, label the order:
#   “Large order detected!”
# - Otherwise label the order:
#   “Orders within normal limits.”

# ---

third_position = [sublist[2] for sublist in all_list]

print(third_position)

if any(quantity > 5 for quantity in third_position):
    print("Large order detected!")
else:
    print("Orders within normal limits.")




# ### 5. Quantity Organization
# Re-organize the quantity list from **smallest to largest** and display the final result.

# ---


third_position.sort()
print(third_position)


# ## Challenge Extension: Classroom Storage Grid

# You are also given a grid showing classroom supply counts:

# Classroom 1: 8, 12, 5  
# Classroom 2: 7, 3, 9  
# Classroom 3: 10, 6, 4  

# Answer the following:

# 1. What is the **middle number** in the second classroom’s list?
# 2. Create a new list that extracts **only the last number** from each classroom.
# 3. Explain **why this information must be stored as a nested structure instead of a single list.**

# ---

# ## What This Assignment Tests
# - Understanding how grouped data is stored
# - Nested structure reasoning
# - Data extraction using position
# - Organizational logic
# - Real-world decision-making with quantities

# ---

# ## Submission Requirements
# - All answers must be written in words and/or tables.
# - No programming code may be used.
# - Show clear reasoning for each response.

# ---

# ## Academic Integrity
# This is an individual logic and reasoning task. All work must be your own.

# ---

# Instructor: Marvin Evins  
# Course:  AP Computer Science Principles  
