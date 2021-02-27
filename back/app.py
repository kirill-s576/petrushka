from src.router import app
from src.database.models import create_all_tables


if __name__ == "__main__":
    app.run(debug=False, port=7777)
