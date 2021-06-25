# Databricks notebook source
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

print("TESTING THE COUNT ON AZURE SERVER. COUNT IS: ", spark.range(100).count())