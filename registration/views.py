from django.shortcuts import render
from registration.models import Customer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.

statusNOK = 'NOK'
statusOK = 'OK'
result = ''

def registerCustomer(request, id, name, email, phone, password):
	recordPresent = True
	try:
		customer = Customer.objects.get(customer_email = email)
	except Customer.DoesNotExist:
		recordPresent = False
	try:
		customer = Customer.objects.get(customer_phone = phone)
		recordPresent = True
	except Customer.DoesNotExist:
		pass
	if(recordPresent):
		json_object=getJSON(statusNOK,'Already Registered')
	else :
		customer = Customer(customer_id=id, customer_name=name, customer_email=email, customer_phone=phone,customer_password=password)
		customer.save()
		json_object=getJSON(statusOK,'Successful Registration')
	return JsonResponse(json_object)

def loginEmail(request, email, password):
	customer = get_object_or_404(Customer, customer_email=email)
	json_object = login(customer,password)
	return JsonResponse(json_object)

def loginPhone(request, phone, password):
	get_object_or_404(Customer,customer_phone=phone)
	json_object = login(customer,password)
	return JsonResponse(json_object)

def loginFBOrGPlus(request, id):
	customer = get_object_or_404(Customer,pk=id)
	getCustomerInfo(customer)
	json_object = getJSON(statusOK , result)
	return JsonResponse(json_object)

def forgotPasswordEmail(request, email, password):
	customer = get_object_or_404(Customer, customer_email=email)
	return JsonResponse(changePassword(customer,password))
	
def forgotPasswordPhone(request, phone,password):
	customer = get_object_or_404(Customer, customer_phone=phone)
	return JsonResponse(changePassword(customer,password))
	
def changePassword(customer,password):
	customer.password = password 
	customer.save()
	json_object = getJSON(statusOK,"Password change successful")
	return json_object


def login(customer,password):
	registeredPassword = customer.customer_password
	if password == registeredPassword:
		getCustomerInfo(customer)
		json_object = getJSON(statusOK,result)
	else : 
		json_object = getJSON(statusNOK,'Wrong Password')
	return json_object

def getCustomerInfo(customer):
	global result 
	result = {
				'id' : customer.customer_id,
				'name' : customer.customer_name,
				'email' : customer.customer_email,
				'phone' : customer.customer_phone,				
				}  

def getJSON(status, message):
	json_object = {
			'status' : status,
			'result' : message
		}
	return json_object

def error404(request):
	json_object = getJSON(statusNOK,'Not Registered')
	return JsonResponse(json_object)

def error500(request):
	json_object = getJSON(statusNOK,'Server Down')
	return JsonResponse(json_object)