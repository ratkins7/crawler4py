

import pymysql

class Database:

    connection = None
    results = None

    def connect(self):
        self.connection = pymysql.connect(host='127.0.0.1',
             user='root', password='root',
             db='CS_121', charset='utf8mb4',
             cursorclass=pymysql.cursors.DictCursor)


    def insert(self, url, html, plain_text):
        """
        insert - inserts data to database
        :return:
        """

        try:
            self.connect()

            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `pages` (`url`, `html`, `plain_text`) VALUES (%s, %s, %s)"
                cursor.execute(sql, (url, html, plain_text))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                self.connection.commit()

                cursor.close()
                self.connection.close()
        except:
            print("uh oh ")

    def update(self, number):
        # update code here but dont need it
        pass



