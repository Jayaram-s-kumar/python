class parent1:
    demo1 = 0
    def parent1function(self):
        print("This is parent1",self.demo1)
    
class parent2:
    demo2 = 0
    def parent2function(self):
        print("This is parent2",self.demo2)

class child(parent1,parent2):
    i=5
    def childfunction(self):
        print("This is child")

child_instance = child()
child_instance.demo1 = 10
child_instance.demo2 = 20
child_instance.parent1function()
child_instance.parent2function()
child_instance.childfunction()
print(child_instance.i)
