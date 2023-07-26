# FLASK TASK

This task is designed to help you become familiar with our code structure, which, in turn, will enable us to work uniformly and more efficiently.

## Tasks

- Set up the project using the steps provided in the [README.md](README.md#installation)

- Try to create a new notes without sending any body. Notice you'll get a `500 INTERNAL SERVER ERROR`, if you check where the error was handled in [notes.py](app/routes/notes.py), `400 BAD REQUEST` was the status code that was returned in the `CustomRequestError` class. Fix this issue.

- Check out the error in the `get_all_notes` function, and try to fix it.

- Check out the comments below in the [notes.py](app/routes/notes.py) and implement those routes. Remember to check for the `id` params and `content` for those routes that requires them and return the appropriate response for them.
