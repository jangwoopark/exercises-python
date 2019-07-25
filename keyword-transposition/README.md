A keyword transposition cipher is a method of choosing a monoalphabetic substitution to encode a message. The substitution alphabet is determined by choosing a keyword, arranging the remaining letters of the alphabet in columns below the letters of the keyword, and then reading back the columns in the alphabetical order of the letters of the keyword.

For instance, if one chose the keyword SECRET, the columns generated would look like the following diagram. Note how the letters in the keyword are skipped when laying out the columns, and duplicate letters are removed from the keyword:

SECRT
ABDFG
HIJKL
MNOPQ
UVWXY
Z
Since the alphabetical order of the characters in the keyword is CERST, the columns are then rearranged based on the first row. Then, the letters are read column-wise to get the substitution cipher as shown below:

CERST         CDJOW
DBFAG         EBINV
JIKHL    =>   RFKPX
ONPMQ         SAHMUZ
WVXUY         TGLQY
   Z
After that, we match the order to the alphabet to get:

Original:     ABCDE FGHIJ KLMNO PQRSTU VWXYZ
Substitution: CDJOW EBINV RFKPX SAHMUZ TGLQY
Task

Given a piece of ciphertext and the keyword used to encipher it, write an algorithm to output the original message with the keyword transposition cipher described above.

Input Format

The first line of input will be an integer  indicating the number of test cases to follow. 
For each test case in , two additional lines will follow, one containing the keyword, and one containing the ciphertext, respectively. 
The keyword will be, at most,  characters long, and the ciphertext will be, at most,  characters in length (all uppercase).

Output Format

Output the decoded version of the ciphertext for each test case, one per line.

Sample Input

2
SPORT
LDXTW KXDTL NBSFX BFOII LNBHG ODDWN BWK
SECRET
JHQSU XFXBQ
Sample Output

ILOVE SOLVI NGPRO GRAMM INGCH ALLEN GES
CRYPT OLOGY
