import json

jsonText = '''
{
	"std000001":{
		"id":"std000001",
		"name":"Hong gil dong",
		"mail":"gildong@gmail.com",
		"address":"Korea seoul",
		"age":"50",
		"hobbys":["sport", "music", "cook"],
		"active":true
	},
	"std000002":{
		"id":"std000002",
		"name":"Park se ri",
		"mail":"seri@gmail.com",
		"address":"Korea daejeon",
		"age":"40",
		"hobbys":["music", "cook"],
		"active":false
	},
	"std000003":{
		"id":"std000003",
		"name":"Son heun min",
		"mail":"son@gmail.com",
		"address":"Korea jeju",
		"age":"30",
		"hobbys":["music"],
		"active":true
	}
}
'''

jsonData = json.loads(jsonText)
print(f'jsonData: {jsonData}')

print(f'id: {jsonData["std000001"]["id"]}')
print(f'name: {jsonData["std000001"]["name"]}')
print(f'mail: {jsonData["std000001"]["mail"]}')
print(f'address: {jsonData["std000001"]["address"]}')
print(f'age: {jsonData["std000001"]["age"]}')
for idx, hobby in enumerate(jsonData["std000001"]["hobbys"]):
    print(f'idx: {idx}, \t hobby: {hobby}')
print(f'active: {jsonData["std000001"]["active"]}')

print(f'id: {jsonData["std000002"]["id"]}')
print(f'name: {jsonData["std000002"]["name"]}')
print(f'mail: {jsonData["std000002"]["mail"]}')
print(f'address: {jsonData["std000002"]["address"]}')
print(f'age: {jsonData["std000002"]["age"]}')
for idx, hobby in enumerate(jsonData["std000002"]["hobbys"]):
    print(f'idx: {idx}, \t hobby: {hobby}')
print(f'active: {jsonData["std000002"]["active"]}')

print(f'id: {jsonData["std000003"]["id"]}')
print(f'name: {jsonData["std000003"]["name"]}')
print(f'mail: {jsonData["std000003"]["mail"]}')
print(f'address: {jsonData["std000003"]["address"]}')
print(f'age: {jsonData["std000003"]["age"]}')
for idx, hobby in enumerate(jsonData["std000003"]["hobbys"]):
    print(f'idx: {idx}, \t hobby: {hobby}')
print(f'active: {jsonData["std000003"]["active"]}')