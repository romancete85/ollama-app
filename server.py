import os
from flask import Flask, request, render_template_string
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)  # QA Test deployment

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url=os.environ.get("LLM_ENDPOINT")
)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Poem Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 600px;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            resize: none;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #0056b3;
        }
        .poem {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #f9f9f9;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Poem Generator</h1>
        <form method="POST">
            <textarea name="input" rows="4" cols="50" placeholder="Enter your prompt..."></textarea>
            <button type="submit">Generate Poem</button>
        </form>
        {% if poem %}
        <h2>Your AI-Generated Poem:</h2>
        <pre>{{ poem }}</pre>
        {% endif %}
    </div>
</body>
</html>
"""
@app.route("/" , methods=["GET", "POST"])
def index():
    poem = None
    if request.method == "POST":
        try:
            input_message = request.form["input"]

            response = client.chat.completions.create(
                model=os.environ.get("MODEL"),
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that creates poems."},
                    {"role": "user", "content": input_message}
                ]
            )
            poem = response.choices[0].message.content

        except Exception as e:
            print(f"Error:{str(e)}")
            poem = "An error occurred while generating the poem."

    return render_template_string(HTML_TEMPLATE, poem=poem)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0" , port=port)