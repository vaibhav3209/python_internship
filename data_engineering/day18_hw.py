user_table = spark.table("default.table_metadata")  # table ingested
user_table.display()

columns = user_table.collect()  # collect the table metadata
for _ in columns:
    print(_)

tables = {}
for row in columns:
    tname = row[0]
    col_def = f"{row[1]} {row[2]}"
    if tname not in tables:
        tables[tname] = []
    tables[tname].append(col_def)
for i, j in tables.items():
    spark.sql(f'''CREATE TABLE if not exists {i} 
            ({','.join(j)})
            ''')

'''get all tables according to metadata'''
# new_df = spark.sql('select * from raw_table')
# new_df.display()
# new_df2 = spark.sql('select * from curated_table')
# new_df2.display()
new_df3 = spark.sql('select * from gold_table')
new_df3.display()