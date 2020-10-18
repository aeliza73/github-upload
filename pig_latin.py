print("Enter a sentence to be translated into Pig Latin\n")
text = input()
print("\nInput text is: ", text)
text_list = text.split()
pl_text_list = [x[1:]+x[0]+"ay" if x.isnumeric()==False else x for x in text_list]
print("\nTranslation: ", *(pl_text_list))
