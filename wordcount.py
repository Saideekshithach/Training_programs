from pyspark import SparkContext

sc = SparkContext("local", "Word Count")

text_rdd = sc.textFile("sample.txt")

words = text_rdd.flatMap(lambda line: line.split(" "))
word_pairs = words.map(lambda word: (word, 1))
word_counts = word_pairs.reduceByKey(lambda a, b: a + b)

print(word_counts.collect())
cc