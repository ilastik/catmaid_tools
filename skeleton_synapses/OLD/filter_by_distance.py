import csv
from skeleton_synapses.skeleton_utils import CSV_FORMAT

def filter_by_distance( synapse_detections_csv, output_csv, max_distance, column_name ):
    with open(synapse_detections_csv, 'r') as detections_file, \
         open(output_csv, 'w') as output_file:

        csv_reader = csv.DictReader(detections_file, **CSV_FORMAT)
    
        output_columns = csv_reader.fieldnames
        csv_writer = csv.DictWriter(output_file, output_columns, **CSV_FORMAT)
        csv_writer.writeheader()

        for row in csv_reader:
            distance = float(row[column_name])
            if distance >= max_distance:
                csv_writer.writerow(row)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv")
    parser.add_argument("output_csv")
    parser.add_argument("max_distance")
    parser.add_argument("column_name")
    
    parsed_args = parser.parse_args()
    
    filter_by_distance( parsed_args.input_csv,
                        parsed_args.output_csv,
                        float(parsed_args.max_distance),
                        parsed_args.column_name )
    