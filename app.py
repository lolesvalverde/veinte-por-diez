import os
from flask import Flask, render_template
from dotenv import load_dotenv
from rox.server.rox_server import Rox
from rox.server.flags.rox_flag import RoxFlag
from models import db

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tournaments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize database with app
db.init_app(app)

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

# Create database tables
with app.app_context():
    db.create_all()

# --- Register Blueprints ---
from routes.tournament_routes import tournament_bp
from routes.player_routes import player_bp
app.register_blueprint(tournament_bp)
app.register_blueprint(player_bp)

# --- Route Definitions ---

@app.route('/')
def home():
    """Renders the main landing page."""
    return render_template(
        'index.html', 
        show_new_tournament_button=flags.show_new_tournament_button.is_enabled()
        )

@app.route('/my-tournaments')
def my_tournaments():
    """Route for viewing saved tournaments."""
    from models import Tournament
    tournaments = Tournament.query.order_by(Tournament.created_at.desc()).all()
    return render_template('my_tournaments.html', tournaments=tournaments)

if __name__ == '__main__':
    # Run the server on local port 8000
    app.run(host='0.0.0.0', port=8500, debug=True)