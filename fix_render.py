import re

file_path = "web_app.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(
    r'if __name__ == "__main__":[\s\S]*',
    'import os\n\nif __name__ == "__main__":\n    port = int(os.environ.get("PORT", 5000))\n    app.run(host="0.0.0.0", port=port)',
    content
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("FIX COMPLETE")