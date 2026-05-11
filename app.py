import os
from flask import Flask, render_template
from dotenv import load_dotenv
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# --- CloudBees Feature Management (Rox) Configuration ---

class Flags:
    def __init__(self):
        # Flag to control the visibility of the New Tournament Button
        self.show_new_tournament_button = RoxFlag(False)

# Initialize the flags container
flags = Flags()

# Register the app container with CloudBees
Rox.register(flags)

# Retrieve the SDK key from environment variables
sdk_key = os.getenv("ROX_SDK_KEY")

if sdk_key:
    # Initialize the connection to CloudBees Unify
    Rox.setup(sdk_key).result()
else:
    print("⚠️ WARNING: ROX_SDK_KEY not found in environment variables.")

# --- Route Definitions ---

@app.route('/')
def home():
    """Renders the main landing page."""
    return render_template(
        'index.html', 
        show_new_tournament_button=flags.show_new_tournament_button.is_enabled()
        )

@app.route('/new')
def new():
    """Placeholder route for creating a new tournament."""
    return render_template('construction.html', title="New Tournament")

@app.route('/my-tournaments')
def my_tournaments():
    """Placeholder route for viewing saved tournaments."""
    return render_template('construction.html', title="My Tournaments")

if __name__ == '__main__':
    # Run the server on local port 8000
    app.run(port=8000, debug=True)