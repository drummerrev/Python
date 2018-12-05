# Import from csv, os, sys modules

from csv import DictReader, writer, DictWriter
import os
import sys


# Dialpad_User class definition

class Dialpad_User:

    def __init__(self, type, name, email, phone, country, departments):
        self.type = type
        self.name = name
        self.email = email
        self.phone = phone
        self.country = country
        self.departments = departments
        self.fullname = list(self.name.split(" "))
        self.fname = self.fullname[0]
        self.lname = self.fullname[1]

## Method to create userName from email attribute
    def username(self):
        emailaslist = list(self.email.split("@"))
        return emailaslist[0]

# Check if email is an alias or a primary ID in GSuite
# Check if userName exists in Okta (or other service)


## Use DictReader to parse file and instantiate Dialpad_User instances:

def transformCSV(csvInPutFile, csvOutPutFile):
    ''' Function takes in CSV input, instantiates User objects, and writes out
    user object attributes to output CSV '''

    with open(csvInPutFile) as file:
        csv_reader = DictReader(file)

        with open(csvOutPutFile, "a") as file:
            headers = ["userName", "firstName", "lastName", "Email", "Phone"]
            csv_writer = DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()

            for row in csv_reader:
            # each row is an OrderedDict:
            # print(row)
                if row['type'] == "user":
                    userID = row['email']
                    userID = Dialpad_User(row['type'], row['name'], row['email'], row['phone_numbers'], row['country'], row['departments'])
                    print("Adding {}, with {} as their Email ID, and {} phone number to CSV...".format(userID.fname, userID.email, userID.phone))

                    csv_writer.writerow({
                        "userName": userID.username(),
                        "firstName": userID.fname,
                        "lastName": userID.lname,
                        "Email": userID.email,
                        "Phone": userID.phone
                        })

def main():

    transformCSV(csvInPutFile, csvOutPutFile)




if __name__ == '__main__':

    csvInPutFile = raw_input("Name of CSV you wish to transform:  ")

    ## File verification
    assert os.path.exists(csvInPutFile), "I did not find the file at, "+str(csvInPutFile)
    f = open(csvInPutFile,'r+')
    print("Hooray we found your file!")
    f.close()

    csvOutPutFile = raw_input("Name of CSV to export:  ")

    main()
