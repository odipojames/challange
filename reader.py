import pandas as pd
df = pd.read_csv("mock_data.csv")
males = 0
females = 0
p = pd.notnull(df['first_name']).sum()#to get Total
gender_column = df['gender']
for row in gender_column:
    if row == "Male":
        males += 1
    else:
        females += 1

print("The males are "+str(males))
print("The females are "+str(females))
print("Total students "+str(p))
