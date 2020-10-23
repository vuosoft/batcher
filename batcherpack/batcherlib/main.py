MAX_RECORD_SIZE = 11 # 1024*1024
MAX_BATCH_SIZE = 11 # 5 * 1024*1024
MAX_RECORDS_IN_BATCH = 50 # 5 * 1024*1024

def batcher(records):
    """
    Input in form of [<record1>, <record2>, <record3>, ... , <recordn>]
    Output is: [<batch1>, <batch2>, ..., <batchn>] where each batch is an 
    array of records just like in the input.
    Maximum size of output record is 1 MB, larger records should be discarded
    Maximum size of output batch is 5 MB
    Maximum number of records in an output batch is 500
    """

    batches = []
    batch_size = 0
    output_records = []

    for input_record in records:        
        if len(input_record) <= MAX_RECORD_SIZE: 
            print(f"C: {input_record}")
            batch_size += len(input_record.encode('utf-8'))
            if batch_size > MAX_BATCH_SIZE:
                print(f"A: {batch_size}")
                print(f"A: {output_records}")
                batches.append(output_records)
                output_records = []
                output_records.append(input_record)
            else:
                print(f"B: {batch_size}")
                print(f"B: {output_records}")                
                output_records.append(input_record)
                print(f"B: {output_records}")   
        else:
            print(f"Skipping, too large, length: {len(input_record.encode('utf-8'))}, {input_record}")

    if output_records:
        batches.append(output_records)

    print(f"batches: {batches}")
    return batches






def addnumbers(a, b):
    return a + b
