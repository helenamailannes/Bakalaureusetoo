
from constants import SWIPE_DISTANCE, ADMIN_PASSWORD


def swipe_ok(start, end):
    return abs(end - start) >= SWIPE_DISTANCE


def password_ok(text):
    return text == ADMIN_PASSWORD