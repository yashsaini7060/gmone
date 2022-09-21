dir_List = []
nodes_List = []
current_node=0
root_node=0
working_dir="/"
term="root:"
doll="$"
cd_count=0

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
      nodes_List= self.children
      # nodes_List= copy.deepcopy(self.children)

    def add_node(self, value):
      file = TreeNode(value)
      self.add_child(file)

    def mkdir_with_p(self,value):
      #print(value)
      substring = value.split('/')
      #print(substring)
      global current_node
      global root_node
      global dir_List
      for item in substring:
        if(item!=""):
          if name in dir_List:
            #cd
            pass
          else:
            name="/"+item
            new_node=TreeNode(name)
            current_node.add_child(new_node)
            current_node=new_node
      current_node=self

def parent_dir(value):
  #print(value)
  substring = value.split('/')
  #print(substring)
  global current_node
  global root_node
  # for item in substring:
  #       if(item!=""):
  #         new_node=TreeNode("/"+item)
  #         current_node.add_child(new_node)
  #         current_node=new_node
  # current_node=self


def main():

  #impoting global variables
  global working_dir 
  global term 
  global doll
  global root_node
  global dir_List
  global nodes_List
  global current_node
  global cd_count


  #initializing tree
  root = TreeNode("root/")
  current_node=root
  root_node=root
  a = True


  #while loop to be in gmone
  while(a):
    print(term+working_dir+doll, end=" ")
    query= input() 
    if(len(query) != 0):

      a = query.split(" ")

      if(a[0]== "exit"):
        a=False
        print("bye, root")

      elif(a[0] == "pwd"):
        print(working_dir)

      elif(a[0] == "cd"):
        current_node.dir_list()
        current_node.nodes_list()
        dir_List.pop(0)
        print(dir_List)
        print("Nodes List")
        print(nodes_List)
        try:
          input_val=a[1]
          dir_name = str(input_val).strip()
          directory_name = "/" + dir_name 
          if dir_name==".":
            del dir_List[:]

          elif dir_name=="/":
            term="root:"
            working_dir="/"
            current_node=root_node
            cd_count=0
            del dir_List[:]
            

          elif dir_name=="..":
            parent_dir(working_dir)
            del dir_List[:]

          elif "./" in dir_name:
            del dir_List[:]
          
          elif len(dir_name) >=1 and dir_name[0]=="/":
            if dir_name in dir_List:
              index_num = dir_List.index(dir_name)
              if cd_count==0:
                working_dir = working_dir + dir_name[1:]
                cd_count=cd_count+1
                current_node=nodes_List[index_num]
              else:
                working_dir = working_dir + dir_name[1:]
                current_node=nodes_List[index_num]
            del dir_List[:]

            

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
            del dir_List[:]

          elif dir_name in dir_List:
            print("cd: Destination is a file")
            del dir_List[:]

          else:
            print("cd: No such file or directory")
            del dir_List[:]

        except:
          print("cd: Invalid syntax") 

      elif(a[0]=="mkdir"):
          try:
            name = str(a[1]).strip()
            if name=="-p":
              try:
                name = str(a[2]).strip()
                if len(name) and name[len(name)-1] == "/":
                  f_name = "/" + name[:-1]
                  current_node.dir_list()
                  if f_name in dir_List:
                    pass
                  else:
                    current_node.add_node(f_name)
                  del dir_List[:]
                else:
                  f_name = "/" + name
                  current_node.dir_list()
                  if name in dir_List:
                    pass
                  if f_name in dir_List:
                    pass
                  else:
                    current_node.add_node(f_name)
                del dir_List[:] 
                pass
              except:
                pass
              pass
            else:
              current_node.dir_list()
              dir_List.pop(0)
              if len(name) and name[len(name)-1] == "/":
                f_name = "/" + name[:-1]
                if f_name in dir_List:
                  print("mkdir: File exists")
                else:
                  current_node.add_node(f_name)
                del dir_List[:]
              else:
                f_name = "/" + name
              # print("yash2")
                if name in dir_List:
                  print("mkdir: File exists")
                if f_name in dir_List:
                  print("mkdir: File exists")
                else:
                  current_node.add_node(f_name)
                del dir_List[:] 
          except:
            pass

      elif(a[0]=="touch"):
        if(working_dir=="/"):
          touch = TreeNode(a[1])
          root.add_child(touch)
      
    else:
      print(term) 
  root.print_tree()
    

  
      


if __name__ == '__main__':
    main() 