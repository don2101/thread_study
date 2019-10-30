import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")

def daemon():
    logging.debug("start")
    time.sleep(5)
    logging.debug("Exit")


def main():
    t = threading.Thread(name="daemon", target=daemon)
    t.setDaemon(True)

    t.start()
    t.join()


if __name__ == "__main__":
    main()