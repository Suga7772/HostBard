from flask import Flask, request, jsonify
from bardapi import Bard

app = Flask(__name__)
token = 'eQghP69SLSffZ7L0MO6XoHpec4S1eyS9SJu27fPxqyRRssSWCcVjXkoBoLaGQyuhNzis5A.'
bard = Bard(token=token)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    query = request.json.get('query')
    response = bard.get_answer(query)['content']
    return jsonify({'response': response})

@app.route('/image_description', methods=['POST'])
def image_description():
    image_data = request.files.get('image')
    if image_data:
        image_bytes = image_data.read()
        bard_answer = bard.ask_about_image('What is in the image ', image_bytes)
        return jsonify({'description': bard_answer['content']})
    else:
        return jsonify({'error': 'No image provided.'}), 400

@app.route('/', methods=['GET'])
def home():
        return 'Wound Model Chatbot'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
