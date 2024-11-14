from .generator import generate_license_plate
def main():
    memory_tag = input("Enter two letters excluding I, Q, Z: ")
    date = input("Enter date in dd/mm/yyyy format: ")
    license_plates= set()

    try:
        license_plate = generate_license_plate(memory_tag, date, license_plates)
        print(f"Your license plate is: {license_plate}")
    except RuntimeError as e:
        print(f"Abort: {e}")

# add error handling

if __name__ == "__main__":
    main()