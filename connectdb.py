import csv
import sqlite3

# open the connection to the database
conn = sqlite3.connect('trade.db')
cur = conn.cursor()

# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS detail1')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE detail1 (date TEXT PRIMARY KEY, Year TEXT, Direction TEXT, Weekday TEXT, Country TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('covidreportcsv/NEWCOVID.csv', newline='') as f:
    reader = csv.reader(f, delimiter=",")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        date = row[2]
        Direction = row[0]
        Year = row[1]
        Weekday = row[3]
        Country = row[4]

        cur.execute('INSERT OR IGNORE INTO detail1 VALUES (?,?,?,?,?)', (date, Year, Direction, Weekday, Country))
        conn.commit()




# drop the data from the table so that if we rerun the file, we don't repeat values
conn.execute('DROP TABLE IF EXISTS detail2')
print("table dropped successfully");
# create table again
conn.execute('CREATE TABLE detail2 (ids INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT, Transport TEXT, Measure TEXT, Value TEXT, Cumulative TEXT)')
print("table created successfully");

# open the file to read it into the database
with open('covidreportcsv/NEWCOVID.csv', newline='') as f:
    reader = csv.reader(f, delimiter=";")
    next(reader) # skip the header line
    for row in reader:
        print(row)

        date = row[2]
        Transport = row[6]
        Measure = row[7]
        Value = row[8]
        Cumulative = row[9]

        cur.execute('INSERT INTO detail2 VALUES (NULL,?,?,?,?,?)', (date, Transport, Measure, Value, Cumulative))
        conn.commit()


print("data parsed successfully");
conn.close()
        