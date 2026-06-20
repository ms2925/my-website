import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="esg_data",   # default admin database
    user="postgres",
    password="Michael06"
)

conn.autocommit = True  # important for CREATE DATABASE
cur = conn.cursor()

metrics = ["Energy consumption", "Carbon emissions", "Waste", "Health and Safety", "Employee turnover", "Gender pay gap", "Board diversity", "Board independence", "Ethics incidents"]
units = ["kWh", "tCO2e", "tonnes", "%", "%", "%", "%", "%", "count"]
description = ["total energy used in operations", "total greenhouse gas emissions", "total waste generated", "workplace injury rate", "percentage of employees leaving annually", "pay difference between genders", "percentage of female board representation", "proportion of independent directors", "number of regulatory/ ethics related incidents per year"]

for i in range(len(metrics)):
    cur.execute("""
    INSERT INTO metrics
    (metric_name, unit, description)
    VALUES (%s, %s, %s)
    """, (metrics[i], units[i], (description[i])))

conn.commit()
