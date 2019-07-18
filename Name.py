import os
import re
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


y=Name("G:\DONE\Corpse Party(shityyyyyy)");
y.Print_Current_Directory_Contents_Names();
y.Word_Before_The_Episode_Number("OVA")
y.Rename_Episodes("x","Naruto x")