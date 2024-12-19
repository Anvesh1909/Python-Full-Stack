from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression

# Step 1: Create a SparkSession
spark = SparkSession.builder.appName("PySparkPipelineExample").getOrCreate()

# Step 2: Create a sample DataFrame
data = spark.createDataFrame([
    (0, "male", 25, 3000, 0),
    (1, "female", 32, 4000, 1),
    (2, "male", 40, 5000, 0),
    (3, "female", 28, 3500, 1),
], ["id", "gender", "age", "income", "label"])

# Step 3: Define the stages of the pipeline
# StringIndexer to convert categorical column 'gender' into numerical
gender_indexer = StringIndexer(inputCol="gender", outputCol="gender_index")

# VectorAssembler to combine feature columns into a single vector
assembler = VectorAssembler(inputCols=["gender_index", "age", "income"], outputCol="features")

# Logistic Regression Model
lr = LogisticRegression(featuresCol="features", labelCol="label")

# Step 4: Create a Pipeline
pipeline = Pipeline(stages=[gender_indexer, assembler, lr])

# Step 5: Fit the Pipeline to the data
model = pipeline.fit(data)

# Step 6: Make predictions
predictions = model.transform(data)

# Step 7: Show results
predictions.select("id", "features", "label", "prediction").show()
