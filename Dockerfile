FROM postgresql:11

RUN pip install psycopg2-binary
RUN python db_setup.py

