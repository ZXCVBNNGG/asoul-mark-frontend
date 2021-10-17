import regex
from sanic import Request


def is_uuid(uuid):
    if not regex.match("[0-9a-fA-F]{32}", uuid):
        return False
    return True


def is_uid(uid):
    try:
        int(uid)
    except ValueError:
        return False
    if len(str(uid)) > 11:
        return False
    return True


def userUUID_get(request: Request):
    UserUUID_H = request.headers.get("UserUUID")
    UserUUID_C = request.cookies.get("UserUUID")
    if not (UserUUID_H or UserUUID_C):
        return None
    if UserUUID_C and UserUUID_H:
        return UserUUID_H
    else:
        if UserUUID_C:
            return UserUUID_C
        else:
            return UserUUID_H
