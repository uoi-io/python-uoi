# coding: utf-8
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# Following from Python cookbook, #475186
def use_color(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        # Auto color only on TTYs
        return False
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # Guess false in case of error
        return False

def printc(text, color=WHITE):
    if use_color:
        seq = "\x1b[1;%dm" % (30+color) + text + "\x1b[0m\n"
        sys.stdout.write(seq)
    else:
        sys.stdout.write(text)
