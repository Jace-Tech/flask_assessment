from mysql.connector import connect
from dotenv import dotenv_values
from colorama import Fore, init, Style
import os

if os.name == 'nt': init()

ENV = dotenv_values()

def get_connection():
  try:
    connection = connect(
      host=ENV["MYSQL_HOST"],
      user=ENV["MYSQL_USER"],
      password=ENV["MYSQL_PASSWORD"],
      database=ENV["MYSQL_DB"],
      port=ENV["MYSQL_PORT"],
    )

    cursor = connection.cursor(buffered=True, dictionary=True)
    print(Fore.BLUE + "DATABASE INFO:" + Fore.RESET, Fore.GREEN + "Database connected!" + Fore.RESET)
    return connection, cursor
  except Exception as e:
    print(Fore.RED + "DATABASE ERROR:" + Fore.RESET, Fore.RED + str(e) + Fore.RESET)
    return None
    