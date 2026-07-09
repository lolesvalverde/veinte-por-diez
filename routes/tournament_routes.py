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

            flash(f'Torneo "{tournament_name}" creado!', 'success')
            return redirect(f'/tournaments/{tournament.id}/players')
        else:
            flash('Por favor sube un logo', 'error')

    return render_template('new_tournament.html')

@tournament_bp.route('/tournaments/<tournament_id>/players', methods=['GET', 'POST'])
def tournament_players(tournament_id):
    """Route for managing players in a tournament."""
    from models import db, Tournament, Player

    tournament = Tournament.query.get_or_404(tournament_id)

    if request.method == 'POST':
        # Get selected player IDs from form
        selected_player_ids = request.form.getlist('player_ids')

        # Clear existing players
        tournament.players = []

        # Add selected players
        for player_id in selected_player_ids:
            player = Player.query.get(player_id)
            if player:
                tournament.players.append(player)

        db.session.commit()

        flash(f'{len(selected_player_ids)} jugadores añadidos al torneo', 'success')
        return redirect('/my-tournaments')

    # Get all players grouped by group
    players_group_a = Player.query.filter_by(group='A').order_by(Player.first_name).all()
    players_group_b = Player.query.filter_by(group='B').order_by(Player.first_name).all()

    # Get currently selected player IDs
    selected_ids = [p.id for p in tournament.players]

    return render_template('tournament_players.html',
                         tournament=tournament,
                         players_group_a=players_group_a,
                         players_group_b=players_group_b,
                         selected_ids=selected_ids)

@tournament_bp.route('/tournaments/<tournament_id>/delete', methods=['POST'])
def delete_tournament(tournament_id):
    """Route for deleting a tournament."""
    from models import db, Tournament
    import os
    from flask import current_app

    try:
        tournament = Tournament.query.get_or_404(tournament_id)

        # Delete logo file
        logo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], tournament.logo_filename)
        if os.path.exists(logo_path):
            os.remove(logo_path)

        db.session.delete(tournament)
        db.session.commit()
        flash('Torneo eliminado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar torneo: {str(e)}', 'error')

    return redirect('/my-tournaments')

@tournament_bp.route('/tournaments/<tournament_id>')
def tournament_detail(tournament_id):
    """Route for viewing tournament details."""
    from models import Tournament

    tournament = Tournament.query.get_or_404(tournament_id)

    # Separate players by group
    players_group_a = [p for p in tournament.players if p.group == 'A']
    players_group_b = [p for p in tournament.players if p.group == 'B']

    return render_template('tournament_detail.html',
                         tournament=tournament,
                         players_group_a=players_group_a,
                         players_group_b=players_group_b)

@tournament_bp.route('/tournaments/<tournament_id>/edit', methods=['GET', 'POST'])
def edit_tournament(tournament_id):
    """Route for editing tournament details."""
    from models import db, Tournament
    import os
    from flask import current_app

    tournament = Tournament.query.get_or_404(tournament_id)

    if request.method == 'POST':
        try:
            tournament.name = request.form.get('tournament_name')
            tournament.mode = request.form.get('mode')
            tournament.start_date = datetime.strptime(request.form.get('start_date'), '%Y-%m-%d').date()
            tournament.end_date = datetime.strptime(request.form.get('end_date'), '%Y-%m-%d').date()

            # Handle logo update if new file is uploaded
            logo = request.files.get('logo')
            if logo and logo.filename:
                # Delete old logo
                old_logo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], tournament.logo_filename)
                if os.path.exists(old_logo_path):
                    os.remove(old_logo_path)

                # Save new logo
                filename = secure_filename(logo.filename)
                unique_filename = f"{uuid.uuid4().hex[:8]}_{filename}"
                logo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], unique_filename)
                logo.save(logo_path)
                tournament.logo_filename = unique_filename

            db.session.commit()
            flash('Torneo actualizado exitosamente', 'success')
            return redirect(f'/tournaments/{tournament_id}')

        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar torneo: {str(e)}', 'error')

    return render_template('edit_tournament.html', tournament=tournament)
