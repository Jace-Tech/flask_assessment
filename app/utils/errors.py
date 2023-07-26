from functools import wraps
from .helpers import response

class CustomRequestError(Exception):
  """
    Request error class
  """
  def __init__(self, message, code = 400):
    super().__init__(message)
    self.message = message
    self.code = code


def catch_exception(fn):
  """
    Catches any exceptions that occurs in the provided route function
  """
  @wraps(fn) 
  def wrapper(*args, **kwargs):
    try:
      return fn(*args, **kwargs)
    
    except CustomRequestError as e:
      return response(e.message, None, False), 500
  
    except Exception as e:
      return response(str(e), None, False), 500
  return wrapper