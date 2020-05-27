def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                location = 'princeton',
                field = 'physics')
print(user_profile)
#using arb keyword args. The def of 'build_profile()' expects first and last name and then allows in as many name-value pairs as they want.
# the ** before the paramenter cause Pyt to create an empty dict called 'user_info' and pack whatever name-value pairs it recvs into the dict.
#Within the func, you can access the key-value pairs in 'user_info' just as you would for any dict. 
#In the body of 'build_profile' we add the first and last names to the 'user_info dict bc we'll always rec this info, and they havent been placed in the dict yet. the we return the 'user_info' dict to the func call line.
#we call 'build_profile' passing the first name 'albert', last name'einstein', and the 2 key val pairs, loc='prin' and field= 'phy'. 
#we assigned the returned 'profile' to 'user_profile' and print 'user_profile'

