import twittercredentials
import csv
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import time

hashtag1 = "#IMEC18"
hashtag2 = "#GiraMexicoPorSiempre"
hashtag3= "#ToinasMakerRegresa"

# Open/create a file to append data to


#csvFile = open('result.csv', 'a')
#Use csv writer


#csvFile = open('C:/code/IntelligentSuit/tweet.csv', 'a')
csvFile = open('/home/upsquared/Adafruit_NeoPixel_FTDI/tweet.csv', 'a')
csvWriter = csv.writer(csvFile)

class listener(StreamListener):
    # def on_data(self, data):
		# tweet = data.split(',"text":"')[1].split('","source')[0]
		# if(tweet):
            # #replace with custom tag 1
			# if ('#ToinasMakerRegresa' in tweet):
				# print(tweet+"\n")
				# time.sleep(5)
            # #replace with custom tag 2        
			# elif(hashtag2 in tweet):
				# print(tweet+"\n")
				# time.sleep(5)
            # #replace with custom tag 3
			# elif(hashtag3 in tweet):
				# print(tweet+"\n")
				# time.sleep(5)
		# return(True)
	def on_status(self, status):
		print 'Tweet text:' + status.text
		try:
			#csvFile = open('C:/code/IntelligentSuit/tweet.csv', 'a')
			csvFile = open('/home/upsquared/Adafruit_NeoPixel_FTDI/tweet.csv', 'a')
		#Use csv writer
			csvWriter = csv.writer(csvFile)
			csvWriter.writerow([status.created_at, status.text.encode('utf-8')])
			csvFile.close()
			return(True)
		except:
			time.sleep(5)
			csvWriter.writerow([status.created_at, status.text.encode('utf-8')])
			print("file is already open")
			csvFile.close()
			raise
		
	def on_error(self, status_code):
		print('Got an error with status code: ' + str(status_code))
		return(True) # To continue listening
 
	def on_timeout(self):
		print('Timeout...')
		return(True) # To continue listening
		
    
	# def on_error(self, status):
		# if status == 420:
			# #returning False on_data method in case rate limit occurs
			# return False
		# print(status)

if __name__ == '__main__':

	auth = OAuthHandler(twittercredentials.CONSUMER_KEY, twittercredentials.CONSUMER_SECRET)
	auth.set_access_token(twittercredentials.ACCESS_TOKEN, twittercredentials.ACCESS_TOKEN_SECRET)

	twitterStream = Stream(auth, listener())
#replace hashtags with custom tags below. ALSO: replace tags in lines #30, #48, and #66
	print("tracking: " + hashtag1 + "," + hashtag2 + "," + hashtag3)
	
	twitterStream.filter(track=[hashtag1, hashtag2, hashtag3])
	print "does it ever go back here?"
	
	
	


