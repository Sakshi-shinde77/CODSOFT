def main():
    
    lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
    uppercase_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digit_chars = "0123456789"
    symbol_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    def get_random_number(seed, max_val):
        a = 1664525
        c = 1013904223
        m = 2**32
        
        new_seed = (a * seed + c) % m
        random_number = new_seed % max_val
        return random_number, new_seed

    seed = 12345
    
    while True:
        try:
            length_str = input("Enter desired password length (e.g., 8): ")
            length = int(length_str)
            
            if length <= 0:
                print("Password length must be a positive number.")
                continue

            include_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            include_digits = input("Include numbers? (yes/no): ").lower() == 'yes'
            include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

            char_pool = lowercase_chars
            if include_upper:
                char_pool += uppercase_chars
            if include_digits:
                char_pool += digit_chars
            if include_symbols:
                char_pool += symbol_chars
            
            if not char_pool:
                print("You must include at least one type of character.")
                continue

            password_list = []
            current_seed = seed
            for _ in range(length):
                index, current_seed = get_random_number(current_seed, len(char_pool))
                password_list.append(char_pool[index])
            
            password = "".join(password_list)
            print(f"Generated password: {password}")
            
            seed = current_seed

        except ValueError:
            print("Invalid input. Please enter a valid number for length.")
        
        again = input("Generate another password? (yes/no): ").lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    main()
