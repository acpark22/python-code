def make_album(artist_name, album_title):
    """Return the artist name and album title."""
    album_info = f"{artist_name}, {album_title}"
    return album_info.title()
while True:
    print("\nPlease tell me your favorite artist and album:")
    print("(enter 'q' at any time to quit)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    a_title = input("Album title: ")
    if a_title == 'q':
        break
    music_info = make_album(a_name, a_title)
    print(f"\nMy favorite artist and album is {music_info}")

