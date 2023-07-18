class Parent:
    i=10
    def parentfunction(self):
        print("I am parent ")

class child(Parent):
    i=5
    def childfuctnion(self):
        print("I am child")

child_instance = child()
parent_instance = Parent()

child_instance.childfuctnion()
child_instance.parentfunction()

parent_instance.parentfunction()