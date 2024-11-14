from .validators import validate_memory_tag, validate_date
def main():
    memory_tag = input("Enter two letters excluding I, Q, Z: ")
    date = input("Enter date in dd/mm/yyyy format: ")

    try:
        if not validate_memory_tag(memory_tag):
            print("Wrong memory tag provided")
        if not validate_date(date):
            print("Wrong date provided")
    except RuntimeError as e:
        print(f"abort: {e}")

# add generator function (+50, suffix, concat parts)
# add error handling

if __name__ == "__main__":
    main()