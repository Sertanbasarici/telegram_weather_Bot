import http.client
import json

class Food:

	querry = ""
	
	def	__init__(self, querry=None):
		if querry is None:
			self.querry = None
		else:
			self.querry = querry.lower()

	def	calories(self):

		conn = http.client.HTTPSConnection("api.collectapi.com")

		headers = {
			'content-type': "application/json",
			'authorization': "apikey 0NiAI18skP45wrwRoPvFXS:4f1ZdUhjyP6mMDqp3IXyUW"
		}
		conn.request("GET", f"/food/calories?query={self.querry}", headers=headers)
		res = conn.getresponse()
		data = res.read()
		conn.close()
		return (json.loads(data))

	def	process_food_data(self, datas):
		result = datas["result"]
		index = 0
		while index < len(result):
			if (result[index]["name"] == self.querry.capitalize()):
				break
			index += 1
		try:
			return result[index]["kcal"]
		except	IndexError:
			print(f"Error: Index {index} is out of range.")
			return f"Error: Index {index} is out of range."

