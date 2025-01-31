def info(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys} : {values}")
info(nombre="pedro", edad=19)