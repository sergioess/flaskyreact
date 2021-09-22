import psycopg2


def create_connection():
    conn = psycopg2.connect(
        host='ec2-3-231-69-204.compute-1.amazonaws.com', port=5432, database='d3hr8qndm4p50h', user='oxwttxarfidlxi', password='89e47cacfc5926776ab52a7e485b08a91bf9632736ca0843d80b6356b506f3f2')

    return conn
