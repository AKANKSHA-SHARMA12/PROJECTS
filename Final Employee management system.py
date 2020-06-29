#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:23:44 2020

@author: HP
"""

class Emp:
    dict_emp={}
    def __init__(self):
        self.ID=0
        self.name=""
        self.type=""
        
    def __str__(self):
        return "ID: "+str(self.ID)+"Name: "+self.name+"Type "+self.type
    
    def add(self):
        Emp.dict_emp[self.ID]=self
        
    def search(self,ID):
        e=Emp.dict_emp.get(ID)
        if e!=None:
            self.ID=e.ID
            self.name=e.name
            self.type=e.type
        else:
             raise exception ("ID not found")
    
    def delete(self,ID):
        if Emp.dict_emp.get(ID)!=None:
            Emp.dict_emp.pop(ID)
        else:
            raise exception ("Id already exist")
    
    def modify(self,ID):
        e=Emp.dict_emp.get(ID)
        if e!=None:
            e.ID=self.ID
            e.name=self.name
            e.type=self.type
        else:
            raise exception ("ID not found")
    @staticmethod
    def OBJ(ID):
        e=Emp.dict_emp.get(ID)
        if e!=None:
            if e.type=="Dir":
                obj=Dir()
                obj.type="Dir"
                
                return obj
            elif e.type=="Mgr":
                obj=Mgr()
                obj.type="Mgr"
                
                return obj
            elif e.type=="TT":
                obj=TT()
                obj.type="Mgr"
                
                return obj
    @staticmethod
    def getAllEmpinDict():
        return Emp.dict_emp

    
class Dir(Emp):
    
    def __init__(self):
        super().__init__()
        self.dirspecial=""
        self.share=""
    def __str__(self):
        strsuper=super().__str__()
        strdata= "Dirspecial: "+self.dirspecial+"Share "+self.share
        return strsuper+strdata    
       
    def add(self):
        super().add()
               
    def search(self,ID):
        super().search(ID)
        e=Emp.dict_emp.get(ID)
        if e!=None:
            self.dirspecial=e.dirspecial            
            self.share=e.share
        else:
            raise exception ("ID not found")
    
    def delete(self,ID):
        super().delete(ID)
    
    def modify(self,ID):
        super().modify(ID)
        e=Emp.dict_emp.get(ID)
        if e!=None:
            e.dirspecial=self.dirspecial
            e.share=self.share
        else:
            raise exception ("ID not found")

class Mgr(Emp):
    
    def __init__(self):
        super().__init__()
        self.mgrspecial=""
        self.incentives=""
    def __str__(self):
        strsuper=super().__str__()
        strdata= "mgrspecial: "+self.mgrspecial+"incentives "+self.incentives
        return strsuper+strdata    
       
    def add(self):
        super().add()
               
    def search(self,ID):
        super().search(ID)
        e=Emp.dict_emp.get(ID)
        if e!=None:
            self.mgrspecial=e.mgrspecial            
            self.incentives=e.incentives
        
        else:
            raise exception ("ID not found")
    
    def delete(self,ID):
        super().delete(ID)
    
    def modify(self,ID):
        super().modify(ID)
        e=Emp.dict_emp.get(ID)
        if e!=None:
            e.mgrspecial=self.mgrspecial
            e.incentives=self.incentives
            
        else:
            raise exception ("ID not found")
            
class TT(Emp):
    
    def __init__(self):
        super().__init__()
        self.TTspecial=""
        self.salary=""
    def __str__(self):
        strsuper=super().__str__()
        strdata= "TTspecial: "+self.TTspecial+"salary "+self.salary
        return strsuper+strdata    
       
    def add(self):
        super().add()
               
    def search(self,ID):
        super().search(ID)
        
        e=Emp.dict_emp.get(ID)
        if e!=None:
            self.TTspecial=e.TTspecial            
            self.salary=e.salary
            
        else:
            raise exception ("ID not found")
    
    def delete(self,ID):
        super().delete(ID)
    
    def modify(self,ID):
        super().modify(ID)
        e=Emp.dict_emp.get(ID)
        if e!=None:
            e.TTspecial=self.TTspecial
            e.salary=self.salary
            
        else:
            raise exception ("ID not found")

#PL
def showAllEmp():
    dict_in_pl=Emp.getAllEmpinDict()
    for e in dict_in_pl.values():
        print(e)
        
while(True):
    try:
        print("\n1.Add\n2.Search\n3.Delete\n4.Modify\n5.Show all\n6.Exist")
        ch=input("Enter your choice")
        if ch=="1":
            print("\n1.Director\n2.Manager\n3.Trainer")
            cho=input("Enter your choice")
            
            if cho=="1":
                try:
                    obdir=Dir()
                    obdir.type="Dir"
                    while(True):
                        try:
                            obdir.ID=int(input("Enter ID"))
                            break
                        except Exception as ex:
                            print(ex)
                    obdir.name=input("Enter Name:")
                    obdir.dirspecial=input("Enter dir special")
                    obdir.share=input("Enter Share")
                    obdir.add()
                    print("Director added succesfully")
                except Exception as ex:
                    print(ex)

            elif cho=="2":
                try:
                    obmgr=Mgr()
                    obmgr.type="Mgr"
                    while(True):
                        try:
                            obmgr.ID=int(input("Enter ID"))
                            break
                        except Exception as ex:
                            print(ex)
                    obmgr.name=input("Enter Name:")
                    obmgr.mgrspecial=input("Enter mgr special")
                    obmgr.incentives=input("Enter Incentives")
                    obmgr.add()
                    print("Manager added succesfully")
                except Exception as ex:
                    print(ex)
            
            elif cho=="3":
                try:
                    obTT=TT()
                    obTT.type="TT"
                    while(True):
                        try:
                            obTT.ID=int(input("Enter ID"))
                            break
                        except Exception as ex:
                            print(ex)
                    obTT.name=input("Enter Name:")
                    obTT.TTspecial=input("Enter TT special")
                    obTT.salary=input("Enter salary")
                    obTT.add()
                    print("Trainer added succesfully")
                except Exception as ex:
                         print(ex)
        
        elif ch=="2":
            while(True):
                try:
                    while(True):
                            try:
                                ID=int(input("Enter ID"))
                                break
                            except Exception as ex:
                                print(ex)
                    obj=Emp.OBJ(ID)
                    obj.search(ID)
                    print(obj)
                    break
                except Exception as ex:
                        print(ex)
       
        elif ch=="3":
            while(True):
                try:
                    while(True):
                        try:
                            ID=int(input("Enter ID"))
                            break
                        except Exception as ex:
                            print(ex)
                    obj=Emp.OBJ(ID)
                    obj.delete(ID)
                    print(obj)
                except Exception as ex:
                        print(ex)
        elif ch=="4":
            while(True):
                try:
                    while(True):
                        try:
                            ID=int(input("Enter ID"))
                            break
                        except Exception as ex:
                            print(ex)
                    obj=Emp.OBJ(ID)
                    obj.name=input("Enter name to modify:")
                    if obj.type=="Dir":
                        obj.dirspecial=input("Enter Director special")
                        obj.share=input("Enter share")
                    elif obj.type=="Mgr":
                        obj.mgrspecial=input("Enter manager special")
                        obj.incentives=input("Enter incentives")
                    elif obj.type=="TT":
                        obj.TTspecial=input("Enter trainer special")
                        obj.salary=input("Enter salary")
                    obj.modify(ID)
                    print("Employee modified successfully")
                except Exception as ex:
                        print(ex)
        
        elif ch=="5":
            showAllEmp()
        elif ch=="0":
             break
    except Exception as ex:
            print(ex)
               
            
            
            
            
            
            


# In[ ]:




