#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymongo
# Communication with mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
#creating database
db = client["EmployeeData"]


# In[2]:


def main():
    while(1):
    #  option given to user to do CRUD operations
        selection =int(input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete, 5 to complete\n'))
    
        if selection == 1:
            insert()
        elif selection == 2:
            update()
        elif selection == 3:
            read()
        elif selection == 4:
            delete()
        elif selection ==5:
            print('\n task completed\n')
        else:
            print ('\n INVALID SELECTION \n')


# In[3]:


# Function to insert data into mongo db
def insert():
    try:
        employeeId = int(input('Enter Employee id :'))
        employeeName = str(input('Enter Name :'))
        employeeAge = int(input('Enter age :'))
        employeeCountry =str(input('Enter Country :'))
        
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name":employeeName,
                "age":employeeAge,
                "country":employeeCountry
        })
        print ('\nInserted data successfully\n')
    
    except:
        print("invalid input")


# In[4]:


# function to read records from mongo db
def read():
    try:
        empCol = db.Employees.find()
        print ('\n All data from EmployeeData Database \n')
        for emp in empCol:
            print (emp)

    except:
        print("Data does not exist")


# In[5]:


# Function to update record to mongo db
def update():
    try:
        criteria = int(input('\nEnter id to update\n'))
        name = str(input('\nEnter name to update\n'))
        age = int(input('\nEnter age to update\n'))
        country =str(input('\nEnter country to update\n'))

        db.Employees.update_one(
          
            {"id": criteria},
            {
                "$set": {
                    "name":name,
                    "age":age,
                    "country":country
                }
            }
        )
        print ("\nRecords updated successfully\n")    
    
    except:
        print("update unsuccessful")


# In[6]:


# Function to delete record from mongo db
def delete():
    try:
        criteria =int(input('\nEnter employee id to delete\n'))
        db.Employees.delete_many({"id":criteria})
        print ('\nDeletion successful\n') 
    except :
        print("Delete unsuccessful")


# In[ ]:


main()


# 

# In[ ]:





# 

# In[ ]:





# In[ ]:




