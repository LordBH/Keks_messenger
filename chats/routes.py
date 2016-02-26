from flask import session, render_template
from . import from_chats
from .tools import cmp_user as compare


main = from_chats


@main.route('/im/<id_user>', methods=['GET', 'POST'])
def chat(id_user=None):

    user1 = session.get('user_id')
    try:
        user2 = int(id_user)
    except ValueError:
        user2 = None

    extra = compare(user1, user2)

    room_id = '%d|%d' % extra

    session['name'] = session.get('user_username')
    session['room'] = room_id

    return render_template('im.html', room=session.get('room'))


@main.route('/im', methods=['GET', 'POST'])
def index():

    session['name'] = session.get('user_username')

    return render_template('im.html', room=session.get('room'))