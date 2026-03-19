# 2.. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animal:
    def show():
        print("This is an animal class")

class Pets(Animal):
    def show():
        print("This is a pets class ")

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dogs are barking")

dog = Dog()
dog.bark()