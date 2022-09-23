

from final_code_func import initial_dir


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


# def initialize_value():
#   del dir_List[:]
#   del nodes_List[:]
#   current_node.dir_list()
#   current_node.nodes_list()
#   dir_List.pop(0)






#FUNCTION TO ADD NODE
def add_node(type, name):
  global current_node
  if type=="mkdir":
    name="/"+name
    new_node= TreeNode(name)
    print(current_node)
    current_node.add_child(new_node)
  elif type=="touch":
    new_node= TreeNode(name)
    print(current_node)
    current_node.add_child(new_node)

def func_mkdir(sub_query):
  # print(sub_query)
  # print(working_dir)
  add_node("mkdir",sub_query)


def func_cd(dir_name):

  global child_List
  global nodes_List
  global dir_List
  global root_node
  global current_node
  global cd_count
  global working_dir 
  global term 
  global doll

  # initial_dir()
  del dir_List[:]
  current_node.dir_list()
  current_node.nodes_list()
  dir_List.pop(0)

  # initial_dir()
  # print(dir_List)
  # print(nodes_List)
  # current_node.node_data()
  # print(current_node)
  # for item in nodes_List:
  #   item.node_data()
    # print(item)
    


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
    term="root:"
    working_dir="/"
    cd_count=0
    current_node=root_node  
    
  elif dir_name in dir_List:
    print("cd: Destination is a file")

  elif len(path_list)>1:
    print("To many paths")

  elif directory in dir_List:
    print("got it")
    index_num = dir_List.index(directory)
    if cd_count==0:
      working_dir = working_dir + directory[1:]
      cd_count=cd_count+1
      current_node=nodes_List[index_num]
    else:
      working_dir = working_dir + directory
      current_node=nodes_List[index_num]
    # print("found")
  
  else:
    print("cd: No such file or directory")






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
          print(sub_query)
          func_mkdir(sub_query)
        except:
          print("mkdir: Invalid syntax") 

      elif(a[0]=="touch"):
        try:
          file_name = str(a[1]).strip()
          func_touch(file_name)
        except:
          pass


      elif(a[0]=="tree"):
          root_node.print_tree()

  pass








if __name__ == '__main__':
    main() 