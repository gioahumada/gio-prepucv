def medir_largos(a, *b):
    if b:
        largos = [len(a)]
        for i in b:
            largos.append(len(i))
        return largos
    return len(a)

def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas"))

if __name__ == "__main__":
    main()