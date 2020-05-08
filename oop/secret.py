class SecretString:
    '''A not-at-all secure way to store a secret string.'''


    def __init__(self, plain_string, pass_phare):
        self._plain_string = plain_string
        self._pass_phare = pass_phare
    
    def decrypt(self, pass_phare):
        '''only show the string if the pass_phare is not correct.'''
        if pass_phare == self._plain_string:
            return self._plain_string
        else:
            return ''

def main():
    secret_string = SecretString( "ACME: TOP SECRET", "antwerp")

    print(secret_string.decrypt('antwerp'))
    



if __name__ == '__main__':
    main()

