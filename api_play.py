import flickrapi

api_key = u'a1d88869dab6eac4056848acd41d0376'
api_secret = u'185ff65976e1c007'

flickr = flickrapi.FlickrAPI(api_key, api_secret)
photos = flickr.photos.search(text="interesting dog")
print photos
