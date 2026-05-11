import os
import uuid
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, flash, current_app
from werkzeug.utils import secure_filename

tournament_bp = Blueprint('tournament', __name__)

@tournament_bp.route('/new', methods=['GET', 'POST'])
def new():
    """Route for creating a new tournament."""
    from models import db, Tournament

    if request.method == 'POST':
        # Get form data
        tournament_name = request.form.get('tournament_name')
        mode = request.form.get('mode')
        start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()

        # Handle file upload
        logo = request.files.get('logo')
        if logo and logo.filename:
            filename = secure_filename(logo.filename)
            # Add UUID prefix to avoid filename conflicts
            unique_filename = f"{uuid.uuid4().hex[:8]}_{filename}"
            logo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
            logo.save(logo_path)

            # Create new tournament
            tournament = Tournament(
                name=tournament_name,
                mode=mode,
                logo_filename=unique_filename,
                start_date=start_date,
                end_date=end_date
            )

            db.session.add(tournament)
            db.session.commit()

            flash(f'Torneo "{tournament_name}" creado exitosamente!', 'success')
            return redirect('/my-tournaments')
        else:
            flash('Por favor sube un logo', 'error')

    return render_template('new_tournament.html')
