import sqlite3


class HighScoreDatabase:
    def __init__(self, db_name="highscores.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        create_table_command = """
        CREATE TABLE IF NOT EXISTS highscores (
            id INTEGER PRIMARY KEY,
            username TEXT,
            score INTEGER
        );
        """
        self.cursor.execute(create_table_command)
        self.connection.commit()

    def add_score(self, username, score):
        insert_data_command = """
        INSERT INTO highscores (username, score) VALUES (?, ?);
        """
        self.cursor.execute(insert_data_command, (username, score))
        self.connection.commit()

    def get_highscores(self):
        select_data_command = """
        SELECT username, score FROM highscores ORDER BY score ASC;  -- Order by score in ascending order
        """
        self.cursor.execute(select_data_command)
        highscores = self.cursor.fetchall()
        return highscores

    def close(self):
        self.connection.close()

    def username_exists(self, username):
        highscores = self.get_highscores()  # Fetch usernames from the database
        return any(entry[0] == username for entry in highscores)

