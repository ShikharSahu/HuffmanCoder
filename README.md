# Huffman Encoder

## usage :
```
stringToBeEncoded = 'sample string aaaa eeee sample sample'
test = HuffmanCoder(stringToBeEncoded)
print()
test.printEncodedString()
print()
test.printFrequencyCountOfInput()
print()
test.printMappingTableAsciiToHuffman()
print()
test.bitsUsedByBothMethods()
print()
```

## methods :
```
Note: pass only a string to the constructor!!
1. 
# used to print the attributes in a formatted manner
printMappingTableAsciiToHuffman():
printFrequencyCountOfInput():
printEncodedString():
bitsUsedByBothMethods():

2.
# encodes the String passed by the user and returns it,
# does NOT store it, except the encoded string passed in the constructor 
encode(ipString :str):

3.
# user can provide a string consisting of 0 and 1 and get it decoded to ASCII
decode(ipString : str):

4.
# get the dictionary which has the mapping from ASCII character to its encoded bit string
getMappedTableAsciiToHuffman():

5.
# get the dictionary which has the mapping from ASCII character to its number of occurences
getFrequencyCountOfInput():

6.
# returns the orignal string passed as an input
getInputString():

7.
# returns the orignal string encoded to huffman
getEncodedString():
```
