# Have it start with the encrypted message. Make a dictionary, and go through the encrypted msg and for every three consecutive characters,  make an entry in to the dictionary that has a list as it's value. Put the start index of those three characters into the list. If those 3 characters occur again, append the new index to the list. 
# dict["abcd"].append(12)
import string
import math
from statistics import mode
encrypted_message = input("Enter the message you'd like to decrypt: ").lower()

# encrypted_message = "elqguzievnofqsaelqfrqsdofwszundezmbyiochwhdszpqnsetrropemfkndhutstggzgqsdoajszsgzgaarftiwgsepogpxtslseptvcwfocaimfromfvnowqszphfvrjhmzjlceprprfvrcimbqjifhupcesrxipgbzyfcsapmqrhlkbbmspmulhdszzzqrgsiykndecirdxucaelmhulhnsryeeyroxuarlrpotlmzpheatwypxtsllpxhuzysvgtxzcozhkvnoihseqsgbqelqsapvsmgzeohhlpxmqzmfgbelqguziefrxeubroszhupwfscdsghbqtxoppmzcapwqbfpfghcpvrspepkbbcqmzvyezcgsidofdlqgneamhpsmzugsiicewhscojwaarelubtneguuelqfrjiuhjlwzhfzqgqutxeqbwsdcedlmdrmyfhupammveamgzzzubtdlqgdfmzhroxagrpmrgupgaiyofqhgpvgbqpvehnyhivnemfkndezrjsidsveamgtzmzuofxuhqthzhuppbofdlqqbyxubhphfcfeedsvyxahuphugglrosfsipwqyxgbqpvehnyhivlelughyimgvyiegjlwnivwhubttrewqplqfozhkgupjqzgwmwsfsievbfppureyboaovgbvqszzldlqqbfppanviaighlmhveamgnextogxsysaewtspzqbfrsizrroatogtxioflrpkupvqwgheevrlhubtlrpgupozsjsidzvqi"

# Removing all non-alphabetical characters.
for i in encrypted_message:
  if i not in string.ascii_letters:
    encrypted_message.replace(i, "")

# Creating variables for sequencing
length = 3
lower_limit = 0
letter_sequences = {}
done = False

# Counting the occurences of each sequence of 3 letters, and adding it to a dictionary.
while not done:
  sequence = encrypted_message[lower_limit:lower_limit + length]
  if sequence in letter_sequences:
    letter_sequences[sequence].append(lower_limit)
  else:
    letter_sequences[sequence] = [lower_limit]
  lower_limit += 1
  if lower_limit + length == len(encrypted_message):
   done = True


#https://stackoverflow.com/questions/57524979/how-to-find-the-common-factors-of-2-numbers
def gcf(numbers):
     current_gcf = math.gcd(numbers[0], numbers[1])
     for i in range(2, len(numbers)):
        current_gcf = math.gcd(current_gcf, numbers[i])
     return current_gcf

# print(gcf([6, 42, 27, 9, 48, 66]))

diff_list = []

# Gettting the differences of indexes of each multi-occuring sequence. 
for seq, position_list in letter_sequences.items():
  if len(position_list) > 1:
    #https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
    position_diff = [position_list[i+1] - position_list[i] for i in range(len(position_list)-1)]
    # Using the lists of differences to find the key length through gcf.
    if len(position_diff) > 1:
      diff_list.append(gcf(position_diff))
    
key_length = mode(diff_list)

empty_list = []
empty_string = ""
key_length = 5
for j in range(0, key_length):
  for i in range(j, len(encrypted_message), key_length):
    empty_string = empty_string + encrypted_message[i]
  empty_list.append(empty_string)
  empty_string = ""


def letter_frequency(string):
  occurences = {}
  if string == "":
      print("There are no letters.")
  else:
   while string != "":
     # Counting letter occurences and storing them in the counter variable, and adding it to the dictionary.
      counter = string.count(string[0])
      occurences[string[0]] = counter
        # Removing all occurrences of that letter from the string.
      string = string.replace(string[0], "")
  return occurences

letter_ranks = {}
for i in string.ascii_lowercase:
  letter_ranks[i] = string.ascii_lowercase.index(i)

recovered_key = ""
for i in range(0, len(empty_list)):
  occurences = letter_frequency(empty_list[i])
  #print(occurences)
  max_letter = max(occurences, key = occurences.get)
  #print(max_letter)
  new_char = (letter_ranks[max_letter] - 4) % 26
  for j in letter_ranks:
    if new_char == letter_ranks[j]:
      recovered_key = recovered_key + j

print(recovered_key)

# Making it so that the key is the same length as the text (wraps around if it's too short).
while len(encrypted_message) > len(recovered_key):
  for i in range(0, len(recovered_key)):
    recovered_key += recovered_key[i]
    if len(recovered_key) == len(encrypted_message):
      break
   
for i in range(0, len(encrypted_message)):  
  new_char = (letter_ranks[encrypted_message[i]] - letter_ranks[recovered_key[i]]) % 26
  for j in letter_ranks:
    if new_char == letter_ranks[j]:
        print(j, end="")


