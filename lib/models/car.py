# ./lib/models.car.py

from models.__init__ import CURSOR, CONN
from models.train import Train

class Car:
    
    # dictionary of all objects saved to db

    all = {}

    def __init__(self, name, description, train_id, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.train_id = train_id
        

    def __repr__(self):
        return (
            f"<Car {self.id}: {self.name}, " +
            f"Description: {self.description}, >"
        )
    
    @property 
    def name(self):
        return self._name  

    @name.setter
    def name(self, name):
        if isinstance(name,str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )
        
    @property
    def description(self):
        return self._description 

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string" )

    @property
    def train_id(self):
        return self._train_id

    @train_id.setter
    def train_id(self, train_id):
        if type(train_id) is int and Train.find_by_id(train_id):
            self._train_id = train_id
        else:
            raise ValueError("Train ID must reference a train in the database")
    
    @classmethod
    def create_table(cls):
        """ Create a new table for attributes of car instances """
        sql = """
                CREATE TABLE IF NOT EXISTS cars (
                id INTEGER PRIMARY KEY,
                name TEXT,
                description TEXT,
                train_id INTEGER,
                FOREIGN KEY (train_id) REFERENCES trains(id))
            """
        CURSOR.execute(sql)
        CONN.commit()
        

    @classmethod
    def drop_table(cls):
        """ drop table that persists cars instances """
        sql = """
            DROP TABLE IF EXISTS cars;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with name, description, and weight of current car
            update object ID attribute using primary key value of new row
            save the object in local dictionary using table row's PK as dictionary key """
        sql = """
            INSERT INTO cars (name, description, train_id)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.description, self.train_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        """ Update the table row corresponding to current Car """
        sql = """
            UPDATE cars
            SET name = ?, description = ?, train_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description,
                            self.train_id, self.id))
        CONN.commit()
    
    def delete(self):
        """ 
            Delete the table row corresponding to current car instance
            then delete dictionary entry, and reassign id attribute
        """
        sql = """
            DELETE FROM cars
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # delete dictionary entry using id as key
        del type(self).all[self.id]

        # set the id to None
        self.id = None

    @classmethod
    def create(cls, name, description, train_id):
        """ Initialize a new car object and save the object to db """
        car = cls(name, description, train_id)
        car.save()
        return car

    @classmethod
    def instance_from_db(cls,row):
        """ return a car object having the attribute values from the table row """

        # check dictionary for existing instance using row's primary key
        car = cls.all.get(row[0])
        if car:
            # ensure attributes match row values in case local instance was modified
            car.name = row[1]
            car.description = row[2]
            car.train_id = row[3]
        else:
            # not in dictionary, so create instance and add to dictionary
            car = cls(row[1], row[2], row[3])
            car.id = row[0]
            cls.all[car.id] = car
        return car
    
    @classmethod
    def get_all(cls):
        """ Return a list containing 1 car object per table row """
        sql = """
            SELECT *
            FROM cars
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ Return car object corresponding to the table row matching specified primary key """
        sql = """
            SELECT * 
            FROM cars
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """ Return employee object corresponding to fist table row matching specified PK """
        sql = """
            SELECT *
            FROM cars
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None