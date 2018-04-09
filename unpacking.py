def moyenne(a, b):
    print("array")
    return 0.5 * (a+b)

# def moyenne(note1=0, note2=0):
#     print("dictionary")
#     return 0.5 * (note1+note2)

if __name__ == '__main__':
    notes1 = [3, 8]
    notes2 = {'note1':4, 'note2':8}
    # La liste notes1 est depaquetee en arguments unitaires
    print(moyenne(*notes1))
    # Le dictionnaire notes2 est depaquete en arguments unitaires
    print(moyenne(**notes2))