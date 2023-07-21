import csv

def data_scrubber(file_in, file_out, column, bad_data, clean_data):
    # Working storage
    records = []

    # Get the data from the input file
    try:
        with open(file_in) as rating_file:
            reader = csv.DictReader(rating_file)
            for row in reader:
                records.append(dict(row))

    except:
        print("Could not read file")
        return None

    # Clean the data
    for record in records:
        if record[column] == str(bad_data):
            record[column] = clean_data

    # Save the new file
    with open(file_out, "w") as clean_rating_file:
        writer = csv.DictWriter(clean_rating_file, fieldnames=records[0].keys())
        writer.writerows(records)


if __name__ == '__main__':
    rating_file_in = './unit_7_restaurant_rating.csv'
    rating_file_out = './unit_7_restaurant_rating_cleaned.csv'

    data_scrubber(rating_file_in, rating_file_out, "Worth_the_price", "45", "no")
    print("Data cleaned")

