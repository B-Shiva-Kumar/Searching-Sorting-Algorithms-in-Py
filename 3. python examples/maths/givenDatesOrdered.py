# Method 1: using datetime module and lambda function
# importing datetime
from datetime import datetime

datedList = ["04-1967", "10-2012", "06-2012", "01-1989", "12-2000", "08-1947"]
datedList.sort(key=lambda date: datetime.strptime(date, "%m-%Y"))
print("The input list of date strings after sorting:\n", datedList)

# output
# The input list of date strings after sorting:
#  ['08-1947', '04-1967', '01-1989', '12-2000', '06-2012', '10-2012']

# ---

# Method 2

# input list of date strings
inputDateList = ['06-2014', '08-2020', '4-2003', '04-2005', '10-2002', '12-2021']

def orderedDates(DatesList):
    split_up = DatesList.split("-")

    return split_up[1], split_up[0]

# sort() sorted the splited dates
inputDateList.sort(key=orderedDates)
print(inputDateList)
# output -> ['10-2002', '4-2003', '04-2005', '06-2014', '08-2020', '12-2021']


# ---

# Method 3
# NOTE: 
# sort() will sort the list in-place, mutating its indexes and returning None 
# whereas sorted() will return a new sorted list leaving the original list unchanged

inputDateList = ['06-2014', '08-2020', '4-2003', '04-2005', '10-2002', '12-2021']

def OrdDates(DatesList):
    splitDates = DatesList.split("-")
    return splitDates[1], splitDates[0]

sortedDates = sorted(inputDateList, key=OrdDates)
print(sortedDates)
# output -> ['10-2002', '4-2003', '04-2005', '06-2014', '08-2020', '12-2021']


# ---

# Method 4
inputDateList = ['06-2014', '08-2020', '04-2003', '04-2005', '10-2002', '12-2021', "11-2021"]

ans = []
for i in inputDateList:
    splitDate = i.split("-")
    temp = "-".join(splitDate[::-1])
    ans.append(temp)
ans.sort()
print(ans)

for i in ans:
    splitDate = i.split("-")
    temp = "-".join(splitDate[::-1])
    print(temp)