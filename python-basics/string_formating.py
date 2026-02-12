# Name : Dawood Adams
# Date : 12/02/2026
# string formating
# get string length
sentence = "I watch football"
string_length = len(sentence)
print(f"The length is:{string_length}")
# Splitting a string
sentence_2 = "Mathematics Physics Chemistry German"
split = sentence_2.split(" ")
print(f"the first subject is: ", split[0])
print(f"The second subject is: ", split[1])
print(f"The third subject is: ", split[2])
print(f"The fourth subject is: ", split[3])
string_length2 = len(sentence_2)

print(f"The length is:{string_length2}")
# Make everything a capital letter
mpesa_code = "uf76iokp67t"
capitalized = mpesa_code.upper()
print(f"New Mpesa code: ", capitalized)
lower_case = mpesa_code.lower()
print(f"New Mpesa code: ", lower_case)
# Replacing characters in a string 
balance = "100Kes"
amount_added = "50Kes"
cleaned_balance = balance.replace("Kes", "")
print("Cleaned balance: ", cleaned_balance)
cleaned_amount_added =amount_added.replace("Kes", "")
print("Cleaned amount added: ", cleaned_amount_added)
new_balance = int(cleaned_amount_added) + int(cleaned_balance)
print(f"New MPESA balance is: ", new_balance)
end = "Kes"
new_balance_complete = str(new_balance) + str(end)
print(f" CONFIRMED, you have received {amount_added} from Phillip.Your new MPESA balance is {new_balance_complete} ")


