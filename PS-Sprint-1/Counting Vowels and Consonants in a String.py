# Write a program to count vowels and consonants in a given string.

# Function Definition
def Count_vowel_Consonents(input_String):

    #Defining Vowels
    Vowels = "aeiouAEIOU"

    # Initialize Counters
    Vowels_Count = 0
    Consonent_Count = 0 

    # Loop Through the String
    for char in input_String:
        #Check if the Character is Alphabetic
        if char.isalpha():
            # Check if the Character is a Vowel
            if char in Vowels:
                Vowels_Count += 1 
            # Otherwise, Count as a Consonant
            else:
                Consonent_Count += 1 
    return Vowels_Count, Consonent_Count


user_input = input("Enter a String : ")
Vowels, Consonent =  Count_vowel_Consonents(user_input)

# Display the result 
print(f"The no of Vowels : {Vowels}")
print(f"The no of Consonent : {Consonent}")



