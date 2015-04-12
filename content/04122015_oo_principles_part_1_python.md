Title: Object Oriented Principles Part 1: Python
Date: 2015-04-12
Tags: computer language, Python, java, object oriented
slug: oo_principles_Python
Summary: What I learned about Python from learning Java

For my latest assignment at work, I needed to learn Java, which seemed a little daunting at first. As I was going through tutorials, I was presented with a lot of Object Oriented concepts I had not come into contact with before. I knew what objects and classes were, and was familiar with the idea of inheritance. But other concepts, like interfaces, constructors, and polymorphism, were new ideas, or at least new vocabulary.

I decided to go back and learn about the basics of OO Programming, and to investigate how some of these concepts are applied in Python and Javascript. This is part 1 of 2, exploring OO Programming and Python.

It may be helpful to check out one of the resources below if you're rusty on or totally unfamiliar with OO programming. I won't go into the more common concepts in as much depth.

For reference, I'm using Python 2.7. Some of these details might be different for Python 3.

###Class
A class is the blueprint for an object. It tells what attributes (variables/data) and methods (functions) an object should have. The basic syntax is:
```python
class className(parentObject)
```

Pretty simple. Let's see an example:
```python
class DothrakiMan(object):
	def __init__(self, name, hairLength):
		self.name = name
		## Units are inches, because Dothraki don't use the metric system either
		self.hairLength = hairLength

	def cutHair():
		hairLength = 0		
```

Here we have a class to create a `DothrakiMan`. We've included the attributes of a `name`, and his `hairLength`. He can cut his hair and, well that's it for now.

###Object
An object is an *instance* of a class. In other words, an object is the thing you create with a class. Let's see an example.
```python
Drogo = DothrakiMan('Khal Drogo', 48)		
```
Now we have the **object** `Drogo`, made from the **class** `DothrakiMan`. You can make as many objects as you want from that one class.

Now that the bare basics are out of the way, let's talk about some more interesting topics.

###Encapsulation
There are two components to encapsulation.

1. Grouping data and functions into a single, logical group.
2. Protecting those data and methods/preventing unauthorized access, aka "data hiding".

In defining the term, some sources use just one component, some use both. Whatever the case, encapsulation is most often acheived through the use of classes (there are exceptions, which we'll see with Javascript). The whole purpose of a class is to group data and functionality into a convenient package.

Python really only uses the first component. Data hiding is kind of possible, but not fully.

A little background: in Java, when creating data or methods, you include the keyword `public`, `private`, or `protected`. Those define whether or not you can directly access an item from the object created from a given class. If we pretend we created our class `DothrakiMan` and object `Drogo` in Java, and set the `name` attribute as private, trying `Drogo.name` would fail.

Here's an example of the different methods of data hiding in Python:

```python
class EncapsulationClass(object):
    def __init__(self, pub, semi, prv):
        self.public = pub
        self._semiPrivate = semi
        self.__private = prv

encapsulateObject = EncapsulationClass()
```
In our `EncapsulationCLass` class, we have three different attributes. The first one, `self.public`, we have seen before. You can access it directly on an object like `encapsulateObject.public`.

In the second attribute, `self._semiPrivate`, the underscore at the beginning of the name denotes that this attribute should be regarded as private. It's letting others know they shouldn't access it directly. However, there is no enforced protection. `encapsulateObject._semiPrivate` would run without error, and return the value of the attribute.

The last attribute has two _ at the beginning, and does provide a little extra protection through "name mangling." If you were to try to run `encapsulateObject.__private`, you would get the error below:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'EncapsulationClass' object has no attribute '__private'
```

But if you ran `encapsulateObject._EncapsulationClass__private`, blamo, you have access to the attribute. So by using `objectName._className__privateAttributeName` you can access those so called private attributes and methods.


###Constructor
A constructor is a special method that's called when an object is *created*. It's where you pass in and set any data you want the object to have. In the example above, with `DothrakiMan`, it looks like we're passing in and setting the attributes of the object with `__init__`. So `__init__` must be the constructor!

Actually, no. `__init__` is technically an initializer. The method `__new__` gets called first, and it is what creates the new instance, a.k.a. a new object. After the new object has been created, `__init__` sets the data on the object. The article [__new__() in Python](http://agiliq.com/blog/2012/06/__new__-Python/) gives a good, in depth explanation, better than I'm able to.

If this seems confusing, and you don't really get exactly what that means, that's ok. To be honest, I don't 100% understand the nuances, at least not in any practical sense. More importantly, you don't really need to know this to write a Python program. Odds are you're not going to need to touch `__new__`, so unless you have a specific reason to muck with it, don't worry about it. 


###Inheritance
Inheritance is the process of one class, the "child", taking on the attributes and methods of another class, the "parent". It's often referred to an "Is-A" relationship. For instance, a `Cat` is a(n) `Animal`, and a `Car` is a `Vehicle`. The syntax is super simple:

```python
class ChildClass(ParentClass)
```

You can redefine methods in the child class that exist in the parent class if you want different behavior. You can also add classes and attributes to the child class that don't exist in the parent class.

Python supports multiple inheritance, meaning a child class can have multiple parents. Syntax is similarly straightforward:

```python
class ChildClass(ParentClass1, ParentClass2, ParentClass3)
```

Multiple inheritance can be pretty tricky in terms of maintaing your code. [Learn Python the Hard Way, lesson 44](http://learnPythonthehardway.org/book/ex44.html) has a good explanation of how to implement inheritance, as well as pitfalls to watch out for.

Abstract Base Classes (ABC) are an interesting part of inheritance. An ABC only exists to be inherited from, you can't create an instance of it. The concept exists for cases when you need a parent class that groups together most functionality, but you would never want an object created from that class. Using our example of `DothrakiMan` from above, we might want to create a `DothrakiPerson` parent class which contains some basic information that would apply to a man, woman, or child.

```python
class DothrakiPerson(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age		
```

Right now anyone could make a `DothrakiPerson` object. To change this to an ABC in Python, you use the `abc` module (and you know what that stands for now). 

```python
from abc import ABCMeta, abstractmethod

class DothrakiPerson(object):
	__metaclass__ = ABCMeta

	def __init__(self, name, age):
		self.name = name
		self.age = age

@abstractmethod
def person_type(self):
	pass
``` 

There are two things going on here:
1. At the beginning, set `__metaclass__` = ABCMeta`
2. Add `@abstractmethod` decorator to a method, here `person_type`, to turn that into a *virtual* method. A virtual method is one which must exist on the child class, but which the parent may not implement.

An alternative way to create a virtual method is
```python
def person_type(self):
	raise NotImplementedError("You need to implement the person_type method")
```

Note that if you don't include the `@abstractmethod` decorator on any methods, you will still be allowed to create an instance of the ABC class, `DothrakiPerson`. 



###Interfaces
In other object oriented languages, like Java, you are always tied to the type of a thing. Is it a string, an integer, a DothrakiMan? When creating a function/method, all the inputs have their types declared, and you won't be able to even attempt execution if you pass something of a different type.

The purpose of all this type checking is that you know exactly what attributes and methods you have available, and thus what actions you can take on/with your objects. You can write your code knowing what you can access, even if not the specifics (you know that any `DothrakiMan` will have a `name` attribute, though you won't know that name until an instance of `DothrakiMan` has been created).

Interfaces are a way of adding flexibility. They are nothing more than a list of empty methods that any class that uses ("implements") that interface must define. So you could have 10 very different classes all implementing the same interface. In addition, a class can implement multiple interfaces.

Their utility comes from being able to check for, and base actions off of, this interface rather than a type. Let's say you have a function that takes an object as input. You want to call the `ride()` method on that input object. That could be a horse, a bike, a ferris wheel, and more. In some cases you can have a parent class everything inherits from, and you can check for that parent relationship, as any methods available in the parent is also in the child. Since it isn't likely, in this example, that there's a logical parent class, you would need to create a different function for each different type of input you want. If instead these disparate objects all had classes that implemented some interface with a `ride` method, you no longer need different functions! You just have one function which checks for that interface.

Ok ok, get to the Python. Well, that was a lot of explanation just to tell you there are no interfaces in Python, at least not formally. ABC's and their virtual classes are the closest approximation Python has.

So why doesn't Python have interfaces? You don't need them! Python is a 'duck-typed' language. That means it's so easy, a duck could do it. Wait, no, that's a lie. It comes from the concept of the "duck test" - if you've got an animal that walks like a duck, swims like a duck, quacks like a duck, it must be a duck. Wikipedia sums it up nicely:

>[I]n duck typing, an object's suitability is determined by the presence of certain methods and properties (with appropriate meaning), rather than the actual type of the object.
> - [Wikipedia](http://en.wikipedia.org/wiki/Duck_typing)

You can check the type of an object and base action off of that, but it's usually a bad idea. If nothing else, that indicates a possible flaw in your class design - any functionality tied directly to the type of an object should usually be a part of that object (there are always exceptions though). Instead you can use the `hasattr` or `getattr` methods to check for presence of an attribute or method.

###Composition
Composition, in contrast to inheritance, is a "Has-A" relationship. It represents a relationship between classes that doesn't depend on a parent/child relationship. For instance, a `Cat` has a `Tail`, or a `Dothraki` has a `Horse`. Composition works by creating an instance (an object) of one class in another class.

```python
class Horse(object):
	
	def run():
		pass

class DothrakiMan(object):

	def __init__(self, hairLength):
		self.hairLength = hairLength
		self.horse = Horse()	
```

Now every time you create a new `DothrakiMan`, he will have a `Horse`. But what about those attributes we put in `DothrakiPerson`? We haven't said to inherit from that class, so we don't have a `name` or `age` on our objects. You can accomplish the same thing with composition:

```python
class Horse(object):
	pass

class DothrakiPerson(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		return self.name

class DothrakiMan(object):

	def __init__(self, name, age, hairLength):
		self.dothrakiPerson = DothrakiPerson(name, age)
		self.hairLength = hairLength
		self.horse = Horse()

	def getName(self):
		return self.dothrakiPerson.getName()
```

Whaaat. Yup. You can create a new `DothrakiPerson` instance, and just use that instance's attributes and methods. Make sure your parent class isn't an ABC or this won't work.

Using composition over inheritance is preferred in OO Programming. There aren't hard and fast rules for when to use what. Zed Shaw has a good, brief list in [Learn Python the Hard Way](http://learnPythonthehardway.org/book/ex44.html#composition).

###Polymorphism
This concept really confused me the first time I heard it defined. And the second. And probably a few more times after that. My best crack at defining it is that polymorphism refers to

1. The ability of a piece of code, given an input, to execute on that input as long as it has the required methods and attributes.
2. The fact that the specific behavior of an attribute or method may differ between classes.

An example of each. For item 1:
```python
def polyFunction(a,b)
	return a+b
```

Here, we could input strings, integers, lists, any 2 items with the `__add__` method.

And for item 2:
```python
class Person(object):
	def sayHello(self):
		pass

class AmericanPerson(Person):
	def sayHello(self):
		print 'Hello'

class FrenchPerson(Person):
	def sayHello(self):
		print 'Bonjour'
```

Both an `AmericanPerson` and a `FrenchPerson` have a `sayHello` method, but the output is different for each. If you were writing code that calls the `sayHello` method, you could pass in either.

###Conclusion
Phew, that was a lot. I encourage you to explore the resources listed below to get more information and clarification. I hope I haven't led anyone astray or caused any confusion.

If you see any errors, factual, grammatical, whatever else, please feel free to submit it as an issue on the repository [issues page](https://github.com/srthurman/selectstarfromlanguages/issues) on github.

**Resources**:

- [Jeff Knupp - Python Classes and OO Programming](http://www.jeffknupp.com/blog/2014/06/18/improve-your-Python-Python-classes-and-object-oriented-programming/)
- [Learn Python the Hard Way - Lessons 40-44](http://learnPythonthehardway.org/book/index.html)
- [Lynda.com - Object-Oriented Design](http://www.lynda.com/Programming-tutorials/Foundations-of-Programming-Object-Oriented-Design/96949-2.html)
- [Python-course.eu - Object Oriented Python](http://www.Python-course.eu/object_oriented_programming.php)
- [Good Morning, Polymorphism](http://lgiordani.com/blog/2014/08/21/python-3-oop-part-4-polymorphism/#.VSrjKOnd_IE)
- [\_\_new\_\_() in Python](http://agiliq.com/blog/2012/06/__new__-Python/)