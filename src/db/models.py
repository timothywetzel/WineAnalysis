from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float
import psycopg2

Base = declarative_base()

class Wine(base):
    __table_name__ = 'wine'
    index = Column(Integer, primary_key = True)
    fixed_acidity = Column(Float)
    volatile_acidity = Column(Float)
    citric_acid = Column(Float)
    residual_sugar = Column(Float)
    chlorides = Column(Float)
    free_sulfur_dioxide = Column(Float)
    total_sulfur_dioxide = Column(Float)
    density = Column(Float)
    pH = Column(Float)
    sulphates = Column(Float)
    alcohol = Column(Float)
    quality = Column(Integer)
    
    def __repr__(self):
        return "<Wine(Fixed Acidity='{}', \
        Volatile Acidity='{}', \
        Citric Acid='{}', \
        Residual Sugar='{}', \
        Chlorides='{}', \
        Free Sulfur Dioxide='{}', \
        Total Sulfur Dioxide='{}', \
        Density='{}', \
        pH='{}', \
        Sulphates='{}', \
        Alcohol='{}', \
        Quality='{}')>".format(self.fixed_acidity,
                        self.volatile_acidity,
                        self.citric_acid,
                        self.residual_sugar,
                        self.chlorides,
                        self.free_sulfur_dioxide,
                        self.total_sulfur_dioxide,
                        self.density,
                        self.pH,
                        self.sulphates,
                        self.alcohol,
                        self.quality)
    