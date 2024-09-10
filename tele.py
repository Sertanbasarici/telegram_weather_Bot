import http.client
import json
import urllib.parse

class Telebot:

	token = ""
	chat_id = ""
	def	__init__(self, token):
		self.token = token

	def sendMessage(self, chat_id, text):
		host = 'api.telegram.org'
		if not isinstance(text,str):
			data = json.dumps(text, ensure_ascii=False)
		else:
			data = text
		path = f'/bot{self.token}/sendMessage?chat_id=' + str(chat_id) + "&" + "text=" + urllib.parse.quote(data)
		connection = http.client.HTTPSConnection(host)
		connection.request("POST", path)
		response = connection.getresponse()
		data = response.read().decode('utf-8')
		connection.close()

	def getUpdates(self, offset=None, string=None):
		host = 'api.telegram.org'
		path = f'/bot{self.token}/getUpdates?timeout=100'
		if offset:
			path += f"&offset={offset}"
		connection = http.client.HTTPSConnection(host)
		connection.request("GET", path)
		response = connection.getresponse()
		data = response.read().decode('utf-8')
		connection.close()
		return (json.loads(data))

	def offset_id(self, updates):
		result = updates['result']
		index = 0
		if result and len(result) > index:
			result_1 = result[index]['update_id']
		else:
			result_1 = 0
		while index < len(result):
			if result_1 < result[index]['update_id']:
				result_1 = result[index]['update_id']
			index += 1
		return result_1 + 1

	def	last_sended_text(self, updates):
		result = updates['result']
		if result and len(result) > 0:
			result_1 = result[len(result) - 1]['message']
			output = result_1['text']
		else:
			output = None
			print("No entry")
		return output

	def	getChatid(self, updates):
		result = updates['result']
		index = 0
		if result and len(result) > index:
			id = result[index]["message"]["chat"]["id"]
		else:
			id = 0
		while index < len(result):
			id = result[index]["message"]["chat"]["id"]
			index += 1
		return id