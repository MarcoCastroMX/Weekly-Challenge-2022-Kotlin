"""
Reto #11
ELIMINANDO CARACTERES
Fecha publicación enunciado: 14/03/22
Fecha publicación resolución: 21/03/22
Dificultad: FÁCIL

Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
- out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
- out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

Información adicional:
- Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
- Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
- Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
- Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

def main():
    printNonCommon("brais","moure")
    printNonCommon("Me gusta Java","Me gusta Kotlin")
    printNonCommon("Usa el canal de nuestro discord (https://mouredev.com/discord) \"\uD83D\uDD01reto-semanal\" para preguntas, dudas o prestar ayuda a la comunidad",
        "Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.")

def printNonCommon(str1,str2):
    out1 = "out1: "
    out2 = "out2: "

    str1 = str1.encode("ascii", "ignore")
    str1 = str1.decode()

    str2 = str2.encode("ascii", "ignore")
    str2 = str2.decode()

    for char in str1.lower():
        if str2.find(char) == -1:
            out1 += char

    for char in str2.lower():
        if str1.find(char) == -1:
            out2 += char    
    
    print(out1)
    print(out2)


if __name__ == "__main__":
    main()
