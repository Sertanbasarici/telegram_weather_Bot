import http.client
import json

class Weather:

	city = ""
	lang = ""

	def __init__(self, city=None, lang=None):
		if city is None and lang is None:
			self.city = "istanbul"
			self.lang = "tr"
		else:
			self.city = city.lower()
			self.lang = lang.lower()

	def getWeather(self):
		connection = http.client.HTTPSConnection("api.collectapi.com")
		headers = {
			'content-type': "application/json",
			'authorization': "apikey 0NiAI18skP45wrwRoPvFXS:4f1ZdUhjyP6mMDqp3IXyUW" }
		connection.request("GET", f"/weather/getWeather?data.lang={self.lang}&data.city={self.city}", headers=headers)
		response = connection.getresponse()
		data = response.read().decode("utf-8")
		connection.close()
		#weather_data = json.loads(data)
		#return json.dumps(weather_data, ensure_ascii=False)
		return (json.loads(data))

	def getDays(self, datas):
		result = datas["result"]
		day_list = []
		index = 0
		while index < len(result):
			day_list.append(result[index]["day"])
			index += 1
		return day_list

	def getCond(self, datas):
		result = datas["result"]
		cond_list = []
		index = 0
		while index < len(result):
			cond_list.append(result[index]["description"])
			index += 1
		return cond_list

	def getDegree(self, datas):
		result = datas["result"]
		temp_list = []
		index = 0
		while index < len(result):
			temp_list.append(result[index]["degree"])
			index += 1
		return temp_list

	def getHumidity(self, datas):
		result = datas["result"]
		humidity_list = []
		index = 0
		while index < len(result):
			humidity_list.append(result[index]["humidity"])
			index += 1
		return humidity_list

	def getAlltogether(self, datas):
		result = datas["result"]
		weather_dict = {}
		days = self.getDays(datas)
		cond = self.getCond(datas)
		degree = self.getDegree(datas)
		humidity = self.getHumidity(datas)
		index = 0
		while index < len(result):
			weather_dict[days[index]] = [cond[index], degree[index], humidity[index]]
			index += 1
		return weather_dict