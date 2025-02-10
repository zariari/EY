import re, openai, os
openai.api_key = os.getenv("OPENAI_API_KEY", "")

def menu():
    print("\nBienvenido al Asistente IA ")
    print("Seleccione una opción:")
    print("1. Cálculos matemáticos")
    print("2. Manipulación de texto (Contar palabras, Mayúsculas, Minúsculas)")
    print("3. Preguntas con IA")
    print("4. Salir")

def calcular():
    print("\nCálculo Matemático")
    print("Ingrese una operación matemática o escriba 'salir' para volver al menú.")

    while True:
        expr = input("Operación: ").strip()
        if expr.lower() == "salir":
            return  
        
        if not re.fullmatch(r"[0-9+\-*/().\s]+", expr):
            print("Error: Operación inválida. Solo se permiten números y operadores (+, -, *, /).")
            continue

        try:
            result = eval(expr)
            print("Resultado:", result)
        except Exception as e:
            print(f"Error: {e}")
            
def texto():
    print("\nManipulación de Texto")
    txt = input("Ingrese el texto: ").strip()

    print("\nElija una opción:")
    print("1. Contar palabras")
    print("2. Convertir a MAYÚSCULAS")
    print("3. Convertir a minúsculas")
    print("4. Volver al menú")

    while True:
        opc = input("Opción: ").strip()

        if opc == "1":
            print("Número de palabras:", len(txt.split()))
        elif opc == "2":
            print("Texto en MAYÚSCULAS:", txt.upper())
        elif opc == "3":
            print("Texto en minúsculas:", txt.lower())
        elif opc == "4":
            return 
        else:
            print("Opción inválida, por favor elija 1, 2, 3 o 4.")

def pregunta():
    print("\nPregunta a la IA")
    print("Escriba su pregunta o escriba 'salir' para volver al menú.")

    while True:
        q = input("Pregunta: ").strip()
        if q.lower() == "salir":
            return 
        
        try:
            client = openai.OpenAI(api_key=openai.api_key)
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": q}]
            )
            print("Respuesta:", response.choices[0].message.content)
        except openai.RateLimitError:
            print("Error #1")
            return
        except openai.AuthenticationError:
            print("Error #2")
            return 
        except Exception as e:
            print(f"Error: {e}")
        
def main():
    while True:
        menu()
        opc = input("Opción: ").strip()

        if opc == "1":
            calcular()
        elif opc == "2":
            texto()
        elif opc == "3":
            pregunta()
        elif opc == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()
