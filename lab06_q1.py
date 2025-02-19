class Password:
    def __init__(self):
        self.old_password=[]
    
    def set_password(self,new_pass):
        if new_pass not in self.old_password:
            self.old_password.append(new_pass)
            return 1
        else:
            return 0  
    
    def get_password(self):
        if self.old_password: 
            return "current_password: "+self.old_password[-1]
        else:
            return "old_password list is empty"
            
    def is_correct(self,string):
        if self.old_password:
            return string==self.old_password[-1]
        else:
            return -1    
c1=Password()
while True:
    choice=int(input("Enter the choice:\n1.set_password()\n2.get_password()\n3.is_correct()\n4.exit\n"))
    match choice:
        case 1: 
            string=input("Enter the new_password:")
            print(c1.set_password(string)) #it return 1 for success and 0 for failure
        case 2:
            print(c1.get_password())
        case 3:
            check_string=input("Enter the string you want to compare:")
            print(c1.is_correct(check_string))# return -1 if list is empty 
        case 4:
            exit()
