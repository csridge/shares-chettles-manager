import requests
data = {
    "player_id": "user123",
    "inventory": [
        {"piece": "Queen", "count": 2},
        {"piece": "Knight", "count": 3},
        {"piece": "Bishop", "count": 1},
        {"piece": "Pawn", "count": 8}
    ]
}

response = requests.post("http://127.0.0.1:5003/inventory/update", json=data)

print(response.status_code)
print(response.json())  # Check server response