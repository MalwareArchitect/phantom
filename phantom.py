import requests
import time
import json
from pyfiglet import figlet_format

print("\nCreated by AlgorithmNerd")
print(figlet_format("PHANTOM", font = "doom"))

phone_number = input("Phone Number: ")
text_message = input("Message: ")
custom_key = input("Key: ")

webhook_question = input("Would you like to receive reply messages? yes/no\n")
if webhook_question == 'yes':
	webhook_url = input("Webhook URL: ")
	resp = requests.post('https://textbelt.com/text', {
  		'phone': phone_number,
  		'message': text_message,
  		'replyWebhookUrl': webhook_url,
  		'key': custom_key,
	})
else:
	webhook_url = " "
	resp = requests.post('https://textbelt.com/text', {
  		'phone': phone_number,
  		'message': text_message,
		'replyWebhookUrl': webhook_url,
  		'key': custom_key,
	})

result = resp.json()
list_values = list(result.values())

print("\nSending Message...")

time.sleep(2)

if True in list_values:
	print("\nMessage Successful")
	time.sleep(1)
	print("\nText ID: {}".format(list_values[1]))
	print("Credits Available: {}".format(list_values[2]))
elif 'Invalid phone number or bad request. If your phone number contains a +, please check that you are URL encoding it properly.' in list_values:
	print("\nMessage Failed")
	print("\nError: Invalid Phone Number")
elif 'Out of quota' in list_values:
	print("\nMessage Failed")
	print("\nError: Out of Credits")
else:
	print("\nMessage Failed")

message_2 = input("\nWould you like to send another message? yes/no\n")

while message_2 == 'yes':
	message_updated = input("\nMessage: ")
	resp = requests.post('https://textbelt.com/text', {
  		'phone': phone_number,
  		'message': message_updated,
  		'replyWebhookUrl': webhook_url,
  		'key': custom_key,
	})
	result = resp.json()
	list_values = list(result.values())

	print("\nSending Message...")

	time.sleep(2)

	if True in list_values:
		print("\nMessage Successful")
		time.sleep(1)
		print("\nText ID: {}".format(list_values[1]))
		print("Credits Available: {}".format(list_values[2]))
	elif 'Invalid phone number or bad request. If your phone number contains a +, please check that you are URL encoding it properly.' in list_values:
		print("\nMessage Failed")
		print("\nError: Invalid Phone Number")
	elif 'Out of quota' in list_values:
		print("\nMessage Failed")
		print("\nError: Out of Credits")
	else:
		print("\nMessage Failed")
		print("\nThank you for using Phantom")
	message_2 = input("\nWould you like to send another message? yes/no\n")
else:
	print(" ")
	print(figlet_format("Goodbye", font = "small"))




