import numpy as np
import pandas as pd

def clean(df):
	# get date
	df['date'] = df.apply(lambda row: row['image'].split('/')[-2], axis=1)
	# remove filepath and reorganize dataframe...
	cols = ['date', 'tags']
	df = df[cols]

	df.to_csv("google_cloud_image_annotations.csv")


df = pd.read_csv("google_cloud_image_annotations.csv")
clean(df)
