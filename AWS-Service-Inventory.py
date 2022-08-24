# Week 12 Python Project. Create a list of AWS services. Print it and it's length. Remove two items and print again.

# Create an empty list
import time

aws_services = []

# Append or Input items to your list

aws_services.insert(0, "S3")
aws_services.append('Lambda')
aws_services.append('DynamoDB')
aws_services.append('Cloudwatch')
aws_services.append('EC2')

# Creating a list of AWS services using Python, deleting items, and printing the new list

#aws_services += ['S3', 'Lambda', 'DynamoDB', 'Cloudwatch', 'EC2']

print("Here's my list of AWS services!")
time.sleep(2)
print(aws_services)
time.sleep(2)
print("Now I will delete a couple of items from the list-")
time.sleep(2)
del aws_services[0]
del aws_services[3]
print(aws_services)
print("I narrowed it down to", len(aws_services), "items.")
time.sleep(2)
print("LUIT!")