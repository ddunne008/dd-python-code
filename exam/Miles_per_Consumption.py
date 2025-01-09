import sys # I believe that for the file to be accessed it would use the Import sys module and then to allow command line arguments, sys.argv
# This code file is a WIP. Unfortuntely could not program it to read the external file so I have added the contents as a list called 'data'
data = [57.4, 62.3, 58.9, 48.9, 55.0]

m = max(data)
av = sum(data) / len(data)

print(f"The Largest number of miles per gallon consumption is {m}")
print(f"the Average number of miles per gallon consumption is {av}")

