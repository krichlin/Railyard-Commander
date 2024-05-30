# ./lib/models.train.py

from models.__init__ import CURSOR, CONN

class Train:

    # dictionary of objects saved to db
    all = {}

    def __init__(self, name, type, id=None):
        self.id = id
        self.name = name
        self.type = type
    
    def __repr__(self):
        return f"<Train {self.id}: {self.name}, {self.type}"
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name (self, name):
        if isinstance(name,str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, type):
        if isinstance(type, str) and len(type):
            self._type = type
        else:
            raise ValueError("Type must be a non-empty string")
    
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
        # Save the object in local dictionary using table row's PK as dictionary key
        type(self).all[self.id] = self 

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
    
        # also delete the dictionary entry using the id as the key
        del type(self).all[self.id]
        # set the id to None
        self.id = None

    @classmethod 
    def instance_from_db(cls,row):
        """ Return a train object having attribute values from the table row """

        # check dictionary for existing instance using rows primary key
        train = cls.all.get(row[0])
        if train:
            # check attributes match row values in case local object was modified
            train.name = row[1]
            train.type = row[2]
        else:
            # it's not in the dictionary, create a new instance and add to dictionary
            train = cls(row[1], row[2])
            train.id = row[0]
            cls.all[train.id] = train
        return train
    
    @classmethod
    def get_all(cls):
        """ return a list containing a Train object for each row in trains table """
        sql = """
            SELECT *
            FROM trains
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return a Train object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM trains
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """ Return a train object corresponding to the first table row matching specified name """
        sql = """
            SELECT *
            FROM trains
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def cars(self):
        """ returns a list of cars asasociated with current train """
        from car import Car
        sql = """
            SELECT * from cars
            WHERE train_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        return [Car.instance_from_db(row) for row in rows]