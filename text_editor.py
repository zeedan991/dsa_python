class Simpleditor:
    def __init__(self):
        self.undo_list = []
        self.redo_list = []
        self.txt = ""
    
    def user_input(self ,user_txt):
        self.undo_list.append(self.txt)
        self.txt += user_txt
        
    def show_input(self):
        print("USER TEXT  : ",self.txt)
    
    def undo_edit(self):
        if not self.undo_list:
            print(" NOTHING TO UNDO  ")
            return
        else:
            self.redo_list.append(self.txt)
            self.txt = self.undo_list.pop(-1)
            print("TEXT UNDO  : ", self.txt )
            
            
        
    def redo_edit(self):
        if not self.redo_list:
            print("NOTHING TO REDO ")
            return
        else:
            self.undo_list.append(self.txt)
            self.txt = self.redo_list.pop(-1)
            print("TEXT REDO  : ", self.txt )
            
            
        

editor1 = Simpleditor()
editor1.user_input("hello ")
editor1.user_input("my ")
editor1.user_input("name ")
editor1.user_input("is ")
editor1.user_input("zeedan ")
editor1.show_input()
editor1.undo_edit()
editor1.undo_edit()
editor1.redo_edit()
editor1.redo_edit()

