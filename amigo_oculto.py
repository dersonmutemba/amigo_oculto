import os
import random

names = []
name = input("Insira um nome: ")
while name.strip() != "":
    names.append(name)
    name = input("Insira um nome: ")

selectorsnames = names.copy()
availablenames = names.copy()
while len(names) > 0:
    print(selectorsnames)
    person = input("Insira o seu nome: ")
    while person not in selectorsnames:
        person = input("Nome não está na lista. Insira o seu nome: ")
    if person in availablenames:
        availablenames.remove(person)
    selectedperson = availablenames[random.randint(0, len(availablenames) - 1)]
    print("Terá que presentear a " + selectedperson)
    names.remove(selectedperson)
    availablenames.append(person)
    availablenames.remove(selectedperson)
    selectorsnames.remove(person)
    input("Pressione Enter para continuar")
    os.system('clear')