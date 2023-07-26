from . import get_connection
from colorama import Fore, init, Style

def create_notes_table():
  db = get_connection()

  # TERMINATES THE FUNCTION IF THERE'S NO CONNECTION
  if not db: return

  connection, cursor = db

  sql = """CREATE TABLE IF NOT EXISTS notes (
      note_id INT PRIMARY KEY AUTO_INCREMENT,
      content VARCHAR(100) NOT NULL,
      is_completed TINYINT DEFAULT 0
  )"""

  cursor.execute(sql)
  connection.commit()

  print("(NOTES) TABLE CREATED!")
  connection.close()



def get_note_by_id(note_id):
  db = get_connection()
  if not db: return

  connection, cursor = db
  sql = "SELECT * FROM notes WHERE note_id = %s"
  cursor.execute(sql, [note_id])
  
  note = cursor.fetchone()
  connection.close()
  return note


def get_notes():
 pass
