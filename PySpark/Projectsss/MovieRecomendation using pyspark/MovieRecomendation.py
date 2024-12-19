from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

# Create a SparkSession
spark = SparkSession.builder \
.appName(“MovieRecommendation”) \
.getOrCreate()

# Read the movie ratings data from a CSV file
ratings = spark.read \
.csv(“path/to/movie_ratings.csv”, header=True, inferSchema=True)

# Split the data into training and testing sets
(training, testing) = ratings.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS
als = ALS(maxIter=5, regParam=0.01, userCol=”userId”, itemCol=”movieId”, ratingCol=”rating”)
model = als.fit(training)

# Generate movie recommendations for a specific user
user_id = 123
recommendations = model.recommendForAllUsers(10)
user_recommendations = recommendations \
.filter(recommendations.userId == user_id) \
.select(“recommendations.movieId”)

# Show the recommended movie IDs for the user
user_recommendations.show()




# In this example, PySpark is used to build a movie recommendation engine using the Alternating Least Squares (ALS) algorithm. 
# The movie ratings data is read from a CSV file and split into training and testing sets. The ALS model is trained on the training data,
# and then recommendations are generated for a specific user. The recommended movie IDs are displayed, 
# providing personalized movie suggestions for the user.