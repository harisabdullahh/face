from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    try:
        # Check if the 'image' file is in the POST request
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['image']

        # Check if the file has a valid name and extension
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        # You can save the uploaded image to a specific directory
        file.save('/path/to/folder/' + secure_filename(file.filename))

        # Here, you can process the uploaded image using your facial recognition script
        # Replace this with your actual processing logic
        
        # Return a response (you can customize the response as needed)
        return jsonify({'message': 'File uploaded successfully'})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Listen on all available network interfaces
