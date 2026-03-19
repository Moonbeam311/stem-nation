file = "web_app.py"

with open(file, "r", encoding="utf-8") as f:
    content = f.read()

if "@app.route('/test-live')" not in content:
    insert_point = content.rfind("if __name__ == \"__main__\":")
    
    route_code = """

@app.route('/test-live')
def test_live():
    return "LIVE CODE UPDATED"
"""

    content = content[:insert_point] + route_code + "\n" + content[insert_point:]

with open(file, "w", encoding="utf-8") as f:
    f.write(content)

print("TEST ROUTE INSTALLED")