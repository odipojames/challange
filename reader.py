import csv

with open('mock_data.csv') as csvfile:

    m,f = 0,0
    for row in csv.DictReader(csvfile):
        id,first_name,last_name,email,gender =row
        next(csvfile)
        if row["gender"] == 'Male':
            m += 1
        else:
            f += 1


print("Total male = {}".format(m))
print("Total female = {}".format(f))

csvfile.close()
