import json
import requests
from fnexchange.core.plugins import AbstractPlugin


class FreshdeskPlugin(AbstractPlugin):#change ticket id to id in payload later 
	
	def create_ticket(self,payload):# Was earlier going into spam since deleted contacts go into spam
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			response = requests.post(self.config.url,auth=(self.config.api_key,"x"),headers=headers,data = json.dumps(elements[0]))
			
			success=False
			if response.status_code == 201:
			  success= True 
			else:
			  success= False
						
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	
	def update_ticket(self,payload):#Put method is not allowed apparently, error 405--Couldnt update spam messages, see above,still not working
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			ticket_id=str(elements[1]["ticket_id"])
			response = requests.put(self.config.url+'/'+ ticket_id, auth = (self.config.api_key,"x"), headers = headers, data = json.dumps(elements[0]))
			
			if response.status_code==200:
				success= True
			else:
				success= False	
			
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	
	def delete_ticket(self,payload):#Delete method is not allowed apparently, error 405-- error 405--Couldnt delete spam messages, see above
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			ticket_id=str(elements[0]["ticket_id"])
			response=requests.delete(self.config.url+'/'+ ticket_id, auth = (self.config.api_key,"x"), headers = headers)
			
			if response.status_code==204:
			   success= True
			else:
			   success= False
						
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	def restore_ticket(self,payload):#'https://domain.freshdesk.com/api/v2/tickets/1/restore'
			elements=payload["elements"]
			headers={'Content-Type':'application/json'}
			ticket_id=str(elements[0]["ticket_id"])
			response=requests.put(self.config.url+'/'+ticket_id+'/restore', auth = (self.config.api_key,"x"), headers = headers)
			
			if response.status_code==204:
				success= True
			else:
				success= False	
			
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
	
	def view_ticket(self,payload):#Working
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			ticket_id=str(elements[0]["ticket_id"])
			
			response=requests.get(self.config.url+'/'+ ticket_id,auth= (self.config.api_key,'x'), headers=headers)	
			
			return response.content
	
	def create_contact(self,payload): #Working
			headers = { 'Content-Type' : 'application/json' } 
			elements=payload["elements"]
			contact_info=elements[0]["contact_info"]
			
			response = requests.post(self.config.url1,auth=(self.config.api_key,"x"), headers=headers,data = json.dumps(contact_info))
			
			if response.status_code==201:
				success= True
			else:
				success= False	
			
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}

	def view_contact(self,payload):#Working
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			contact_id=str(elements[0]["contact_id"])			
			response=requests.get(self.config.url1+'/'+ contact_id,auth= (self.config.api_key,'x'), headers=headers)
			return response.content

	def delete_contact(self,payload): #Working 
			headers = { 'Content-Type' : 'application/json' }
			elements=payload["elements"]
			contact_id=str(elements[0]["contact_id"])
			
			response = requests.delete(self.config.url1+'/'+contact_id,auth=(self.config.api_key,"x"), headers=headers)
			
			if response.status_code==204:
				success= True
			else:
				success= False	
			print "Status Code :" + str(response.status_code)
			
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}
			
	def update_contact(self,payload):#Put method is not allowed apparently, error 405--Couldnt update spam messages, see above,still not working
			headers = { 'Content-Type' : 'application/json' }
			elements = payload["elements"]
			contact_id=str(elements[1]["contact_id"])
			
			response = requests.put(self.config.url1+'/'+contact_id, auth = (self.config.api_key,"x"), headers = headers, data = json.dumps(elements[0]["contact_info"]))

			if response.status_code == 200:
			   success= True
			else:
			   success= False
			print "Status Code : " + str(response.status_code)
			
			return {
				'metadata': {
					'success': success
				},
				'elements': elements  # return the same thing back
			}