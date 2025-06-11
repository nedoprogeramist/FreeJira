from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

issues = [
	{"id": 1, "key": "DPO-777", "status": "todo", "owner": "user1"},
	{"id": 2, "key": "DPO-778", "status": "todo", "owner": "user2"},
	{"id": 3, "key": "DPO-779", "status": "todo", "owner": "user3"},
]

@app.get("/items/{id}")
async def read_id(id: int):
	for issue_id in issues:
		if issue_id['id'] == id:
			return issue_id
		return {"error": "Item not found"}
	
@app.get("/items/key/{key}")
async def read_keys(key: str):
	for issue_key in issues:
		if issue_key['key'] == key:
			return issue_key
		return {"error": "Item not found"}
