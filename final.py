


dir_List = []
child_List = []
nodes_List = []
child_node_List = []
user_List= ["root"]
parent_node=0
current_node = 0
root_node = 0
cd_count=0
working_dir="/"
username="root"
doll="$"
anc_dir=1
des_file=1











class TreeNode:
    def __init__(self, data):
        self.data = data
        self.perms="-rw-r--"
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def child_nodes(self):
      global child_List
      for child in self.children:
        child_List.append(child.data)
    
    def child_node_list(self):
      global child_node_List
      child_node_List.clear()
      for child in self.children:
        child_node_List.append(child.data)
    
    def dir_list(self):
      dir_List.append(self.data)
      if self.children:
        for child in self.children:
          child.dir_list()

    def nodes_list(self):
      
      global nodes_List
      # nodes_List.clear()
      nodes_List = self.children

    def node_data(self):
      print(self.data)

    def childCount(self):
      length= len(self.children)
      print(length)
      return length

    def removeChild(self,node_adr):

       for child in self.children:
        if node_adr==child:
            # print(self.children)
            self.children.remove(child)
            # print(self.children)
            break
        else:
          child.removeChild(node_adr)
    
    def get_parent(self,node_name):
      global parent_node
      if self.children:
        for child in self.children:
          if child.data== node_name:
            parent_node=self
      else:
        for child in self.children:
          child.dir_list()
      pass

#FUNCTION TO ADD NODE
def add_node(type, name):
  global current_node
  if type=="mkdir":
    name="/"+name
    new_node= TreeNode(name)
    current_node.add_child(new_node)
  elif type=="touch":
    new_node= TreeNode(name)
    current_node.add_child(new_node)


def func_cd(dir_name,str="cd: No such file or directory",extr="false"):

  # extr=false means no other function is not calling it
  # if true other function calls it
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir
  global des_file
  temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)


  if len(dir_name)>=2 and dir_name[0]=="/":
    dir_name=dir_name[1:]    




  directory = "/" + dir_name

  path_list = dir_name.split('/')

  while("" in path_list):
    path_list.remove("")

  

  if dir_name==".":
    pass

  elif dir_name=="..":
    # parent_dir(working_dir)
    pass
    
  elif "./" in dir_name:
    pass

  elif dir_name=="/":
    username="root"
    working_dir="/"
    cd_count=0
    current_node=root_node  
    
  elif (dir_name in dir_List) and extr=="false":
    print("cd: Destination is a file")
    des_file=0


  elif len(path_list)>1:
    for item in path_list:
      func_cd(item)

  

  elif directory in dir_List:
    index_num = dir_List.index(directory)
    if cd_count==0:
      working_dir = working_dir + directory[1:]
      cd_count=cd_count+1
      current_node=nodes_List[index_num]
    else:
      working_dir = working_dir + directory
      current_node=nodes_List[index_num]

  
  else:
    print(str)
    anc_dir=0

  if(des_file==0):
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count

def func_cd_multiple(query):
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll

  temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count



  query=query.split("/")
  while("" in query):
    query.remove("")
    

  for item in query:
    current_node.child_nodes()
    current_node.nodes_list()

    directory="/"+item
    if item==".":
      pass

    elif item=="..":
      pass

    elif directory in child_List:
      index_num = child_List.index(directory)
      if cd_count==0:
        working_dir = working_dir + directory[1:]
        cd_count=cd_count+1
        current_node=nodes_List[index_num]
      else:
        working_dir = working_dir + directory
        cd_count=cd_count+1
        current_node=nodes_List[index_num]
    elif item in child_List:
      print("cd: Destination is a file")
      current_node=temp_node
      working_dir=temp_working
      cd_count=temp_cd_count
    else:
      print("cd: No such file or directory")
      current_node= temp_node
      working_dir=temp_working
      cd_count=temp_cd_count

    child_List.clear()

def mkdir_p(path_list):
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll


  temp_node = current_node
  temp_working=working_dir
  temp_cd_count=cd_count
  if len(path_list)==1:
    name="/"+path_list[0]
    if name in dir_List:
      pass
    else:
      add_node("mkdir",path_list[0])

  if len(path_list)>1:
    for item in range(0, len(path_list)):

      del dir_List[:]
      current_node.dir_list()
      current_node.nodes_list()
      dir_List.pop(0)

      name=path_list[item]
      directory="/"+path_list[item]

      if item==(len(path_list)-1):
        if directory in dir_List:
          func_cd(directory[1:])
        else:
          func_mkdir(directory[1:],"false")
      
      else:

        if directory in dir_List:
          func_cd(directory[1:])
        else:
          func_mkdir(directory[1:],"false")
          func_cd(directory[1:])
        

  current_node=temp_node
  working_dir=temp_working
  cd_count=temp_cd_count

def func_mkdir(sub_query, flag="false"):

  #flag =false if -p is not their
  #flag =true if -p is their
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)

  temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  path_list=sub_query.split('/')
  
  while("" in path_list):
    path_list.remove("")
  
  if flag=="false":
    dir_name = "/" + sub_query

  elif len(path_list)==1 and flag=="false":
    dir_name = "/" + path_list[0]
    sub_query=path_list[0]

  if len(path_list)==1 and flag=="false":
    if dir_name in dir_List:
      print("mkdir: File exists")
    elif sub_query in dir_List:
      print("mkdir: File exists")
    else:
      add_node("mkdir",sub_query)


  if len(path_list)>1 and flag=="false":
    for item in range(0, len(path_list)):
      if item==(len(path_list)-1):
        func_mkdir(path_list[item],"false")
      else:
        func_cd(path_list[item], "mkdir: Ancestor directory does not exist")
        if(temp_node==current_node):
          break
  current_node=temp_node
  working_dir=temp_working
  cd_count=temp_cd_count
  
  if flag=="true":
    mkdir_p(path_list)

def func_touch(sub_query):

  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)

  temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  path_list=sub_query.split('/')
  
  while("" in path_list):
    path_list.remove("")

  
  if len(path_list)==1:
    item=path_list[0]
    if item in dir_List:
      pass
    else:
      add_node("touch",item)
  elif len(path_list)>1:
    for item in range(0,len(path_list)):
      if item==(len(path_list)-1):
        if path_list[item] in dir_List:
          pass
        else:
          func_touch(path_list[item])
      else:
        name="/"+path_list[item]
        func_cd(name, "touch: Ancestor directory does not exist","true")
      
      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break
  current_node=temp_node
  working_dir=temp_working
  cd_count=temp_cd_count

def fun_cp(file_path, dest_path):
  
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)
  temp_node_it=temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  temp_des=dest_path
  file_path=file_path.split('/')
  dest_path=dest_path.split('/')

  while("" in file_path):
    file_path.remove("")
  
  while("." in file_path):
    file_path.remove(".")
  
  while(".." in file_path):
    file_path.remove("..")

  

  while("" in dest_path):
    dest_path.remove("")
  
  while("." in dest_path):
    dest_path.remove(".")
  
  while(".." in dest_path):
    dest_path.remove("..")

  file_path_exists="false"
  dest_path_exists="false"

  
  if len(dest_path)>=1:
    for item in range(0,len(dest_path)):
      if item==(len(dest_path)-1):
        for_dir="/"+dest_path[item]
        if dest_path[item] in dir_List:
          print("cp: File exists")
        elif for_dir in dir_List:
          print("cp: Destination is a directory")
          break
        else:
          dest_path_exists="true"
      else:
        func_cd(dest_path[item],"cp: No such file or directory", "true")
      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count   

  
  if len(file_path)>=1 and dest_path_exists=="true":
    for item in range(0,len(file_path)):
      if item==(len(file_path)-1):
        for_dir="/"+file_path[item]
        if file_path[item] in dir_List:
          file_path_exists="true"
        elif for_dir in dir_List:
          print("cp: Source is a directory")
        else:
          print("cp: No such file")
      else:
        func_cd(file_path[item],"cp: No such file or directory")

      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count 




  if file_path_exists=="true" and dest_path_exists=="true":
    func_touch(temp_des)  
  
  current_node=temp_node
  working_dir=temp_working
  cd_count=temp_cd_count 



def fun_mv(file_path, dest_path):
  global child_List
  global nodes_List
  global dir_List
  global child_node_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)
  temp_node_it=temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  temp_des=dest_path
  file_path=file_path.split('/')
  dest_path=dest_path.split('/')

  while("" in file_path):
    file_path.remove("")
  
  while("." in file_path):
    file_path.remove(".")
  
  while(".." in file_path):
    file_path.remove("..")

  while("" in dest_path):
    dest_path.remove("")
  
  while("." in dest_path):
    dest_path.remove(".")
  
  while(".." in dest_path):
    dest_path.remove("..")

  file_path_exists="false"
  dest_path_exists="false"

  
  if len(dest_path)>=1:
    for item in range(0,len(dest_path)):
      if item==(len(dest_path)-1):
        for_dir="/"+dest_path[item]
        if dest_path[item] in dir_List:
          print("mv: File exists")
        elif for_dir in dir_List:
          print("mv: Destination is a directory")
          break
        else:
          dest_path_exists="true"
      else:
        func_cd(dest_path[item],"mv: No such file or directory", "true")
      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count   

  
  if len(file_path)>=1 and dest_path_exists=="true":
    for item in range(0,len(file_path)):
      if item==(len(file_path)-1):
        for_dir="/"+file_path[item]
        if file_path[item] in dir_List:
          # print("current node data")
          # print(current_node.data)
          current_node.child_node_list()
          # print("printing child nodes list")
          # print(child_node_List)
          index_num = child_node_List.index(file_path[item])
          # print(index_num)
          # print("printing child nodes name list")
          current_node.nodes_list()
          # print(nodes_List[index_num])
          # print(nodes_List[index_num].data)
          current_node.removeChild(nodes_List[index_num])
          file_path_exists="true"
        elif for_dir in dir_List:
          print("mv: Source is a directory")
        else:
          print("mv: No such file")
      else:
        func_cd(file_path[item],"mv: No such file or directory")

      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count 




  if file_path_exists=="true" and dest_path_exists=="true":
    func_touch(temp_des)  
  
  current_node=temp_node
  working_dir=temp_working
  cd_count=temp_cd_count


def fun_rm(file_path):

  global child_List
  global nodes_List
  global dir_List
  global child_node_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)
  temp_node_it=temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  file_path=file_path.split('/')

  while("" in file_path):
    file_path.remove("")
  
  while("." in file_path):
    file_path.remove(".")
  
  while(".." in file_path):
    file_path.remove("..")

  if len(file_path)>=1:
    for item in range(0,len(file_path)):
      if item==(len(file_path)-1):
        for_dir="/"+file_path[item]
        if file_path[item] in dir_List:
          # print("current node data")
          # print(current_node.data)
          current_node.child_node_list()
          # print("printing child nodes list")
          # print(child_node_List)
          index_num = child_node_List.index(file_path[item])
          # print(index_num)
          # print("printing child nodes name list")
          current_node.nodes_list()
          # print(nodes_List[index_num])
          # print(nodes_List[index_num].data)
          current_node.removeChild(nodes_List[index_num])
          file_path_exists="true"
        elif for_dir in dir_List:
          print("rm: Is a directory")
        else:
          print("rm: No such file")
      else:
        func_cd(file_path[item],"rm: No such file")

      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count
  pass

def fun_rmdir(file_path):
  
  global child_List
  global nodes_List
  global dir_List
  global child_node_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll
  global anc_dir

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)
  temp_node_it=temp_node=current_node
  temp_working=working_dir
  temp_cd_count=cd_count

  if file_path=="/":
    if working_dir!="/":  
      root_node.get_parent(working_dir)
      # print(parent_node)
      # print(parent_node.data)
      length=parent_node.children
      length_arr=len(length)
      # print(length_arr)
      if length_arr>0:
        print("rmdir: Directory not empty")
      else:
        print("rmdir: Cannot remove pwd")
    else:
      print("rmdir: Cannot remove pwd")


  elif file_path==".":
    print("rmdir: Cannot remove pwd")

  elif file_path=="..":

    if working_dir!="/":  
      root_node.get_parent(working_dir)
      # print(parent_node)
      # print(parent_node.data)
      length=parent_node.children
      length_arr=len(length)
      # print(length_arr)
      if length_arr>0:
        print("rmdir: Directory not empty")
      else:
        print("rmdir: Cannot remove pwd")
    else:
      print("rmdir: Cannot remove pwd")

  file_path=file_path.split('/')

  while("" in file_path):
    file_path.remove("")
  
  while("." in file_path):
    file_path.remove(".")
  
  while(".." in file_path):
    file_path.remove("..")
  if len(file_path)==1:
    fp="/"+file_path[0]
    if working_dir==fp:
      print("rmdir: Cannot remove pwd")
      return

  if len(file_path)>=1:
    for item in range(0,len(file_path)):
      if item==(len(file_path)-1):
        for_dir="/"+file_path[item]
        # print(dir_List)
        if file_path[item] in dir_List:
          print("rmdir: Not a directory")
        elif for_dir in dir_List:
          # print(current_node.data)
          # print("rmdir: Is a directory")
          current_node.child_node_list()
          # print("child")
          # print(child_node_List)
          current_node.nodes_list()
          # print(nodes_List)
          # for item in nodes_List:
          #   print(item.data)
          index_num = child_node_List.index(for_dir)
          # print("index")
          # print(index_num)
          # print(nodes_List[index_num].data)
          child=nodes_List[index_num].children
          # print("childrens")
          # print(child)
          # for items in child:
          #   print(items.data)
          # print(len(child))
          if len(child)>0:
            print("rmdir: Directory not empty")
          else:
            current_node.removeChild(nodes_List[index_num])
          # temp=nodes_List[index_num]
          # print("new list")
          # print(temp)
          # temp.child_node_list()
          # print(child_node_List)
          # current_node.nodes_list()
          # current_node.removeChild(nodes_List[index_num])
        else:
          print("rmdir: No such file or directory")
      else:
        func_cd(file_path[item],"rm: No such file")

      if(temp_node==current_node or anc_dir==0):
        anc_dir=1
        break 
  
    current_node=temp_node
    working_dir=temp_working
    cd_count=temp_cd_count

def main():
  # global variables
  global child_List
  global nodes_List
  global dir_List
  global user_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global username 
  global doll


  #Creating first node of root
  root = TreeNode("root/")
  current_node=root
  root_node = root
  # root.add_node("/a")

  a = True
  while(a):

    #SAFE CODE BEGINS
    print(username+":"+working_dir+doll, end=" ")
    query= input() 

    #if else ladder for queries
    if(len(query) != 0):

      a = query.split(" ")
      a[0] = str(a[0]).strip()
      if(a[0]== "exit"):
        a=False
        print("bye, "+username)

      elif(a[0] == "pwd"):
        try:
          sub_query = str(a[1]).strip()
          print("pwd: Invalid syntax")
        except:
          print(working_dir)
        
      
      #SAFE CODE ENDS

      elif(a[0]=="cd"):
        try:
          sub_query = str(a[1]).strip()
          if a[1]!="cd":
            query=sub_query.split("/")

            while("" in query):
              query.remove("")

            if len(query)<=1:
              func_cd(sub_query)
            else:
              func_cd_multiple(sub_query)
          else:
            print("cd: Invalid syntax") 
        except:
          print("cd: Invalid syntax") 


      elif(a[0]=="mkdir"):
        try:
          sub_query=str(a[1]).strip()
          if a[1]!="mkdir":
            if sub_query=="-p":
              try: 
                sub_query=str(a[2]).strip()
                func_mkdir(sub_query,"true")
              except:
                print("mkdir: Invalid syntax") 
                pass
            else:
              func_mkdir(sub_query,"false")
          else:
            print("mkdir: Invalid syntax") 
        except:
          print("mkdir: Invalid syntax") 

      elif(a[0]=="touch"):
        try:
          file_name = str(a[1]).strip()
          if file_name=="":
            pass
          else:
            func_touch(file_name)
        except:
          print("touch: Invalid syntax")
          pass

      elif(a[0]=="cp"):
        try:
          file_path=str(a[1]).strip()
          dest_path=str(a[2]).strip()
          fun_cp(file_path, dest_path)
        except:
          print("cp: Invalid syntax")
          pass
      
      elif(a[0]=="mv"):
        try:
          file_path=str(a[1]).strip()
          dest_path=str(a[2]).strip()
          fun_mv(file_path, dest_path)
        except:
          print("mv: Invalid syntax")
          pass

      elif(a[0]=="rm"):
        try:
          file_path=str(a[1]).strip()
          fun_rm(file_path)
        except:
          print("rm: Invalid syntax")
          pass

      elif(a[0]=="rmdir"):
        try:
          file_path=str(a[1]).strip()
          fun_rmdir(file_path)
        except:
          print("rmdir: Invalid syntax")
          pass    

      elif(a[0]=="adduser"):
        try:
          name=str(a[1]).strip()
          if username=="root" and name!="":
            if name in user_List:
              print("adduser: The user already exists")
            else:
              user_List.append(name)
        except:
          pass 
      
      elif(a[0]=="deluser"):
        try:
          name=str(a[1]).strip()
          if username=="root" and name!="":
            if name=="root" and username=="root":
              print("WARNING: You are just about to delete the root account\n"
              "Usually this is never required as it may render the whole system unusable\n"
              "If you really want this, call deluser with parameter --force\n"
              "(but this `deluser` does not allow `--force`, haha)\n"
              "Stopping now without having performed any action")
            elif (name in user_List) and name!="root":
              user_List.remove(name)
            elif (name not in user_List)  and name!="root":
              print("deluser: The user does not exist")
        except:
          pass 

      elif(a[0]=="su"):
        try:
          name=str(a[1]).strip()
          if username=="root" and name!="" and name!="root":
            if name in user_List:
              username=name
            elif (name not in user_List) and name!="root":
              print("su: Invalid user")
          if username!="root" and name=="root":
            username="root"
        except:
          username="root"
          pass 


      elif(a[0]=="child"):
        current_node.child_nodes()

      elif(a[0]=="users"):
        print(user_List)

      elif(a[0]=="tree"):
          root_node.print_tree()

      else:
        print(a[0]+": Command not found")
  pass







if __name__ == '__main__':
    main() 