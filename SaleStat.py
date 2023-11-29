class SaleStat:
    def __init__(self, con):
        while True:
            try:
                con = con  # Assign the database connection to a local variable
                cursor = con.cursor()

                # Execute a SQL query to select all records from the 'Sale' table
                cursor.execute("SELECT * FROM Sale;")
                row = cursor.fetchall()  # Fetch all the results

                # Print a table header
                print()
                print('+', end='')
                for i in range(0, 17 + 13 + 17 + 17 + 13 + 18):
                    print('-', end='')
                print('+')
                a = "{:<17} {:<13} {:<17} {:<17} {:<13} {:<13} {:<2}".format("| Invoice Number", "| Agent ID",
                                                                             "| Customer Name", "| Customer mob",
                                                                             "| Netpay", "| Gst", "|")
                print(a)
                print('+', end='')
                for i in range(0, 17 + 13 + 17 + 17 + 13 + 18):
                    print('-', end='')
                print('+')

                # Iterate through the retrieved rows and format and print them
                for r in row:
                    b = "{:<17} {:<13} {:<17} {:<17} {:<13} {:<13} {:<2}".format('| ' + r[0], '| ' + r[5], '| ' + r[1],
                                                                                 '| ' + r[2], '| ' + str(r[3]),
                                                                                 '| ' + str(r[4]), '|')
                    print(b)

                # Print a closing line for the table
                print('+', end='')
                for i in range(0, 17 + 13 + 17 + 17 + 13 + 18):
                    print('-', end='')
                print('+')

                con.commit()  # Commit any changes made to the database

                break  # Exit the loop
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue