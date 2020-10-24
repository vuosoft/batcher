MAX_RECORD_SIZE = 1024*1024
MAX_BATCH_SIZE = 5 * 1024*1024
MAX_RECORDS_IN_BATCH = 500
ENABLE_LOGGER = False

def batcher(records, max_record_size=MAX_RECORD_SIZE, max_batch_size=MAX_BATCH_SIZE, max_records_in_batch=MAX_RECORDS_IN_BATCH):
    """
    Input in form of [<record1>, <record2>, <record3>, ... , <recordn>]
    Output is: [<batch1>, <batch2>, ..., <batchn>] where each batch is an array of records just like in the input.
    Maximum size of output record is 1 MB, larger records should be discarded.
    Maximum size of output batch is 5 MB. 
    Maximum number of records in an output batch is 500. 
    Inputs:
    * records as array containing strings
    * max_record_size integer, will be used to modify maximum size of output record
    * max_batch_size integer will be used to modify maximum size of output batch
    * max_records_in_batch integer will be used to modify maximum number of records in an output batch
    Returns:
    * Array of arrays containing valid input records
    """

    try:
        logger(f"Records: {records}", ENABLE_LOGGER)
        batches = []
        batch_size = 0
        record_count = 0
        output_records = []

        for input_record in records:        
            if byte_size(input_record) <= max_record_size: 
                logger(f"input_record: {input_record}", ENABLE_LOGGER)
                batch_size += byte_size(input_record)
                record_count += 1
                if batch_size > max_batch_size or record_count > max_records_in_batch:
                    logger(f"batch_size: {batch_size}", ENABLE_LOGGER)
                    logger(f"output_records: {output_records}", ENABLE_LOGGER)
                    batches.append(output_records)
                    output_records = []
                    batch_size = 0
                    record_count = 0
                    output_records.append(input_record)
                    
                else:
                    logger(f"batch_size: {batch_size}", ENABLE_LOGGER)
                    logger(f"output_records: {output_records}", ENABLE_LOGGER)
                    output_records.append(input_record)
                    logger(f"output_records: {output_records}", ENABLE_LOGGER)
            else:
                logger(f"Skipping, too large (max {max_record_size}), length: {byte_size(input_record)}", True)

        if output_records:
            batches.append(output_records)

        logger(f"batches: {batches}", ENABLE_LOGGER)
        return batches
    except Exception as e:
        logger(f"{e}", True)
        raise

def byte_size(input):
    """
    returns the size of input taking in the consideration potential 
    unicode characters that takes more than 1 byte be character
    Inputs:
    * input string, the string that the size will be calculated
    Returns:
    * size integer
    """
    return len(input.encode('utf-8'))

def logger(input, enable=True):
    """
    Will print the input string if enabled
    Inputs:
    * input string that will be printed
    * enable boolean, if True, print the input
    Returns:


    """
    if enable:
        print(input)
        
        