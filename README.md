# Flask Test API

Just a simple example of how to deploy a flask API

## Installation

- Create a virtual enviroment

- Activate the virtual environment

- Install the packages from the `requirements.txt` by running `pip install -r requirements.txt`

- Create a new `.env` file in the root of your directory, and then add in all the variables from the `.env.examples` with the appropriate values

- Finally, run the app with `gunicorn --workers=2 'app:create_app()'` or

  ```bash
  # Windows 
  py app.py

  # Unix (Mac | Linux)
  python3 app.py
  ```
