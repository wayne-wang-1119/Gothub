import os
import dotenv


dotenv.load_dotenv()


TEST_HTTPS_URL = "https://github.com/Git-of-Thoughts/GoT-test.git"
OTHER_BRANCH = "modify-snake.py"
GITHUB_TOKEN = str(os.getenv("GITHUB_GOT_TEST_TOKEN"))
OPENAI_API_KEY = str(os.getenv("OPENAI_API_KEY"))
