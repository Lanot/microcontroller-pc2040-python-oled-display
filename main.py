import time
from modules.config import Config
from modules.display import Display

if __name__ == '__main__':
    try:
        config = Config('config.json')
        display = Display(config)

        for i in range(8):
            display.line("Some Text Here." + str(i), i)
            time.sleep_ms(500)

        display.clear()
        display.line("     FINISH", 3)
        display.line("     THE END", 4)

    except Exception as e:
        print("An Exception Happened:\n{}".format(e))
        #sys.stdout.write("An Exception Happened:\n{}".format(e))
