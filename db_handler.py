import psycopg2

def write_to_db(record, db_params):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO user_logins (
        user_id, device_type, masked_ip, masked_device_id,
        locale, app_version, create_date
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        record["user_id"], record["device_type"],
        record["masked_ip"], record["masked_device_id"],
        record["locale"], record["app_version"],
        record["create_date"]
    ))
    conn.commit()
    cursor.close()
    conn.close()