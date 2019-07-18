import os
import shutil

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
        for name in self.Contents_Names:
            extension = os.path.splitext(self.New_Folder_Dir+"\\"+name)[1]
      #      print(extension)
            os.rename(self.New_Folder_Dir+"\\"+name,self.New_Folder_Dir+"\\"+List_Of_New_Names[i]+extension)
            i+=1
        print("renaming is done")

x=Direcrory("G:\DONE\Corpse Party(shityyyyyy)");
x.Print_Current_Directory_Contents_Names();
x.Make_New_Folder("newsss")
x.Copy_Directory_Content_To_The_New_Folder()
xn=["Corpse Party_ Tortured Souls OVA 001","Corpse Party_ Tortured Souls OVA 002","Corpse Party_ Tortured Souls OVA 003","Corpse Party_ Tortured Souls OVA 004","x"]
x.Rename_The_Contents_Of_The_New_Folder(xn)