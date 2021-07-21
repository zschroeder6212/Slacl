from flask_login import current_user


def get_user_details():
    if current_user.is_authenticated:
        return current_user.get_user_info()
    else:
        generic_user = {
            'email': '',
            'id': '',
            'name': '',
            'picture': ''
        }
        return generic_user
