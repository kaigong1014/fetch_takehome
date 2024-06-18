from sqs_handler import receive_messages
from pii_masking import mask_pii, flatten_and_mask
from db_handler import write_to_db
from config import QUEUE_URL, DB_PARAMS

def main():
    messages = receive_messages(QUEUE_URL)
    for message in messages:
        body = message['Body']
        flattened_data = flatten_and_mask(body)
        write_to_db(flattened_data, DB_PARAMS)

if __name__ == "__main__":
    main()