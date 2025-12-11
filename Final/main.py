'''Sorts a database based on certain categories after putting the database into a hash'''
'''author Amanullah Anis'''
'''version 1.0 '''
'''since 1.0 '''

''' 
* OS: Windows
* IDE: Visual Studio
* Copyright : This is my own original work 
* based on specifications issued by our instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified, nor used generative AI as a final draft. 
* I have not given other fellow student(s) access to my program.
'''
from tkinter import *
import tkinter 
import pandas as pd
import tkinter.messagebox
# Table for the sorting method
class Sorter:
    # This is the insetion sort that sorts the items in descending order.
    def insertion_sort(num):
        n = len(num) 
        if n <= 1:
            return 
        for i in range(1, n):  
            key = num[i] 
            j = i-1
            while j >= 0 and key > num[j]:  
                num[j+1] = num[j] 
                j -= 1
            num[j+1] = key  

# Table for the has data strucutre being used
class Hash:
    #This sets a regular hashtable ht that is used for the hash table. The dictionary underneath is used to hold elements and keys while the sort is being ran. Variables is so that I can get the hash table into a string and return it. 
    def __init__(self):
        self.ht = {}
        self.sortedht = {}
        self.variables = f''
    #Gets values or a value from the hash table based off of the key
    def get(self, key):
        if self.contains(key):
            return self.ht[key]
        else: return None
    #If a key is put into the parameter and is in the hash table in then true is returned other wise a false is returned
    def contains(self, key):
        if key in self.ht:
            return True
        else: return False
    #Inserts a new element into the hash table if they key is new to the table
    def insert(self, key, value):
        if self.contains(key) == True:
            return None
        self.ht[key] = value
    #Pops or removes the key that was put in if key is in table. Does not retrun the popped key/value
    def remove(self, key):
        if self.contains(key):
            self.ht.pop(key)
        else: return None
    #Returns the suze of the hash table
    def get_length(self):
        return len(self.ht)
    #Puts the hash table into a string so I can output easier into tkinter
    def print(self):
        if self.get_length() > 0:
            self.variables = f''
            for item in self.ht:
                self.variables = self.variables + f'{item}- {self.ht[item]}\n\n'
        else: return None
    #Used for using insertion sort method to sort hash table in descending order by charitable commitment
    def sort(self):
        #Gets the unsorted values and puts them into a list
        sorting = list(self.ht.values())
        #Used for getting all the unsorted charitable commitment values from the values
        sorting2 = []
        #Goes through every key and appends the chartiable commitment
        for items in sorting:
            sorting2.append(items[4][1])
        #Insertion sort is called form class Sorter to sort the charitable commitments in descending order
        Sorter.insertion_sort(sorting2)
        #A list of the keys of the unsorted hash table is made 
        keys = list(self.ht.keys())
        #Used for iterating through the sorted list of charitable commitments
        index = 0
        #A while loop that breaks when the sorted hash table is the same size as the unsorted hash table 
        while len(self.sortedht) < len(self.ht):
            #Goes through the list keys and uses each key as k to bring the values from the unsorted hash and puts them into v
            for k in keys:
                v = self.ht[k]
                #If the current element that is being iterated in the sorted list is equal to the key list element's value of charitable commitment and this same key list element is not in the new sorted hash table then the new sorted hash table is given a new key and value and then the for loop breaks and adds one to the index used for iterating the sorted charitable commitment and the while loop condition is checked.
                if sorting2[index] == v[4][1] and k not in self.sortedht:
                    self.sortedht[k] = v
                    break
            index += 1
        #Empties the current unsorted hash table
        for items in range(0, len(self.ht)):
            self.remove(keys[items])
        #Inserts the new sorted hash table items into the hash table object.
        for k,v in self.sortedht.items():
            self.insert(k,v)

       
class Preferance:
    #Variable initializers for gui and functions in gui
    def __init__(self, ui):
        #Rreads the table 
        self.orginiz = pd.read_csv("charities.csv")
        #Object for the gui
        self.m = ui
        #Makes an object for the hash table
        self.ht = Hash()
        #Gui button and text boxs made
        self.n_category = tkinter.Button(self.m, text="Domestic Needs", command=lambda: self.set_cartegory("Domestic Needs"))
        self.n_category.grid(row=4)
        self.n_category1 = tkinter.Button(self.m, text="International Needs", command=lambda: self.set_cartegory("International Needs"))
        self.n_category1.grid(row=5)
        self.n_category2 = tkinter.Button(self.m, text="Medical", command=lambda: self.set_cartegory("Medical"))
        self.n_category2.grid(row=6)
        self.n_category3 = tkinter.Button(self.m, text="Youth", command=lambda: self.set_cartegory("Youth"))
        self.n_category3.grid(row=7)
        self.n_category4 = tkinter.Button(self.m, text="Environment & Animals", command=lambda: self.set_cartegory("Environment & Animals"))
        self.n_category4.grid(row=8)
        self.n_category5 = tkinter.Button(self.m, text="Health", command=lambda: self.set_cartegory("Health"))
        self.n_category5.grid(row=9)
        self.n_category6 = tkinter.Button(self.m, text="Religious", command=lambda: self.set_cartegory("Religious"))
        self.n_category6.grid(row=10)
        self.n_category7 = tkinter.Button(self.m, text="Public Affairs", command=lambda: self.set_cartegory("Public Affairs"))
        self.n_category7.grid(row=11)
        self.n_category8 = tkinter.Button(self.m, text="Education", command=lambda: self.set_cartegory("Education"))
        self.n_category8.grid(row=12)
        self.n_category9 = tkinter.Button(self.m, text="Cultural", command=lambda: self.set_cartegory("Cultural"))
        self.n_category9.grid(row=13)
        self.output = tkinter.Text(self.m)
        self.output.grid(row=3)       
        self.search_entry = tkinter.Text(self.m, width=50, height=1)
        self.search_entry.grid(row=1)
        self.search_label = tkinter.Label(self.m, text="Search Bar")
        self.search_label.grid(row=2)
        self.search_button = tkinter.Button(self.m, text="Search", command=self.selection)
        self.search_button.grid(row=1, column=2)
    #Prints the string of the hash table 
    def printer(self):
        self.output.config(state=tkinter.NORMAL)
        self.output.delete("1.0", "end")
        self.output.insert("1.0", self.ht.variables)
        self.output.config(state=tkinter.DISABLED)
    #Sets category with the clicked button and calls another funtion
    def set_cartegory(self, word):
        self.category = word
        self.find_organization()
    #Called after button is cliked and category is selected and used to output hash table
    def find_organization(self):
        #Empties the hash table so output is more specific to what is clicked
        self.ht.ht = {}
        #Empties the sorted hash table so output is more specific to what is clicked
        self.ht.sortedht = {}
        #Groups the table by categories and then returns the category that was selected
        self.selected = self.orginiz.groupby("category").get_group(self.category)
        #Gets the names of the orginizations which is also the keys to the hash table
        names = self.selected["name"].tolist()
        #Retrieves the values of the table and removes the rank and name
        charity = self.selected.drop(self.selected.iloc[:,0:2], axis=1)
        #used to hold the values that will be inserted into the hash table
        processing = []
        #Variable used for iteration throughout the different values
        num = 0
        #While loop that breaks when processing is same size to charity or the values
        while len(processing) < len(charity):
            #Dictionary used for adding values to a list cand there column names to a list
            row = {}
            #Used for changing datatypes into integer so that I can use them in sorting. k is the column names and v is the values at the current index of num at the selected category.
            for k,v in zip(charity.columns.tolist(), charity.loc[charity.index[num]].tolist()):
                #When specific columns are found there values are casted into an integer.
                if k == "fundraising efficiency %" or k == "charitable commitment %":
                    v = int(v)
                #Adds column name and their value into the dictionary
                row[k] = v
            #Appends a list version of the row dictionary which turns into a list of tuples with the first item in the tuple being the name of the column and the second item in the tuple being the value for that column. Once all items or names of the different items in the categories are appended the while loop breaks. 
            processing.append(list(row.items()))
            #The current category item is changed to the next item for updating and appending into processing
            num += 1
        #Inserts the names of the orginzations in the selected category as the keys for the hash table and puts in the corresponsing values that are tuples form processing
        for item in range(0, len(names)):
            self.ht.insert(names[item], processing[item])
        #Calls the sort function
        self.ht.sort()
        #Makes the variable string to that I Can print easier
        self.ht.print()
        #Calls the printer function to output selected categories in descending charitable commitment 
        self.printer()
    #Used for the search bar
    def selection(self):
        #Gets the names of the orginizations in the table and puts it in a list
        names = self.orginiz['name'].to_list()
        #Used for outputting search 
        relevant = pd.read_csv("charities.csv", index_col='name')
        #Returns what was searched
        name = self.search_entry.get("1.0", "end-1c")
        #Iterates through the names from the table
        for items in names:
            #If the searched up name is in the table then the information is outputted in a pandas format and the function is done
            if name == items:
                self.output.config(state=tkinter.NORMAL)
                self.output.delete("1.0", "end")
                self.output.insert("1.0", relevant.loc[items])
                self.output.config(state=tkinter.DISABLED)
                return
        #If not than a message is popped up
        tkinter.messagebox.showinfo(message="Not an orginaztion in the database")
        
if __name__ == "__main__":
    tester = tkinter.Tk()
    testing = Preferance(tester)
    tester.mainloop()
