from glob import glob
from platform import node


dir_List = []
child_List = []
nodes_List = []
current_node = 0
root_node = 0
cd_count=0
working_dir="/"
term="root:"
doll="$"

dir_List = []

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
    
    def child_list(self):
      global child_List
      for child in self.children:
        child_List.append(child.data)
      print(child_List)

    def nodes_list(self):
      global nodes_List 
      nodes_List= self.children
      print(nodes_List)

    def add_node(self, type, filename):
      if(type=="mkdir"):
        filename="/"+filename
        file = TreeNode(filename)
        self.add_child(file)
      elif(type=="touch"):
        file = TreeNode(filename)
        print(file)
        self.add_child(file)
        self.print_tree()
        

    def mkdir_with_p(self,value):
      print(value)
      substring = value.split('/')
      print(substring)
      global current_node
      global root_node
      for item in substring:
        if(item!=""):
          new_node=TreeNode("/"+item)
          current_node.add_child(new_node)
          current_node=new_node
      current_node=self


def cng_dir(index_num, direname):
  global current_node
  global nodes_List
  global working_dir
  working_dir = working_dir + direname
  current_node=nodes_List[index_num]
  pass

def initial_dir():
  global nodes_List
  global dir_List
  global current_node
  del dir_List[:]
  del nodes_List[:]
  print(current_node)
  current_node.dir_list()
  current_node.nodes_list()
  current_node.child_list()
  dir_List.pop(0)
  print(dir_List)


def func_cd(dir_name):
  global dir_List
  global child_List
  global nodes_List
  global root_node
  global current_node
  global working_dir 
  global cd_count
  global term 
  global doll
  #creating lists
  dir_List.clear()
  nodes_List.clear()
  # print(current_node)
  current_node.dir_list()
  current_node.nodes_list()
  print(dir_List)
  dir_List.pop(0)

  # substring = dir_name.split('/')
  directory_name = "/" + dir_name 


  if dir_name==".":
    pass
  
  elif dir_name=="/":
    term="root:"
    working_dir="/"
    cd_count=0
    current_node=root_node

  elif dir_name=="..":
    # parent_dir(working_dir)
    pass

  elif "./" in dir_name:
    pass

  elif len(dir_name) >=2 and dir_name[0]=="/":
    if dir_name in dir_List:
      index_num = dir_List.index(dir_name)
      if cd_count==0:
        working_dir = working_dir + dir_name[1:]
        cd_count=cd_count+1
        current_node=nodes_List[index_num]
      else:
        working_dir = working_dir + dir_name[1:]
        current_node=nodes_List[index_num]

  elif directory_name in dir_List:
    index_num = dir_List.index(directory_name)
    if cd_count==0:
      working_dir = working_dir + directory_name[1:]
      cd_count=cd_count+1
      current_node=nodes_List[index_num]
    else:
      working_dir = working_dir + directory_name
      cd_count=cd_count+1
      current_node=nodes_List[index_num]

  elif dir_name in dir_List:
    print("cd: Destination is a file")

  else:
    print("cd: No such file or directory")

  # else:
  #   for item in range(0, len(substring)):
      
      
  #     if substring[item] != "":
  #       initial_dir()
  #       print(dir_List)
  #       direname= "/"+ substring[item]
  #       print(substring[item])
  #       if substring[item] in dir_List:
  #         print("cd: Destination is a file")

  #       elif direname in dir_List:
  #         print("found")
  #         index_num = child_List.index(direname)
  #         print(index_num)

  #         if cd_count==0:
  #           cng_dir(index_num, direname[1:])

  #         else:
  #           cng_dir(index_num, direname)

  #       else:
  #         print("cd: No such file or directory")



def func_mkdir(name,dir_name):
  pass

  









def main():
  #global variables
  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global term 
  global doll


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

      if(a[0]== "exit"):
        a=False
        print("bye, root")
        root.print_tree()

      elif(a[0] == "pwd"):
        print(working_dir)
      
      #SAFE CODE ENDS

      elif(a[0]=="cd"):
        try:
          sub_query =str(a[1]).strip()
          # print(sub_query)
          func_cd(sub_query)
        except:
          print("cd: Invalid syntax") 


      elif(a[0]=="mkdir"):
        try:
          name = str(a[0]).strip()
          sub_query =str(a[1]).strip()
          func_mkdir(name)
        except:
          print("mkdir: Invalid syntax") 
          pass

      elif(a[0]=="touch"):
        print("touch")
        try:
          file_name = str(a[1]).strip()
          current_node.add_node("touch", file_name)
          print(current_node)
          initial_dir()

        except:
          print("cd: Invalid syntax") 

  pass








if __name__ == '__main__':
    main() 