from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'  # Replace with your actual API key

def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['user_message']
    response = generate_response(user_message)
    return {'message': response}

if __name__ == '__main__':
    app.run(debug=True)
