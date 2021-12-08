from TreeNode import Node

# @author: Shikhar Sahu 

class HuffmanCoder: 

    # stringToBeEncoded: a string for which recursive tree is to be created is passed
    def __init__(self, stringToBeEncoded : str):
        assert isinstance(stringToBeEncoded, str)
        self.__inputString = stringToBeEncoded
        self.__frequencyMap = self.__getFrequencyMap()
        self.__root = self.__createHuffmanTree()
        self.__mappingTable = self.__createMapping()
        self.__encodedString = self.encode(self.__inputString)

    # private function that creates the huffman tree with the input String and frequency map
    # and returns its root
    def __createHuffmanTree(self):   
        treeList = []
        for ele in self.__frequencyMap:
            treeList.append(Node(ele,self.__frequencyMap[ele]))
            
        while len( treeList )>1:
            treeList.sort(key = lambda x : x.freq)
            n1 = treeList.pop(0)
            n2 = treeList.pop(0)
            nn = Node("internal", n1.freq + n2.freq)
            nn.left = n1
            nn.right = n2
            treeList.append(nn)
        return treeList[0]

    # creates a mapping of the normal ASCII character to its respective encoded bit String
    def __createMapping(self):
        table = {}
        os = ""
        self.__createMappedTableHelper(self.__root,table, os)
        return table

    # recursive helper called by createMapping
    def __createMappedTableHelper(self, root, table, os):
        if root == None:
            return 
        if root.left == None and root.right == None:
            table[root.ch] = os
        self.__createMappedTableHelper( root.left, table , os + "0")
        self.__createMappedTableHelper( root.right, table , os + "1")

    # recursive helper function called by decode
    def __decodeHelper(self, ipStr, root, ind, outputString):
        if root.left == None and root.right == None:
            outputString += root.ch
            return int (ind), outputString

        if ind >= len(ipStr):
            return int(-1), outputString
       
        if(ipStr[ind] == '0' ):
            return self.__decode(ipStr, root.left , ind+1, outputString)
        else:
            return self.__decode(ipStr, root.right, ind+1, outputString)
        
    # takes the the input String and returns the frequency map of 
    # each character of the String with their respective frequency of occurrence
    def __getFrequencyMap(self):
        frequencyMap = {}
        for i in self.__inputString:
            if i in frequencyMap:
                frequencyMap[i] += 1
            else:
                frequencyMap[i] = 1
        return frequencyMap

    def printMappingTableAsciiToHuffman(self):
        print("char\t code")
        for ele in sorted(self.__mappingTable):
            print(ele,"\t",self.__mappingTable[ele])

    def printFrequencyCountOfInput(self):
        print("char\t frequency")
        for ele in sorted(self.__frequencyMap):
            print(ele,"\t",self.__frequencyMap[ele])

    def printEncodedString(self):
        print('The string encoded to Huffman is: ' + self.__encodedString)

    # prints information about the bits used by both the ASCII encoding and the Huffman encoding
    def bitsUsedByBothMethods(self):
        bitsByASCII = len(self.__inputString)*7
        bitsByHuffman = len(self.__encodedString)
        print('bits used by ASCII: '+str(bitsByASCII ))
        print('bits used by Huffman Coding: '+ str (bitsByHuffman ))
        print()
        self.printEncodedString()

    # encodes the String passed by the user and returns it,
    # does NOT store it, except the encoded string passed in the constructor 
    def encode(self, ipString :str):
        assert isinstance(ipString, str)
        outputString = ""
        for ch in self.__inputString:
            outputString += self.__mappingTable[ch]
        return outputString

    # user can provide a string consisting of 0 and 1 and get it decoded to ASCII
    def decode(self, ipString : str):
        assert isinstance(ipString, str)
        ind = int (0)
        outputString = ""
        while(True):
            ind, outputString = self.__decodeHelper(ipString, self.__root, ind, outputString)
            if(ind == -1):
                break
        print("hello  ",outputString)
        return outputString

    # get the dictionary which has the mapping from ASCII character to its encoded bit string
    def getMappedTableAsciiToHuffman(self):
        return self.__mappingTable
    
    # get the dictionary which has the mapping from ASCII character to its number of occurences
    def getFrequencyCountOfInput(self):
        return self.__frequencyMap

    # returns the orignal string passed as an input
    def getInputString(self):
        return self.__inputString

    # returns the orignal string encoded to huffman
    def getEncodedString(self):
        return self.__encodedString

if __name__ == "__main__":

    ipString = 'sample string aaaaa eee ccccccccccccccccccc'
    test = HuffmanCoder(ipString)
    print()
    test.printEncodedString()
    print()
    test.printFrequencyCountOfInput()
    print()
    test.printMappingTableAsciiToHuffman()
    print()
    test.bitsUsedByBothMethods()
    print()


