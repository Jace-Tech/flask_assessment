from flask import Blueprint, request

from ..utils.helpers import response
from ..utils.errors import catch_exception, CustomRequestError

from ..database import get_connection
from ..database.notes_table import get_note_by_id


notes = Blueprint("notes", __name__)

# HTTP STATUS CODES
# Use this to know the appropriate codes to send back in each request

# 200 -> OK
# 201 -> CREATED | POSTED
# 301 -> REDIRECTING
# 400 -> BAD REQUEST
# 401 -> UNAUTHORIZED
# 403 -> FORBIDDEN
# 500 -> INTERNAL SERVER ERROR


# GET: [/] -> RETURNS ALL NOTES
@notes.get("/")
@catch_exception
def get_all_notes():
  all_notes = get_notes()
  return response("All notes", all_notes)



# POST: [/] | [/create] -> CREATE A NOTE
@notes.post("/")
@notes.post("/create")
@catch_exception
def create_notes():
  db = get_connection()

  # CHECK FOR DATABASE CONNECTION
  if not db: raise CustomRequestError("Failed to connect to database", 500)
  connection, cursor = db

  # CHECK IF CONTENT WAS SENT 
  data = request.json
  if not data.get('content'): raise CustomRequestError("Content is required", 400)

  sql = "INSERT INTO notes (content) VALUES (%s)"
  cursor.execute(sql, [data.get('content')])
  connection.commit()

  # CHECK IF NOTE WAS CREATED
  if not cursor.rowcount: raise CustomRequestError("Failed to create note", 500)

  # RETURN NOTE DETAILS
  note = get_note_by_id(cursor.lastrowid)

  return response("Note created", note), 201




# GET: [/:id] -> RETURN NOTE WITH GIVEN ID


# DELETE: [/:id] -> DELETE NOTE WITH GIVEN ID


# PATCH | PUT: [/:id] -> UPDATE NOTE WITH GIVEN ID