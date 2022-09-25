


from importlib.resources import path
from msilib.schema import Directory
from os import mkdir
from re import sub
from sys import flags
from tkinter import W


dir_List = []
child_List = []
nodes_List = []
current_node = 0
root_node = 0
cd_count=0
working_dir="/"
term="root:"
doll="$"











class TreeNode:
    def __init__(self, data):
        self.data = data
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

    def dir_list(self):
      dir_List.append(self.data)
      if self.children:
        for child in self.children:
          child.dir_list()

    def nodes_list(self):
      global nodes_List
      nodes_List = self.children
      # nodes_List= copy.deepcopy(self.children)

    def node_data(self):
      print(self.data)




#FUNCTION TO ADD NODE
def add_node(type, name):
  global current_node
  if type=="mkdir":
    name="/"+name
    new_node= TreeNode(name)
    # print(current_node)
    current_node.add_child(new_node)
  elif type=="touch":
    new_node= TreeNode(name)
    # print(current_node)
    current_node.add_child(new_node)




def func_cd(dir_name,flag="cd: No such file or directory"):

  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global term 
  global doll

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)

  if len(dir_name)>=2 and dir_name[0]=="/":
    dir_name=dir_name[1:]    


  # print(dir_name)


  directory = "/" + dir_name

  path_list = dir_name.split('/')

  while("" in path_list):
    path_list.remove("")

  print(cd_count)

  if dir_name==".":
    pass

  elif dir_name=="..":
    # parent_dir(working_dir)
    pass
    
  elif "./" in dir_name:
    pass

  elif dir_name=="/":
    term="root:"
    working_dir="/"
    cd_count=0
    current_node=root_node  
    
  elif dir_name in dir_List:
    print("cd: Destination is a file")


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
    print(flag)

def mkdir_p(path_list):
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global term 
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
        print(directory)
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
  global term 
  global doll

  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)

  temp_node=current_node
  temp_working=working_dir

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
  
  if flag=="true":
    mkdir_p(path_list)
    # pass


def func_touch(sub_query):
  add_node("touch",sub_query)




def main():
  # global variables
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global term 
  global doll
  # print(working_dir)


  #Creating first node of root
  root = TreeNode("root/")
  current_node=root
  root_node = root
  # root.add_node("/a")

  a = True
  while(a):

    #SAFE CODE BEGINS
    print(term+working_dir+doll, end=" ")
    query= input() 

    #if else ladder for queries
    if(len(query) != 0):

      a = query.split(" ")
      a[0] = str(a[0]).strip()
      if(a[0]== "exit"):
        a=False
        print("bye, root")

      elif(a[0] == "pwd"):
        print(working_dir)
      
      #SAFE CODE ENDS

      elif(a[0]=="cd"):
        try:
          sub_query = str(a[1]).strip()
          # print(sub_query)
          func_cd(sub_query)
        except:
          print("cd: Invalid syntax") 


      elif(a[0]=="mkdir"):
        try:
          sub_query=str(a[1]).strip()
          if sub_query=="-p":
            try: 
              sub_query=str(a[2]).strip()
              func_mkdir(sub_query,"true")
            except:
              pass
          else:
            func_mkdir(sub_query,"false")
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
          pass


      elif(a[0]=="tree"):
          root_node.print_tree()

      else:
        print(a[0]+": Command not found")
  pass








if __name__ == '__main__':
    main() 