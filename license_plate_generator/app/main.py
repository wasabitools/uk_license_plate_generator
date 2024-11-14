from exceptions import InvalidLicensePlateError
from generator import generate_license_plate

def main():
    memory_tag = input("Enter two letters excluding I, Q, Z: ")
    date = input("Enter date in dd/mm/yyyy format: ")
    license_plates= set()

    try:
        license_plate = generate_license_plate(memory_tag, date, license_plates)
        print(f"Your license plate is: {license_plate}")
    except InvalidLicensePlateError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()