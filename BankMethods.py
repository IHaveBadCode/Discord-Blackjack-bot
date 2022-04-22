import json

def get_wallet(ID) -> int:
  f = open("Bank.json")
  data = json.load(f)
  return data[ID]["wallet"]

def update_wallet(ID, money) -> None:
  f = open("Bank.json", "r+")
  data = json.load(f)
  data[ID]["wallet"] += money
  f.seek(0)
  json.dump(data, f)
  f.truncate() 

def set_wallet(ID, money) -> None:
  f = open("Bank.json", "r+")
  data = json.load(f)
  data[ID]["wallet"] = money
  f.seek(0)
  json.dump(data, f)
  f.truncate()  

def NewUser(ID):
  file = open("Bank.json", "r+")
  data = json.load(file)
  if str(ID) not in data:
    data[ID] = {"wallet":0, "streak":0}
    print(data)
    file.seek(0)
    json.dump(data, file)
    file.truncate()  
  