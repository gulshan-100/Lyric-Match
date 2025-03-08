# Lyric Match - Guess the Song!

Lyric Match is a fun web-based game where players guess the song title based on a snippet of its lyrics. The game uses the OpenAI API to generate lyric snippets dynamically and checks the user's guess against the correct song title.

## Features
* Dynamic Lyric Generation: Uses OpenAI's GPT-4 (or GPT-3.5-turbo) to generate lyric snippets from popular songs.
* Interactive Gameplay: Users can guess the song title and get instant feedback on their answer.
* Responsive Design: Built with Bootstrap for a clean and mobile-friendly interface.
* Error Handling: Robust error handling for both frontend and backend.

## Technologies Used
### Frontend:
* HTML, CSS, JavaScript
* Bootstrap 5 for styling

### Backend:
* Flask (Python) for the server
* OpenAI API for lyric generation

### Other Tools:
* dotenv for environment variable management
* fetch API for frontend-backend communication

### Setup and Installation
#### Prerequisites
* Python 3.8+: Ensure Python is installed on your system.
* OpenAI API Key: Sign up at OpenAI and get your API key.
* Git: To clone the repository.

### Steps
1. Clone the repository:
```bash
git clone https://github.com/your-username/lyric-match.git
cd lyric-match
```

2. Set Up a Virtual Environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies:
```bash
pip install -r requirements.txt
```
4. Set Up Environment Variables:
Create a .env file in the root directory and add your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```
5. Run the Flask App:
```bash
python app.py
```
6. Access the Application:
Open your browser and navigate to http://127.0.0.1:5000.

### Screenshot Demo 
![Screenshot (383)](https://github.com/user-attachments/assets/fbc30326-a06f-4521-9d64-f5a46217b8fc)



