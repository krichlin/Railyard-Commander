# ./lib/models.train.py

from models.__init__ import CURSOR, CONN

class Train:
    def __init__(self, name, type, id=None):
        self.id = id
        self.name = name
        self.type = type
    
    def __repr__(self):
        return f"<Train {self.id}: {self.name}, {self.type}"
    
    @classmethod
    def create_table(cls):
        """ Create new table for Trains """
        sql = """
            CREATE TABLE IF NOT EXISTS trains (
            id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table for Trains """
        sql = """
            DROP TABLE IF EXISTS trains;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with name and type of the current Train instance.  
            Then update the object id attribute using the primary key of the new row.
        """
        sql = """
            INSERT INTO trains (name, type)
            VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.type))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, type):
        """ Init new train instance and save the object to db """
        train = cls(name, type)
        train.save()
        return train

    def update(self):
        """ Update the table row corresponding to the current Train instance """
        sql = """
            UPDATE trains
            SET name = ?, type = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.type, self.id))
        CONN.commit();

    def delete(self):
        """ Delete the table row corresponding to the curreint Train instance """
        sql = """
            DELETE from trains
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
