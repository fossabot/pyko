## Mysql Manager -> MM
# Author: Mrx04programmer
# Github : https://github.com/mrx04programmer
import mysql.connector
from dev.colors import *

class mmdb:
    def __init__(self):
        # Default Host Server 
        self.host = 'localhost'  
        # Default User Server 
        self.user = 'root'
        # Default Password Server 
        self.password = ''
    def connectdb(self, namedatabase):
        DB = mysql.connector.connect(
            database = namedatabase,
            host = self.host,
            user = self.user,
            passwd = self.password,
        )
    def execute(self, instructions):
        cursor = DB.cursor()
        instructions = self.instructions
        print(f"{O}[SQL] {W}Executing the next sentences:\n{G}{instructions}")
        if instructions == '':
            print(f"{R} [ERROR] {W} Intructions are empty")
        else:
            cursor.execute(instructions)