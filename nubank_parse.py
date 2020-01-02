from bs4 import BeautifulSoup
import pandas as pd
import re
import sys


def get_expenses(file_name):
    soup = BeautifulSoup(open(file_name), "html.parser")
    dict_list = []
    for subtable in soup.find_all("tbody")[1:]:
        date = subtable.find(attrs={"class": "dc-table-label"}).text
        date_regex = re.findall("\d{2}/[\w]{3}/\d{4}", date)
        if len(date_regex) == 1:
            for node in subtable.find_all(attrs={"class": "transaction"}):
                classes = node.get("class")
                dict_list.append(
                    {
                        "category": node.find(attrs={"class": "title"}).text,
                        "name": node.find(attrs={"class": "description"}).text,
                        "amount_unformatted": node.find(attrs={"class": "amount"}).text,
                        "date_unformated": date,
                        "id": node.get("id"),
                    }
                )
        else:
            print(f"{date} is not a date")

    data = pd.DataFrame(dict_list)

    amount = data.amount_unformatted.str.extract(
        "^(?P<currency>\w\$) (?P<amount_to_parse>[\d|.|,]*)"
    )
    data = pd.concat([data, amount], axis=1)


    assert data.isnull().sum().sum() == 0

    data["amount"] = data.amount_to_parse.str.replace("[,|.]", "").astype(int)

    months = [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago",
        "Set",
        "Out",
        "Nov",
        "Dez",
    ]
    month_translation = {k: v for k, v in zip(months, range(1, 13))}

    parsed_date = data.date_unformated.str.extract(
        "(?P<day>\d{2})/(?P<month>\w{3})/(?P<year>\d{4})"
    )
    parsed_date["month"] = parsed_date.month.replace(month_translation)

    data["date"] = pd.to_datetime(parsed_date)

    return data


if __name__ == '__main__':
    get_expenses(sys.argv[1]).to_csv('nubank.csv')
