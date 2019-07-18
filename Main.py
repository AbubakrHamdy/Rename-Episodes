import os
import shutil
import re

class Direcrory:
    def __init__(self,current_dir):
        self.Current_Dir=current_dir
        self.Contents_Names=os.listdir(self.Current_Dir)

    def Print_Current_Directory_Contents_Names(self):
        print(self.Contents_Names)

    def Make_New_Folder(self,name):
        self.New_Folder_Name=name
        self.New_Folder_Dir=self.Current_Dir+"\\"+name
        if not os.path.exists(self.New_Folder_Dir):
            os.mkdir(self.New_Folder_Dir)
            print("Directory ", self.New_Folder_Dir, " Created ")
        else:
            print("Directory ", self.New_Folder_Dir, " already exists")
    def Copy_Directory_Content_To_The_New_Folder(self):
        for name in self.Contents_Names:
            shutil.copy2(self.Current_Dir+"\\"+name,self.New_Folder_Dir )
        print("copy is done")
    def Rename_The_Contents_Of_The_New_Folder(self,List_Of_New_Names):
        i=0
        for name in List_Of_New_Names:
            extension = os.path.splitext(self.New_Folder_Dir+"\\"+self.Contents_Names[i])[1]
            print(extension)
            os.rename(self.New_Folder_Dir+"\\"+self.Contents_Names[i],self.New_Folder_Dir+"\\"+name+extension)
            i+=1
        print("renaming is done")


class Name:
    def __init__(self,current_dir):
        self.Current_Dir=current_dir
        self.Contents_Names=os.listdir(self.Current_Dir)

    def Print_Current_Directory_Contents_Names(self):
        print(self.Contents_Names)

    def Word_Before_The_Episode_Number(self,word):
        self.Founds=[]
        regex=""

        for char in word:
            regex+="["+char.lower()+char.upper()+"]"

        regex+=" *\d*"
        print(regex)
        for names in self.Contents_Names:
            print(names)
            temp=re.findall(regex,names)
            if(len(temp)>0):
                self.Founds.append(temp[0])
                #regex.count("ss",22,4546,65765)
        print(self.Founds)

    def Rename_Episodes(self,Special_Word,Episode_Name):
        self.New_Names=[]
        for name in self.Founds:
            ep_num=re.findall("[0-9]+",name)
            print(ep_num)

            if (len(ep_num) > 0):
                newname=Episode_Name.replace(Special_Word,ep_num[0])
                self.New_Names.append(newname)
        print(self.New_Names)


x=Direcrory("G:\\DONE\\Naruto\\test");
x.Make_New_Folder("newsss")
x.Copy_Directory_Content_To_The_New_Folder()

y=Name("G:\\DONE\\Naruto\\test");
y.Print_Current_Directory_Contents_Names();
y.Word_Before_The_Episode_Number("Episode")
y.Rename_Episodes("x","Naruto Episode  x")

x.Rename_The_Contents_Of_The_New_Folder(y.New_Names)