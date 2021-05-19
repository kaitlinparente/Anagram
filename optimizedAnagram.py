import time
import sys



def sortedDictAnagram(filepath):
    print("\n")
    print("Welcome to Kaitlin Parente's anagram checker")
    print("Enter a word you would like to find anagrams for. ")
    print("If you would like to stop searching for anagrams, please type 'exit'.")
    print("----------------------------------------------------------------------")
    
    start = time.time() #timer for dictionary sort and load
    orderedDict = {} #initializing the dictionary to be sorted by word len
    
    file = open(filepath)
    file_contents = file.read()
    dictList = file_contents.splitlines()

    for word in dictList: 
        word=word.lower()
        if len(word) not in orderedDict: 
            orderedDict[len(word)]=[]
        orderedDict[len(word)].append(word)
    end = time.time() #timer for dictionary sort and load
    print("Dictionary loaded and sorted in " + str(float((end-start)*1000)) + "ms.")
    print("\n")
    
    anagram = input("Please enter a word to check for anagams: ")

    while anagram != "exit":
        start = time.time() #timer for anagram search starts
        anagramList =[] #empty list initialized/reset for anagrams to be appended to
        checkerList = orderedDict[len(anagram)] #grabbing only words with same len as inputted word
        
        for word in checkerList: 
            if sorted(anagram)==sorted(word) and anagram!=word: #removing the word itself to prevent false positives of one anagram just being the inputted word itself
                anagramList.append(word) #sorted(word) runs in nlogn time and sorts letters in word in alphabetical order
        
        if not anagramList: #if anagramList is empty then no anagrams present
            end = time.time() #timer for anagram search ends
            print("\n")
            print("There are no anagrams for the word '" + anagram +"'.")
            print("No anagrams found for '" +anagram +"'. Processed in " + str(float((end-start)*1000)) + "ms.")
        else: 
            end = time.time() #timer for anagram search ends
            print("\n")
            print("The " + str(len(anagramList))+" anagram(s) for the word '" + anagram+"' are: ")
            print(anagramList)
            print(str(len(anagramList)) + " anagrams found in " + str(float((end-start)*1000)) + "ms.")
        print("\n")
        print("----------------------------------------------------------------------")
        print("\n")
        
        anagram = input("Please enter a word to check for anagams: ")
        


#sortedDictAnagram("dictionary.txt")


        
def main(): 
    filepath = sys.argv[1]
    sortedDictAnagram(filepath)
main()