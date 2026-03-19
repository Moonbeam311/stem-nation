import random
import string

sessions = {}

def generate_session_code():
    return ''.join(random.choices(string.digits, k=4))


def create_session():

    code = generate_session_code()

    sessions[code] = {
        "students": [],
        "civilizations": {
            "River Alliance": None,
            "Forest Union": None,
            "Highland Confederacy": None,
            "Coastal League": None
        }
    }

    return code


def join_session(code, student_name, civilization):

    if code not in sessions:
        return False

    session = sessions[code]

    if session["civilizations"][civilization] is not None:
        return False

    session["students"].append(student_name)
    session["civilizations"][civilization] = student_name

    return True


def get_session(code):
    return sessions.get(code)

