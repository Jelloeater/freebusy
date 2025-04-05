import dotenv

import main as app_main

dotenv.load_dotenv()


class TestMain:
    @classmethod
    def test_hi(cls):
        app_main.start_server()
