# PasteLockly

PasteLockly is a web application that allows users to anonymously share text snippets. Users can create shareable URLs for their snippets and optionally encrypt them with a secret key. Viewers must provide the secret key to decrypt and view the content.

## Features

1. **Create Snippet**: A form where users can enter text snippets and create a shareable URL.
2. **Shareable URL**: Generates a unique URL that leads to a view-only snippet.
3. **Optional Encryption**: Allows the snippet creator to add a secret key for encrypting the content.
4. **Decryption on Viewing**: Requires the viewer to provide the secret key to decrypt and view the content.

## Technologies Used

- **Frontend**: Angular
- **Backend**: Python with Flask
- **Database**: SQLite
- **Encryption**: `cryptography` package

## Installation and Setup

### Prerequisites

- Node.js and npm
- Python and pip

### Frontend Setup

1. Install Angular CLI:
   ```sh
   npm install -g @angular/cli

2.	Clone the repository and navigate to the frontend directory:

    git clone https://github.com/yourusername/pastelockly.git
    cd pastelockly/frontend

3.	Install Angular dependencies:
    npm install

4.	Start the Angular development server:
    ng serve
    The Angular app should now be running on http://localhost:4200.

### Backend Setup    

1.	Navigate to the backend directory:
    cd ../backend
2.	Start the Flask development server:  
    python app.py
    The Flask API should now be running on http://localhost:5000.

### Usage

	1.	Open the Angular app in your browser at http://localhost:4200.
	2.	Use the form to create a new snippet. Optionally, you can provide a secret key to encrypt the snippet.
	3.	A shareable URL will be generated. Share this URL with others.
	4.	Viewers can visit the URL and, if the snippet is encrypted, provide the secret key to decrypt and view the content.

