from name_function import get_formateed_name

print("Enter 'q' at any time to quit")
while True:
    first = input("\nPlease give me a first name")
    if first == 'q':
        break
    last = input("\nplease give me a last name")
    if last == 'q':
        break

    formatted_name = get_formateed_name(first,last)
    print("\tNeatly formatted name:" + formatted_name+ '.')
    
