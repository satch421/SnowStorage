# ewise_progrmgmt = pete@ewise-health.awsapps.com

print("We are saving  all data more recent than <timestamp>?", end='  ')
savestamp = input()
print("What is the IP address for this source?", end='  ')

sourceIP = input()
print("What is the access password for this source?", end='  ')
sourcePW = input()

print(f"Connecting Snow device and {sourceIP} ...!")
print(f"Searching for data more recent than {savestamp} ...!")

print(f"Transfering data more recent than {savestamp} from {sourceIP} to Snow device ...!")


print("Data transfer complete.")
print(f"Terminating connection with {sourceIP}")



print(f"Who is the administrator to handle the data from {sourceIP}?", end='  ')
dataAdmin = input()
print(f"{dataAdmin} works in which department?", end='  ')
adminDept = input()

print(f"What is {dataAdmin}'s phone?", end='  ')
dataAdmin_phone = input()
print(f"What is {dataAdmin}'s email address?", end='  ')
dataAdmin_email = input()

print(f"We have recorded this information in our Snow device database for {sourceIP}.")

# send this email to {dataAdmin_email}


print (f"Data for your {dataAdmin} patients has been saved to Deep Storage.")
