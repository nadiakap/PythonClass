import sqlite3

# name of the sqlite database file
db_file = 'my_db1.sqlite'
table1 = 'students'  # name of the table to be created
table2 = 'courses'  # name of the table to be created
new_field1 = 'course_id' # name of the column
new_field2 = 'course_title' # name of the column
field_type = 'INTEGER'  # column data type
field2_type = 'STRING'

# Connecting to the database file
conn = sqlite3.connect(db_file)
c = conn.cursor()

c.execute('DROP TABLE {tn} '.format(tn=table1))
c.execute('DROP TABLE {tn} '.format(tn=table2))

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table1, nf=new_field1, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table2, nf=new_field1, ft=field_type))

c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table2, cn=new_field2, ct=field2_type))
try:
    c.execute("INSERT INTO {tn} ({idf}, {title}) VALUES (123458, 'course1') ".format(tn=table2, idf=new_field1, title = new_field2 ))
    c.execute("INSERT INTO {tn} ({idf},  {title}) VALUES (123459, 'course1')".format(tn=table2, idf=new_field1, title = new_field2))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(new_field1))
# Committing changes and closing the connection to the database file

c.execute("SELECT * FROM courses") 
'''
res1 = c.fetchone() 
print(res1)   
print("fetchall:")
'''
result = c.fetchall() 
for r in result:
    print(r)
   
conn.commit()
conn.close()
