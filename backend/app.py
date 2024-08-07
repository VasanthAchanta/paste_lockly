from flask import Flask, request, jsonify
from cryptography.fernet import Fernet
import sqlite3
import base64

app = Flask(__name__)
DATABASE = 'your_database.db'

@app.route('/api/create', methods=['POST'])
def create_snippet():
    data = request.get_json()
    text = data['text']
    key = data.get('key')

    if key:
        # Ensure key is properly handled as bytes
        fernet = Fernet(Fernet.generate_key())
        encrypted_text = fernet.encrypt(text.encode())
        key = fernet._signing_key.decode()  # Encode key to store as text
    else:
        encrypted_text = text
        key = None

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO snippets (text, key) VALUES (?, ?)', (encrypted_text, key))
        snippet_id = cursor.lastrowid
        conn.commit()

    return jsonify({'url': f'http://localhost:4200/view/{snippet_id}'}), 201

@app.route('/api/view/<int:id>', methods=['POST'])
def view_snippet(id):
    data = request.get_json()
    provided_key = data.get('key')

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT text, key FROM snippets WHERE id = ?', (id,))
        snippet = cursor.fetchone()

    if not snippet:
        return jsonify({'error': 'Snippet not found'}), 404

    encrypted_text, stored_key = snippet
    if stored_key:
        if not provided_key:
            return jsonify({'error': 'Key is required'}), 401

        # Decode provided_key from base64
        try:
            provided_key = base64.urlsafe_b64decode(provided_key)
            fernet = Fernet(provided_key)
            decrypted_text = fernet.decrypt(encrypted_text).decode()
        except Exception as e:
            return jsonify({'error': str(e)}), 401
    else:
        decrypted_text = encrypted_text

    return jsonify({'text': decrypted_text}), 200 