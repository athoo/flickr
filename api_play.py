from flask import Flask
import flickrapi
import os
import json
api_key = os.environ['FLICKR_API_KEY']
api_secret = os.environ['FLICKR_SECRET']
flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/task_name/<task_name>')
def query_task(task_name):
    ongoing_imgs=[]
    task_photos = flickr.photos.search(text=task_name)
    for item in task_photos['photos']['photo'][:]:
        farm_id = item['farm']
        server_id = item['server']
        pic_id = item['id']
#         tags = flickr.tags.getListPhoto(photo_id=pic_id)
#         tag_list = []
#         for tag in tags['photo']['tags']['tag']:
#             tag_list.append(tag['_content'])
        secret = item['secret']
        url = "https://farm{}.staticflickr.com/{}/{}_{}.jpg".format(farm_id,server_id,pic_id,secret)
        ongoing_imgs.append(url)
#         img_urls.append(tuple([url,tag_list]))
    json_imgs = json.dumps(ongoing_imgs)
    return str(json_imgs)

@app.route('/img_id/<img_id>')
def get_tags(img_id):
#     return "hello%s"%img_id
    tags_cloud=[]
    tags = flickr.tags.getListPhoto(photo_id=img_id)
    for tag in tags['photo']["tags"]["tag"]:
        tags_cloud.append(tag['_content'])
#     json_tags = json.dumps(tags_cloud)
#     return json_tags
    json_tags = json.dumps(tags_cloud)
    return json_tags
    
    
if __name__ == "__main__":
#     app.run(debug=True)
    app.run()