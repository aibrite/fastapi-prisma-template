from core.app import App

from dotenv import load_dotenv
load_dotenv()


def run_application():
    return App.start()
   
if __name__ == "__main__":
    run_application()