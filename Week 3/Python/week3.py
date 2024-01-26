# Rule of thumb : Space complexity is the data structure used but not the data strucutre input
#n -> number of words in the list
#m -> avg length of each word
#cont = [0] * 26 

def groupAnagrams(A):
    dictionary = {} #This is used to store the sorted word as key and the list of words as value
    for word in A:
        sortedWord = "".join(sorted(word)) #This is used to sort the word
        if sortedWord not in dictionary: #Check if the sorted word is in the dictionary
            dictionary[sortedWord] = [word] #If not, add the sorted word as key and the word as value
        else: 
            dictionary[sortedWord].append(word) #add the word to the list of words if the sorted word is already in the dictionary
    return list(dictionary.values())


#Simulation
#n = 6 this is the number of words in the list
#m = 3 this is the avg length of each word
#dictionary = {}
#word = "eat" -> sortedWord = "aet"
#sortedWord = "aet"
#dictionary = {"aet": ["eat"]}
#word = "tea" -> sortedWord = "aet"
#sortedWord = "aet"
#dictionary = {"aet": ["eat", "tea"]}
#word = "tan" -> sortedWord = "ant"
#sortedWord = "ant" -> sortedWord not in dictionary
#dictionary = {"aet": ["eat", "tea"], "ant": ["tan"]}



A = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(A))
#output = 
# [["ate","eat","tea"],["nat","tan"],["bat"]]
# Time complexity: O(n*m*log(m)) -> n is the number of words in the list and m is the avg length of each word
# Space complexity: O(n*m) -> n is the number of words in the list and m is the avg length of each word