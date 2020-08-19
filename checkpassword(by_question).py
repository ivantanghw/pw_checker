import requests
import hashlib
import sys

# api for checking whether the password has been pwned
def request_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again'
        )
    return res

#  
# hash_to_check == count of leakage
def get_password_leaks_count(hashes, hash_to_check):
    hashes_splited = (line.split(':') for line in hashes.text.splitlines())
    for hashes_tail, count in hashes_splited:
        #once the tail is matched with the correct one, the function returns the number of being pwned
        if hashes_tail == hash_to_check:
            return count  # how many times the password has been leaked
    return 0

# Implement the above two functions
def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    #'response'includes all possible tails matched with the first5_char (hash prefix) given to the 'request_api' function
    response = request_api(first5_char)
    return get_password_leaks_count(response, tail)



def main(args):
    # for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'Password: {password}, was found {count} times ... you should probably change your password!')
        else:
            print(f'Password: {password}, was NOT found. You can use it!')
        return 'done!'


# accept all the arguments
if __name__ == '__main__':
    # exit will let you get the value returned --> 'done!'
    password = input('What is your password to check? ')
    sys.exit(main(password))
