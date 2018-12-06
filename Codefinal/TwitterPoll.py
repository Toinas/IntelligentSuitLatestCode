import time
import csv
import pandas as pd
import numpy
import threading
from IPython.display import display as ds


filename='C:/code/IntelligentSuit/tweet.csv'

def printdiffs(df_in):	
	df_in = find_diffs(df_in)
	return df_in
	
	
		
def find_diffs(df_in):
	df_latest = pd.read_csv(filename)
	# print("old frame is:\n{}".format(df_in))	
	# print("newdata frame is:\n{}".format(df_latest))
	diff_df = pd.merge(df_latest, df_in, how='outer', indicator='Exist')

	diff_df = diff_df.loc[diff_df['Exist'] != 'both']
	# print 'new dataframe size is' + str(df_in.size)
	
	if diff_df.size >= 1:
		print 'diff found' + str(diff_df.size)
		# print str(diff_df.size)
		ds_list = df_latest.values[-1].tolist()
		print ds_list[1]
		#print "just the value" + str(df_latest[1])
		df_in = df_latest
	return df_in

if __name__== '__main__':

	df_last = pd.DataFrame()
	df_in =pd.DataFrame()
	df_in = pd.read_csv(filename)	
	i=0
	
	while True:   
		print("executing trhead")
		df_in= printdiffs(df_in)
		time.sleep(7)
		i = i +1 
		

	
	

# i=0
# j=0
# last_tweet=""
# tweet_date=""
# tweet_text=""

# with open(filename, 'r') as f:
	# for row in reversed(list(csv.reader(f))):
		# if i==0:
			# print(', '.join(row))
			# i+=1			
			# if row == last_tweet:
				# break
			# else:
				# for column in row:
					# if j==0:
						# if tweet_date=="":
							# tweet_date=column
							# print tweet_date
							
					# if j==1:
						# tweet_text=column
						# print tweet_text
						
					# j=+1

				
			# if last_tweet == "":
				# last_tweet = row
				# print last_tweet
			
			