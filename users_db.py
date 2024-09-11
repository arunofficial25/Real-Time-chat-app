class UsersDB():
    users_list=[{"user":"Ben","password":"Ben-Ten"},{"user":"Gwen","password":"Gwen-Ten"}]

    def read_db(self,user_name:str,password:str):
        #print("Iniciando sesion.... ")
        for i in self.users_list:
            if (i["user"]==user_name and i["password"]==password):
                return True
        return False
    
  
    def write_db(self,user_name:str,password:str):
        #print("Creando usuario...")
        self.users_list.append({"user":user_name,"password":password})
        return True

