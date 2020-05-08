class SecretString:
    '''A not-at-all secure way to store a secret string.'''


    def __init__(self, plain_string, pass_phrase):
        self.__plain_string = plain_string
        self.__pass_phrase = pass_phrase
    
    def decrypt(self, pass_phrase):
        '''only show the string if the pass_phare is not correct.'''
        if pass_phrase == self.__pass_phrase:
            return self.__plain_string
        else:
            return 'nono'

def main():
    secret_string = SecretString( "ACME: TOP SECRET", "antwerp")

    print(secret_string.decrypt("antwerp"))
 




if __name__ == '__main__':
    main()

