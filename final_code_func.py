dir_List = []
current_node = 0
root_node = 0
working_dir="/"
term="root:/"
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

    def add_node(self, value):
      file = TreeNode(value)
      self.add_child(file)

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




def main():
  #global variables
  global working_dir 
  global term 
  global doll
  global root_node
  global dir_List
  global current_node

  #Creating first node of root
  root = TreeNode("root/")
  current_node=root
  root_node = root

  a = True
  while(a):

    print(term+doll, end=" ")
    query= input() 

    #if else ladder for queries
    if(len(query) != 0):

      a = query.split(" ")

      if(a[0]== "exit"):
        a=False
        print("bye, root")

      elif(a[0] == "pwd"):
        print(working_dir)

      elif(a[0]=="touch"):
        try:
          name = str(a[1]).strip()
          current_node.add_node(name)
        except:
          pass

  pass








if __name__ == '__main__':
    main() 