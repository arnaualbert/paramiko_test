import mysql.connector
import os

# connection to the database
mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

# get all files in the current directory
def search_files(root_dir):
    file_list = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def upload_all_to_db(table,file_list):
# upload the files to the database
    for tfile in file_list:
        with open(tfile,"rb") as file:
            data = file.read()
        name_file = tfile.split('/')[-1]
        query = f"INSERT INTO {table} (test,name_file) VALUES (%s,%s)"
        values = (data,name_file)
        mycursor = mydb.cursor()
        mycursor.execute(query, values)
        mydb.commit()

def write_file(data, filename):
    with open(filename, 'wb+') as f:
        f.write(data)

def get_data_from_db(table):
    query = f"SELECT * FROM {table}"
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for file in myresult:
        write_file(file[1], f"{file[0]}")


if __name__ == "__main__":
    file_list = search_files(os.getcwd())
    print(file_list)
    print(len(file_list))
    upload_all_to_db("uploadblob",file_list) # upload the files in the db
    get_data_from_db("uploadblob") # get all the files in the db