import sys
import time

if sys.platform == 'win32':
    import msvcrt
else:
    import tty
    import termios

def get_key():
    if sys.platform == 'win32':
        if msvcrt.kbhit():  # Проверяем, была ли нажата клавиша
            return msvcrt.getch().decode()
        return None
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            input_char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return input_char