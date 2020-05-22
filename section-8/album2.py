def make_album(artist_name, album_title, songs=None):
    """Display a dictionary of music info."""
    album_info = {
        'name': artist_name.title(), 
        'title': album_title.title(),
        }
    if songs:
        album_info['songs'] = songs
    return album_info
artist = make_album('tupac shakur', 'all eyez on me', songs=14)
print(artist)

artist = make_album('biggie smalls', 'ready to die', songs= 20)
print(artist)

artist = make_album('ludacris', 'word of mouf')
print(artist)

