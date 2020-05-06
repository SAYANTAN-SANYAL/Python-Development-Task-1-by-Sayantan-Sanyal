# To accept a string from user
# and to display only the characters present at even index number
string_input=input("Enter a string: ")
string_output=""
print("The string with even index characters is: ")
for i in range(len(string_input)):
    if(i%2==0):
        string_output=string_output+string_input[i]
print(string_output)