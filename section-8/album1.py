def make_album(artist_name, album_title):
    """Return a dictionary of info about artists."""
    music_album = {'name' : artist_name.title(), 'title': album_title.title()}
    return music_album

artist = make_album('tupac shakur', 'all eyez on me')
print(artist)

artist = make_album('ludacris', 'word of mouf')
print(artist)

artist = make_album('prince', 'purple rain')
print(artist)

