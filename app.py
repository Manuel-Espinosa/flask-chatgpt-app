import os
import logging
from flask import Flask, request, render_template, jsonify
import openai

app = Flask(__name__)

# Load your OpenAI API key from the environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def send_question():
    # Get the question from the request data
    data = request.get_json()
    question = data.get('question', '')

    # Check if the question is empty
    if not question:
        return jsonify({'error': 'Question is required'}), 400

    # Check if the API key is set
    if not openai.api_key:
        logger.error('OpenAI API key is missing or not configured')
        return render_template('index.html', error='OpenAI API key is not configured')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question},
            ]
        )

        answer = response.choices[0].message['content']

        # Log the API call and response
        logger.info(f'API Call: question="{question}", answer="{answer}"')

        return jsonify({'answer': answer})

    except Exception as e:
        logger.error(f'Error: {str(e)}')
        return render_template('index.html', error=str(e))  # Pass the error message to the template

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)