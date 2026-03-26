#returns only valid activities
#duration must be active
#status must be "active"
activities = [
    {"id":1,"duration":30, "status": "active"},
    {"id":2,"duration":-10, "status": "active"},
    {"id":3,"duration":20, "status": "inactive"},
    {"id":4,"duration":40, "status": "active"}
]
ids = []
for activity in activities:
    if activity["duration"] > 0 and activity["status"] == "active":
        ids.append(activity["id"])
print(ids)        
#-------------------------------------------------------------------------------
#converts valid numbers to integers
#ignores invalid values
#returns the cleaned list
list = ["5", "15", "wrong", "25", "text"]
clean_numbers = []
for numbers in list :
    try:
        clean_numbers.append(int(numbers))
    except ValueError:
        pass    
print(clean_numbers)
#---------------------------------------------------------------------------------
#create a function deposit (balance,amount) that:
#rasises an error if amount is negative or zero otherwise returns the updated balance
balance = 100
def deposit(balance, amount):
    if amount <=0:
        raise ValueError("Amount must be bigger than 0")
    return balance + amount

try:
    new_balance = deposit(balance,50)
    print("updated balance", new_balance)
except ValueError as e:
    print("Error:", e)  
#------------------------------------------------------------------------------------
#Working with string 
# count how many times the word "python" appers (case insesitive)
# replace "python" with "PYTHON"    

text = "Python makes development easier and python is widely used"

count = text.lower().count("python")
print("count", count)

import re
new_text = re.sub(r"python" , "PYTHON" , text , flags=re .IGNORECASE)
print("Updated text:" , new_text)
#-------------------------------------------------------------------------------------
# list transformation 
# using comprehension
# return a list of squares of odd numbers only

numbers = [2, 3, 4, 5, 6]
square_of_odds = []

for x in numbers:
    if x % 2 !=0 :
        square_of_odds.append(x * x)
print(square_of_odds)    
#---------------------------------------------------------------------------------------
#reads a file counts:total-lines , non-empty lines and handles error if file doesnt exist
filename = input("Enter the file name: ")
try:
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    total_lines = len(lines)
    non_empty_lines = 0

    for line in lines:
        if line.strip() != "":
            non_empty_lines += 1
    print("Total lines", total_lines)
    print("Non-Empty lines" , non_empty_lines)
except FileNotFoundError:
    print("Error: File not exist.")  
#-----------------------------------------------------------------------------------------
# user_id must not be none
# scores must be positive
# email must contain "@"
# list of invalid records
# reason for each issue

#i also added for valid records output
records = [
    {"user_id": 1, "score": 80, "email": "user@test.com"},
    {"user_id": 2, "score": -10, "email": "invalid"},
    {"user_id": None, "score": 50, "email": "valid@mail.com"},
]          
invalid_records = []
valid_records = []
for record in records:
    reasons = []
    
    if record["user_id"] is None:
        reasons.append("user_id is none")
    if record["score"] <= 0:
        reasons.append("score is not positive")
    if "@" not  in record["email"]:
        reasons.append("email is invalid")
    if reasons:
        invalid_records.append({"record": record, "reasons" : reasons})
    else:
        valid_records.append(record)

for item in invalid_records:
    print("Record:", item["record"])  
    print("issue", item["reasons"])
    print("---")  

print("valid records:")
for record in valid_records:
    print(record)
#------------------------------------------------------------------------------