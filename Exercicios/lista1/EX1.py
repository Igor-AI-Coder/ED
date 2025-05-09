def menor (numero1, numero2, numero3):
        if numero1 < numero2 and numero1 < numero3:
            meno= numero1
            return meno
        if numero2 < numero1 and numero2 < numero3:
            meno = numero2
            return meno
        else:
            meno = numero3
            return meno
