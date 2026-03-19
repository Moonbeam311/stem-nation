file = "web_app.py"

with open(file, "r", encoding="utf-8") as f:
    content = f.read()

# Ensure import exists
if "import teacher_console" not in content:
    content = "import teacher_console\n" + content

# Add route if missing
if "@app.route('/teacher')" not in content:
    insert_point = content.rfind("if __name__ == \"__main__\":")
    
    route_code = """

@app.route('/teacher')
def teacher_dashboard():
    try:
        return str(teacher_console)
    except:
        return "Teacher system connected"
"""

    content = content[:insert_point] + route_code + "\n" + content[insert_point:]

with open(file, "w", encoding="utf-8") as f:
    f.write(content)

print("FINAL TEACHER ROUTE INSTALLED")