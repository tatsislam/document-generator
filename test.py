from markdowngenerator import MarkdownGenerator
import pyodbc


if __name__ == "__main__":

    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tanvee\Documents\_UNSW\sunswift\document-generator\database2.accdb;'
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()
        print("Connected To Database")
 
    except pyodbc.Error as e:
        print("Error in Connection", e)

    cursor.execute("SELECT ParentID FROM LinkSystemRequirementComponent WHERE ChildID = 771")
    for entry in cursor.fetchall():
        req_num = entry[0]
        cursor.execute("SELECT * FROM SystemRequirement WHERE ID = {}".format(req_num))
        thing = cursor.fetchone()
        print(thing)

    # cursor.execute("SELECT * FROM LinkSystemRequirementComponent")

    # for row in cursor.fetchall():
    #     print(row)
    # for col in cursor.columns("Component"):
    #     print(col[3])