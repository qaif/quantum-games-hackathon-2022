from PyQt6.QtCore import QRect


def shrink(rect, amount):
    return QRect(rect.x(), rect.y(), rect.width() - amount, rect.height() - amount)