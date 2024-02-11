#!/usr/bin/python3
"""HBnB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def parse(arg):
    curly = re.search("\{(.*?)\}", arg)
    bracket = re.search("\[(.*?)\]", arg)

    if curly is None:
        if bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bracket.start()])
            retl = [i.strip(",") for i in lexer]
            retl.append(braket.group())
            return retl
    else:
        lexer = split(arg[:curly.start()])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """Defines HBNB command interpreter"""

    prompt = "(hbnb)"
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"}

    def emptyline(self):
        """Do nothing"""
        pass

    def do_quit(self, arg):
        """Quit comand"""
        return True

    def do_EOF(self, arg):
        """End of file"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        A = parse(arg)
        if len(A) == 0:
            print("** class name missing **")
        elif A[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(A[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        A = parse(arg)
        dict_1 = storage.all()
        if len(A) == 0:
            print("** class name missing **")
        elif A[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(A) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(A[0], A[1]) not in dict_1:
            print("** no instance found **")
        else:
            print(dict_1["{}.{}".format(A[0], A[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        A = parse(arg)
        dict_1 = storage.all()
        if len(A) == 0:
            print("** class name missing **")
        elif A[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(A) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(A[0], A[1]) not in dict_1.keys():
            print("** no instance found **")
        else:
            del dict_1["{}.{}".format(A[0], A[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        A = parse(arg)
        if len(A) > 0 and A[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            B = []
            for obj in storage.all().values():
                if len(A) > 0 and A[0] == obj.__class__.__name__:
                    B.append(obj.__str__())
                elif len(A) == 0:
                    B.append(obj.__str__())
            print(B)

    def do_count(self, arg):
        """counts the instances of a class"""
        A = parse(arg)
        c = 0
        for i in storage.all().values():
            if A[0] == i.__class__.__name__:
                c += 1
        print(c)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id"""
        A = parse(arg)
        dict_1 = storage.all()
        if len(A) == 0:
            print("** class name missing **")
            return False
        if A[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(A) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(A[0], A[1]) not in dict_1.keys():
            print("** no instance found **")
            return False
        if len(A) == 2:
            print("** attribute name missing **")
            return False
        if len(A) == 3:
            try:
                type(eval(A[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(A) == 4:
            obj = dict_1["{}.{}".format(A[0], A[1])]
            if A[2] in obj.__class__.__dict__.keys():
                vtype = type(obj.__class.__dict__[A[2]])
                obj.__dict__[A[2]] = vtype(A[3])
            else:
                obj.__dict__[A[2]] = A[3]
        elif type(eval(A[3])) == dict:
            obj = dict_1["{}.{}".format(A[0], A[1])]
            for key, value in eval(A[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    vtype = type(obj.__class.__dict__[key])
                    obj.__dict__[key] = vtype(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def default(self, arg):
        """defines class.method() synthaxe"""
        List = arg.split('.')
        class_n = List[0]
        cmd = List[1].split('(')
        mthd = cmd[0]
        dictionary = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count}
        if mthd in dictionary.keys():
            return dictionary[mthd]("{} {}".format(class_n, ""))
        return False

if __name__ == '__main__':
        HBNBCommand().cmdloop()
