# question 1- dates

def is_date_format_correct(date):
    if (date[4] == "-" and date[7] ==  "-"):
          return "True"
    else:
        return "False"
    
is_date_format_correct("2022-10-01")
is_date_format_correct("2022/10/01")
is_date_format_correct("20221001")