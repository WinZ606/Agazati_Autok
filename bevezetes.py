def automarka():
    print("I/A:")
    neve = str(input("  Autó neve: "))
    datum = int(input(" Gyártási dátuma: "))
    print("I/B:")
    if (datum == 2024):
        print(f"Ez az {neve} friss gyártás")
    elif (datum < 2000):
        print(f"Ez az {neve} öreg autó")
    else:
        print(f"Ez az {neve} átlagos korú")