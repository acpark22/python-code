def make_shirt(shirt_size='large', shirt_text='I love Python'):
    """Display t-shirt size and message."""
    print(f"\nMy shirt size is {shirt_size.title()}.")
    print(f"My shirt should say, {shirt_text}.")

make_shirt()
make_shirt('medium')
make_shirt('medium', 'Its a miracle')

#shirt size and text both have defaults. Make a large shirt and a medium shirt w/ the default message, and a shirt of any size w/ a different message.
