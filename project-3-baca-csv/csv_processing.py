import pandas as pd

SALES_CSV_FILE_PATH = './sales_data_sample.csv'
ORDER_NUM_COLUMN = 'ORDERNUMBER'
PRODUCT_COLUMN = 'PRODUCTCODE'
PRICE_EACH_COLUMN = 'QUANTITYORDERED'
QUANTITY_ORDER_COLUMN = 'PRICEEACH'
SALES_COLUMN = 'SALES'

## Read the csv file & extracting the data
def extract_data(filepath):
    sales_data = pd.read_csv(filepath, encoding='latin1')
    return sales_data

## Summarize the data based on the data needed
def summarize_sales(data):
    summary_data = {}
    total_sales = 0
    highest_sales = 0
    for row in data:
        total_sales += row[-1]
        if row[-1] > highest_sales:
            highest_sales = row[-1]
    summary_data['total_sales'] = total_sales
    summary_data['highest_sales'] = highest_sales
    summary_data['num_of_sales'] = len(data)
    return summary_data

## Run an entire program
if __name__ == '__main__':
    sales_data = extract_data(SALES_CSV_FILE_PATH)
    sales_data = sales_data.loc[:, [ORDER_NUM_COLUMN, 
                                    PRODUCT_COLUMN, 
                                    PRICE_EACH_COLUMN, 
                                    QUANTITY_ORDER_COLUMN, 
                                    SALES_COLUMN]]
    
    sales_summary = summarize_sales(sales_data.values)    
    summary = """
    SALES SUMMARY:
    Total sales: ${total_sales:.2f}
    Highest sales: ${highest_sales:.2f}
    Number of sales: {num_of_sales}
    """.format(**sales_summary)
    print(summary)
    