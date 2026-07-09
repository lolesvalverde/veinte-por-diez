from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Player

player_bp = Blueprint('player', __name__)

@player_bp.route('/players')
def players():
    """Route for viewing all registered players."""
    all_players = Player.query.order_by(Player.id).all()
    return render_template('players.html', players=all_players)

@player_bp.route('/players/new', methods=['GET', 'POST'])
def new_player():
    """Route for creating a new player."""
    if request.method == 'POST':
        try:
            # Create new player from form data
            player = Player(
                first_name=request.form.get('first_name'),
                last_name=request.form.get('last_name') or None,
                position=request.form.get('position'),
                level=int(request.form.get('level')),
                group=request.form.get('group'),
                phone=request.form.get('phone'),
                notes=request.form.get('notes') or None
            )

            db.session.add(player)
            db.session.commit()

            flash('Jugador registrado exitosamente', 'success')
            return redirect(url_for('player.players'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar jugador: {str(e)}', 'error')
            return redirect(url_for('player.new_player'))

    return render_template('new_player.html')

@player_bp.route('/players/<int:player_id>/edit', methods=['GET', 'POST'])
def edit_player(player_id):
    """Route for editing an existing player."""
    player = Player.query.get_or_404(player_id)

    if request.method == 'POST':
        try:
            player.first_name = request.form.get('first_name')
            player.last_name = request.form.get('last_name') or None
            player.position = request.form.get('position')
            player.level = int(request.form.get('level'))
            player.group = request.form.get('group')
            player.phone = request.form.get('phone')
            player.notes = request.form.get('notes') or None

            db.session.commit()

            flash('Jugador actualizado exitosamente', 'success')
            return redirect(url_for('player.players'))

        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar jugador: {str(e)}', 'error')

    return render_template('edit_player.html', player=player)

@player_bp.route('/players/<int:player_id>/delete', methods=['POST'])
def delete_player(player_id):
    """Route for deleting a player."""
    try:
        player = Player.query.get_or_404(player_id)
        db.session.delete(player)
        db.session.commit()
        flash('Jugador eliminado exitosamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar jugador: {str(e)}', 'error')

    return redirect(url_for('player.players'))
