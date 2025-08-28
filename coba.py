import time
import sys
import shutil

MESSAGE = "LUNA CAAAAAKKKKKKEPPPPP BANGGEEEEETTTTTTTTTT,TAPI BOOOHHHHOOOOOONNNGG"
FRAME_DELAY = 0.08      # kecepatan geser (lebih kecil = lebih cepat)
PAUSE_BETWEEN_LOOPS = 8 # jeda 8 detik setelah satu putaran penuh

def main():
    width = shutil.get_terminal_size((80, 20)).columns
    gap = " " * width
    base = MESSAGE + gap
    scroll = base * 2  # gandakan biar slicing aman untuk wrap
    total_shift = len(base)

    while True:
        for i in range(total_shift):
            window = scroll[i:i+width]
            sys.stdout.write("\r" + window)
            sys.stdout.flush()
            time.sleep(FRAME_DELAY)
        time.sleep(PAUSE_BETWEEN_LOOPS)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\n")