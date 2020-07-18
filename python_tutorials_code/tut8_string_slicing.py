# String Slicing
str = "hello is sky is my way"
print(str)
print(len(str))
print(str.capitalize())
print(str.lower())
print(str.count("is"))
print("in string :"f'{str.count("is")}')
print(str.find("my"))
print(str.isalnum())
print(str.upper())
print(str.replace("is", "are"))
print(str.index("sky"))
print(str.endswith("way"))
print("---------------------------------------------")
# In string slicing we sometimes give skip value also i.e. string[n:m:skip_value].
# By default the skip value is 1 but if we want to choose alternate characters of
# a string then we can give it as 2.
# print(str[::-1])  #in this statement string are reverse
print(str[::2])  # in this statement string 1 skip character
