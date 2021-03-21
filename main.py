from markdowngenerator import MarkdownGenerator
import pyodbc


def generate_spec(cursor, doc, conn):
    cursor.execute("SELECT MAX(Number1) FROM Component")
    max_n1 = cursor.fetchone()[0]
    for i in range(1, max_n1 + 1):
        cursor.execute(
            "SELECT ID, Name, Description, Number FROM Component WHERE Number1 = {} AND Number2 IS NULL".format(i))
        row = cursor.fetchone()
        doc.addHeader(1, row.Name)
        doc.writeTextLine(row.Description)
        generate_requirements_for_component(cursor, doc, row.ID, conn, 2)
        cursor.execute(
            "SELECT MAX(Number2) FROM Component WHERE Number1 = {}".format(i))
        max_n2 = cursor.fetchone()[0]
        if max_n2 is None:
            max_n2 = 1
        for j in range(1, max_n2 + 1):
            cursor.execute(
                "SELECT ID, Name, Description, Number FROM Component WHERE Number1 = {} AND Number2 = {}".format(i, j))
            row = cursor.fetchone()
            if (row == None):
                break
            doc.addHeader(2, row.Name)
            doc.writeTextLine(row.Description)
            generate_requirements_for_component(cursor, doc, row.ID, conn, 3)


def generate_requirements_for_component_grr(component_cursor, doc, componentID, conn, header_level):
    req_cursor = conn.cursor()
    component_cursor.execute(
        "SELECT * FROM LinkSystemRequirementComponent WHERE ChildID = {}".format(componentID))
    for link_row in component_cursor.fetchall():
        req_cursor.execute(
            "SELECT * FROM SystemRequirement WHERE ID = {}".format(link_row.ParentID))
        req_row = req_cursor.fetchone()
        doc.addHeader(header_level, req_row.Number + " " + req_row.Name)
        table = [
            {"Description": req_row.Description, "Priority": req_row.cmbPriority,
                "Verification Status": req_row.cmbVerificationStatus}
        ]
        

def generate_requirements_for_component(cursor, doc, conn, component):
    cursor.execute("SELECT ParentID FROM LinkSystemRequirementComponent WHERE ChildID = {}".format(component))
    for entry in cursor.fetchall():
        req_num = entry[0]
        cursor.execute("SELECT * FROM SystemRequirement WHERE ID = {}".format(req_num))
        for thing in cursor.fetchall():
            doc.addHeader(2, thing.Number + " " + thing.Name)
            table = [
                {"Description": thing.Description.replace("\r", " ").replace("\n", " "), "Priority": thing.cmbPriority,
                    "Verification Status": thing.cmbVerificationStatus}
            ]
            doc.addTable(dictionary_list=table)


def generate_requirements_for_system_cat(cursor, doc, conn, cat):
    # doc.addHeader(1, "Whole Car Specification")
    # doc.writeTextLine("This document outlines all the requirements for Sunswift 7")
    # cursor.execute("SELECT MAX(Number1) FROM SystemRequirement")
    # max_n1 = cursor.fetchone()[0]
    cursor.execute(
        "SELECT * FROM SystemRequirement WHERE Number1 = {} AND Number2 IS NULL".format(cat))
    row = cursor.fetchone()
    doc.addHeader(1, row.Name)
    doc.writeTextLine(row.Description)
    cursor.execute(
        "SELECT * FROM SystemRequirement WHERE Number1 = {} AND Number2 IS NOT NULL".format(cat))
    for req_row in cursor.fetchall():
        doc.addHeader(2, req_row.Number + " " + req_row.Name)
        table = [
            {"Description": req_row.Description.replace("\r", " ").replace("\n", " "), "Priority": req_row.cmbPriority,
                "Verification Status": req_row.cmbVerificationStatus}
        ]
        doc.addTable(dictionary_list=table)

def generate_requirements(cursor, doc, conn):
    """
    This function generates the specification of the whole car based on the requirements themselves.

    Args:
        cursor (cursor): cursor for the database connection
        doc (document): the markdown document
        conn (conn): connection to the database itself
    """
    doc.addHeader(1, "Whole Car Specification")
    doc.writeTextLine("This document outlines all the requirements for Sunswift 7")
    cursor.execute("SELECT MAX(Number1) FROM SystemRequirement")
    max_n1 = cursor.fetchone()[0]
    for i in range(1, max_n1 + 1):
        cursor.execute(
            "SELECT * FROM SystemRequirement WHERE Number1 = {} AND Number2 IS NULL".format(i))
        row = cursor.fetchone()
        doc.addHeader(2, row.Name)
        doc.writeTextLine(row.Description)
        cursor.execute(
            "SELECT * FROM SystemRequirement WHERE Number1 = {} AND Number2 IS NOT NULL".format(i))
        for req_row in cursor.fetchall():
            doc.addHeader(3, req_row.Number + " " + req_row.Name)
            table = [
                {"Description": req_row.Description.replace("\r", " ").replace("\n", " "), "Priority": req_row.cmbPriority,
                    "Verification Status": req_row.cmbVerificationStatus}
            ]
            doc.addTable(dictionary_list=table)


if __name__ == "__main__":

    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Tanvee\Documents\_UNSW\sunswift\document-generator\database2.accdb;'
        conn = pyodbc.connect(con_string)
        cursor = conn.cursor()
        print("Connected To Database")

    except pyodbc.Error as e:
        print("Error in Connection", e)

    # Now that you're connecteed to the database, let's make a spec baased on a component
    # for rows in cursor.execute("SELECT "):
    cursor.execute("SELECT * FROM Component")
    for row in cursor.fetchall():
        print("docs\{} Specification.md".format(row.Name))
        with MarkdownGenerator(filename="_{} Specification.md".format(row.Name), enable_write=False) as doc:
            doc.addHeader(1, "Specification for {}".format(row.Name))
            generate_requirements_for_component(cursor, doc, conn, row[0])
    
    print("exited some how")
