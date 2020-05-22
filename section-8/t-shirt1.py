def make_shirt(shirt_size, shirt_text):
    """Display info about a t-shirt."""
    print(f"\nThe shirt size is {shirt_size.title()}.")
    print(f"\nThe {shirt_size.title()} shirt should read, {shirt_text}.")

make_shirt('l', 'Just Do It')
make_shirt(shirt_size='m', shirt_text='3 stripe life')

# write a func called make_shirt that accepts a size and the text of a message that should be printed on the shirt. 
# the func should print a sentence summarizing the size of the shirt and the message printed on it.
# use pos arg and keyword args.
