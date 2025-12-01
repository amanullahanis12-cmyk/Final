import unittest
from tkinter import *
import tkinter 
import pandas as pd
import tkinter.messagebox
class Sorter:
    def insertion_sort(num):
        n = len(num) 
     
        if n <= 1:
            return 

        for i in range(1, n):  
            key = num[i] 
            j = i-1
            while j >= 0 and key < num[j]:  
                num[j+1] = num[j] 
                j -= 1
            num[j+1] = key  
class Hash():
    def __init__(self):
        self.ht = {}
        self.copycat = {}
        self.sortedht = {}
        self.variables = f''
    def get(self, key):
        return self.ht[key]
    def contains(self, key):
        if key in self.ht:
            return True
        else: return False
    def insert(self, key, value):
        if self.contains(key) == True:
            return
        self.ht[key] = value
    def remove(self, key):
        self.ht.pop(key)
    def get_length(self):
        return len(self.ht)
    def print(self):
        self.variables = f''
        for item in self.ht:
            self.variables = self.variables + f'{item}- {self.ht[item]}\n\n'
    def sort(self):
        sorting = []
        sorting2 = []
        sorting.append(list(self.ht.values()))
        for item in sorting:
            for items in item:
                sorting2.append(items[4][1])
        Sorter.insertion_sort(sorting2)
        sorting2.reverse()
        hold = len(self.ht)
        keys = list(self.ht.keys())
        index = 0
        while len(self.sortedht) < hold and index < len(sorting2):
            for k in keys:
                if k not in self.ht:
                    continue
                v = self.ht[k]
                if sorting2[index] == v[4][1] and k not in self.sortedht:
                    self.sortedht[k] = v
                    del self.ht[k]
                    break
            index += 1
        for k,v in self.sortedht.items():
            self.insert(k,v)
        
       
class Preferance:
    def __init__(self, ui):
        self.orginiz = pd.read_csv("charities.csv")
        self.m = ui
        self.ht = Hash()
        #Output for author name with textbox for input
        self.n_category = tkinter.Button(self.m, text="Domestic Needs", command=lambda: self.set_searchword("Domestic Needs"))
        self.n_category.grid(row=2)
        self.n_category1 = tkinter.Button(self.m, text="International Needs", command=lambda: self.set_searchword("International Needs"))
        self.n_category1.grid(row=3)
        self.n_category2 = tkinter.Button(self.m, text="Medical", command=lambda: self.set_searchword("Medical"))
        self.n_category2.grid(row=4)
        self.n_category3 = tkinter.Button(self.m, text="Youth", command=lambda: self.set_searchword("Youth"))
        self.n_category3.grid(row=5)
        self.n_category4 = tkinter.Button(self.m, text="Environment & Animals", command=lambda: self.set_searchword("Environment & Animals"))
        self.n_category4.grid(row=6)
        self.n_category5 = tkinter.Button(self.m, text="Health", command=lambda: self.set_searchword("Health"))
        self.n_category5.grid(row=7)
        self.n_category6 = tkinter.Button(self.m, text="Religious", command=lambda: self.set_searchword("Religious"))
        self.n_category6.grid(row=8)
        self.n_category7 = tkinter.Button(self.m, text="Public Affairs", command=lambda: self.set_searchword("Public Affairs"))
        self.n_category7.grid(row=9)
        self.n_category8 = tkinter.Button(self.m, text="Education", command=lambda: self.set_searchword("Education"))
        self.n_category8.grid(row=10)
        self.n_category9 = tkinter.Button(self.m, text="Cultural", command=lambda: self.set_searchword("Cultural"))
        self.n_category9.grid(row=11)
        self.output = tkinter.Text(self.m)
        self.output.grid(row=2,column=4)
        self.search_entry = tkinter.Text(self.m, width=20, height=1)
        self.search_entry.grid(row=1)
        self.search_button = tkinter.Button(self.m, text="Search", command=self.selection)
        self.search_button.grid(row=1, column=3)
        #Start the program
    def printer(self):
        self.output.delete("1.0", "end")
        self.output.insert("1.0", self.ht.variables)
    def set_searchword(self, word):
        self.category = word
        self.find_organization()
    def get_searchword(self):
        return self.category
    def find_organization(self):
        self.ht.ht = {}
        self.ht.sortedht = {}
        self.selected = self.orginiz.groupby("category").get_group(self.category)
        names = self.selected["name"].tolist()
        charity = self.selected.drop(self.selected.iloc[:,0:2], axis=1)
        processing = []
        num = 0
        while len(processing) < len(charity):
            row = {}
            for k,v in zip(charity.columns.tolist(), charity.loc[charity.index[num]].tolist()):
                if k == "fundraising efficiency %" or k == "charitable commitment %":
                    v = int(v)
                row[k] = v
            processing.append(list(row.items()))
            num += 1
        for item in range(0, len(names)):
            self.ht.insert(names[item], processing[item])
        self.ht.sort()
        self.ht.copycat = self.ht.ht.copy()
        self.ht.print()
        self.printer()
    def selection(self):
        names = self.orginiz['name'].to_list()
        relevant = pd.read_csv("charities.csv", index_col='name')
        name = self.search_entry.get("1.0", "end-1c")
        for items in names:
            if name == items:
                self.output.delete("1.0", "end")
                self.output.insert("1.0", relevant.loc[items])
                return
        tkinter.messagebox.showinfo(message="Not an orginaztion in the database")
            
class Testmain(unittest.TestCase):
    def test_find_organization(self):
        pass
    def test_selection(self):
        pass
    def test_insertion_sort(self):
        pass
    def test_get(self):
        pass
    def test_insert(self):
        pass
    def test_remove(self):
        pass



if __name__ == "__main__":
    tester = tkinter.Tk()
    testing = Preferance(tester)
    tester.mainloop()
