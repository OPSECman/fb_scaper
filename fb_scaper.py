#
#	An OPSECman Product
#
#	Use irresponsibly
#
#Usage: python fb_scraper.py <page URL name here>
#CLI only
#
import facepy
import sys

def main():
	page = sys.argv[1]
	access_token = "YOUR ACCESS TOKEN GOES HERE"
	graph = facepy.GraphAPI(access_token)
	url_comments_likes = page + "/posts?limit=100&fields=likes{id,name},comments{id}"
	
	comments_likes = graph.get(url_comments_likes)
	for key, value in comments_likes.iteritems():
		if key == 'data':
			first_list = value
			for i in first_list:
				for key, value in i.iteritems():
					if key == 'likes' or key == 'comments':
						temp_dict = value
						for key, value in temp_dict.iteritems():
							if key == 'data':
								second_list = value
								for j in second_list:
									for key, value in j.iteritems():
										if key == 'id' and '_' not in value:
											print "id:\t"+value
										if key == 'name':
											print "name:\t"+value+"\r\n"

	return

if __name__ == "__main__":
	main()
