import subprocess
import sys


def install(package):

    subprocess.call([sys.executable, "-m", "pip", "install", package])


if __name__ == '__main__':

    install('pyttsx3')
    install('pypiwin32')
    install("pymongo")
    install("speechrecognition")
