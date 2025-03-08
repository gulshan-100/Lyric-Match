from flask import Flask, render_template, request, jsonify
from openai import OpenAI  
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# List of song titles
SONG_TITLES = [
    "Shape of You", "Someone Like You", "Bohemian Rhapsody", "Blinding Lights",
    "Rolling in the Deep", "Smells Like Teen Spirit", "Billie Jean", "Hotel California",
    "Thinking Out Loud", "Let It Be", "Hallelujah", "Sweet Child O' Mine",
    "Wonderwall", "Take Me to Church", "Hey Jude", "Uptown Funk",
    "Shallow", "Livin' on a Prayer", "Don't Stop Believin'", "Bad Guy"
]

# Function to generate a lyric snippet
def generate_lyric_snippet():
    song_title = random.choice(SONG_TITLES)
    prompt = f"Generate 2-4 lines of lyrics from the song '{song_title}' without mentioning its title."
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",  
            messages=[{"role": "user", "content": prompt}]
        )
        lyrics = response.choices[0].message.content.strip()
        return song_title, lyrics
    except Exception as e:
        print(f"Error generating lyrics: {e}")
        return None, None

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# API Endpoint to generate lyrics
@app.route('/generate', methods=['GET'])
def get_lyric_snippet():
    song_title, lyrics = generate_lyric_snippet()
    if song_title and lyrics:
        return jsonify({"lyrics": lyrics, "song_title": song_title})
    else:
        return jsonify({"error": "Failed to generate lyrics"}), 500

# API Endpoint to check the user's answer
@app.route('/check', methods=['POST'])
def check_answer():
    data = request.json
    user_guess = data.get("guess", "").strip().lower()
    correct_title = data.get("song_title", "").strip().lower()
    
    if user_guess == correct_title:
        return jsonify({"correct": True, "message": "Correct! Well done!"})
    else:
        return jsonify({"correct": False, "message": f"Incorrect! The correct answer was '{correct_title}'."})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)