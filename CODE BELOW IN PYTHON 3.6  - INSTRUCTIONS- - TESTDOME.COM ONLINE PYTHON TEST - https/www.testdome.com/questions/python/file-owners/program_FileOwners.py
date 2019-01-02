## CODE BELOW IN PYTHON 3.6

## INSTRUCTIONS:
## TESTDOME.COM ONLINE PYTHON TEST
## https://www.testdome.com/questions/python/file-owners/11846
## - Implement a group_by_owners function that:
## 1.) Accepts a dictionary containing the file owner name for each file name.
## 2.) Returns a dictionary containing a list of file names for each owner name, in any order.
## - For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
## - The group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

## THEORETICAL ALGORITHM AS ROUGH HYPOTHESIS:
## STEP 0.) TAKE THE VALUES (NAMES) FROM DICTIONARY AND CREATE SET OF NAMES
## STEP 1.) TAKE THE SET OF VALUES (NAMES) AND MAKE THEM KEYS OF NEW DICTIONARY;
## STEP 2.) ADD EMPTY LISTS FOR VALUES IN NEW DICTIONARY
## STEP 3.) APPEND TO THE LISTS NEW VALUES (FILENAMES) FROM OLD KEYS IN OLD DICTIONARY

## ACTUAL ALGORITHM IN PRACTICE:
## FOR EACH KEY (FILENAME) AND VALUE (NAME) IN ITERABLE DICTIONARY.ITEMS() VIEW OBJECT...

## IF VALUE (NAME) IS IN NEW DICTIONARY OF SWITCHED KEYS AND VALUES AS NEW KEY
## ...I.E. IF VALUE (NAME) EXISTS AS KEY IN THIS NEW DICTIONARY...
## ...THEN APPEND OLD KEY (FILENAME) TO NEW DICTIONARY AS NEW VALUE; BECAUSE OLD VALUE (NAME) AS NEW KEY EXISTS IN NEW DICTIONARY
## ...APPEND METHOD AUTOMATICALLY APPENDS VALUE AS NEW LIST OBJECT CONTAINING THE VALUE(S).

## ELSE IF VALUE (NAME) IS NOT (i.e. DOES NOT ALREADY EXIST) IN NEW DICTIONARY AS NEW KEY...
## ...THEN OLD VALUE (NAME) WILL BE NEW KEY (NAME) IN NEW DICTIONARY
## ...AND OLD KEY (FILENAME) WILL BE NEW VALUE (FILENAME) IN NEW DICTIONARY 

## IMPORT MODULES (NONE NECESSARY)
## IMPORT MODULES (NONE NECESSARY)
## IMPORT MODULES (NONE NECESSARY)

## DECLARE INITIAL VARIABLES (NONE NECESSARY)
## DECLARE INITIAL VARIABLES (NONE NECESSARY)
## DECLARE INITIAL VARIABLES (NONE NECESSARY)

## DEFINE CLASSES
## DEFINE CLASSES
## DEFINE CLASSES

class FileOwners:

    ## @staticmethod
    @staticmethod

    ## DEFINE FUNCTIONS
    ## DEFINE FUNCTIONS
    ## DEFINE FUNCTIONS
    def group_by_owners(files):

        ## DEFINE INITIAL VARIABLES NEEDED
        DictOfSwitchedKeysAndValues = {} ## EMPTY DICTIONARY

        ## FOR EACH KEY (FILENAME) AND VALUE (NAME) IN ITERABLE DICTIONARY.ITEMS() VIEW OBJECT...
        for key, value in files.items():  ## for FILENAME, NAME in files.items():
            print("key =", key, type(key), len(key)) ## FILENAME
            print("value =", value, type(value), len(value)) ## NAME
            
            
            ## IF VALUE (NAME) IS IN NEW DICTIONARY OF SWITCHED KEYS AND VALUES AS NEW KEY
            ## ...I.E. IF VALUE (NAME) EXISTS AS KEY IN THIS NEW DICTIONARY...
            if value in DictOfSwitchedKeysAndValues:

                ## ...THEN APPEND OLD KEY (FILENAME) TO NEW DICTIONARY AS NEW VALUE; BECAUSE OLD VALUE (NAME) AS NEW KEY EXISTS IN NEW DICTIONARY
                ## ...APPEND METHOD AUTOMATICALLY APPENDS VALUE AS NEW LIST OBJECT CONTAINING THE VALUE(S).
                DictOfSwitchedKeysAndValues[value].append(key)
                print("FIRST OPTION **IF** - DictOfSwitchedKeysAndValues[value] =", DictOfSwitchedKeysAndValues[value],
                      type(DictOfSwitchedKeysAndValues[value]), len(DictOfSwitchedKeysAndValues[value]))
                print("\n")
                
            ## ELSE IF VALUE (NAME) IS NOT (i.e. DOES NOT ALREADY EXIST) IN NEW DICTIONARY AS NEW KEY...
            else:

                ## ...THEN OLD VALUE (NAME) WILL BE NEW KEY (NAME) IN NEW DICTIONARY
                ## ...AND OLD KEY (FILENAME) WILL BE NEW VALUE (FILENAME) IN NEW DICTIONARY
                DictOfSwitchedKeysAndValues[value] = [key] ## DictOfSwitchedKeysAndValues[NAME] = [FILENAME]
                print("SECOND OPTION **ELSE** - DictOfSwitchedKeysAndValues[value] =", DictOfSwitchedKeysAndValues[value],
                      type(DictOfSwitchedKeysAndValues[value]), len(DictOfSwitchedKeysAndValues[value]))
                print("\n")


        ## TEST OUTPUT BEFORE RETURNING DICTIONARY
        print(DictOfSwitchedKeysAndValues)
                
        ## RETURN DICTIONARY OF SWITCHED KEYS AND VALUES
        return(DictOfSwitchedKeysAndValues)

        ## END DEFINE FUNCTIONS
        ## END DEFINE FUNCTIONS
        ## END DEFINE FUNCTIONS

## END DEFINE CLASSES
## END DEFINE CLASSES
## END DEFINE CLASSES

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
    
## DECLARE VARIABLES

## CREATE DICTIONARY
files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

## CALL CLASS.FUNCTION AND PASS VARIABLE 
ClassCall = FileOwners.group_by_owners(files)

## TEST OUTPUT
print(ClassCall)


## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
    
## WE HOPE YOU ENJOYED AND THAT THIS HELPS YOUR UNDERSTANDING OF USING PYTHON LANGUAGE TO SOLVE PROBLEMS WITH PYTHON PROGRAMMING
## PLEASE COME BACK AGAIN SOON
## PLEASE VISIT OUR WEB SITES (OUR PROBLEM-SOLVING PROGRAMMING, CODING, & DEVELOPMENT SERVICES ARE AVAILABLE FOR HIRE):
## www.JerusalemProgrammer.com
## www.JerusalemProgrammers.com
## www.JerusalemProgramming.com
