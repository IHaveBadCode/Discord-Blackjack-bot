import json

def get_wallet(member) -> int:
  print(member)
  file = open(f"Banks/{member.guild}.json")
  data = json.load(file)
  wallet = data[f"{member.author.id}"]["wallet"]
  file.close()
  return wallet

def update_wallet(member, money) -> None:
  file = open(f"Banks/{member.guild}.json", "r+")
  data = json.load(file)
  data[f"{member.author.id}"]["wallet"] += money
  file.seek(0)
  json.dump(data, file)
  file.truncate() 
  file.close()

def set_wallet(member, money) -> None:
  file = open(f"Banks/{member.guild}.json", "r+")
  data = json.load(file)
  data[member.author.id]["wallet"] = money
  file.seek(0)
  json.dump(data, file)
  file.truncate()  
  file.close()

def NewUsers(members):  
  file = open(f"Banks/{members[0].guild}.json", "r+")
  data = json.load(file)
  for member in members:
    if str(member.id) not in data:
      print(f"- {member} - added to bank")
      data[member.id] = {"wallet":100, "streak":0}
  file.seek(0)
  json.dump(data, file, indent=4)
  file.truncate()  
  file.close()