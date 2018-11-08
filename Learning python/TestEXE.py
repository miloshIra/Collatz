
import re

def process_date(this_date):

    # this regex maes sure that the date is DD-MM-YYYY
    if not re.search(r'\d\d-\d\d-\d\d\d\d$', this_date):
        raise ValueError('please submit date in DD-MM-YYYY format')

    print('the submited date is {0}'.format(this_date))

process_date('01-03-1988')
print; print
process_date('1/3/1111')

## Creating Exception class!!! ()()

class Error(Exception):
    def __init__(self, *args):
        print('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        print('calling str')
        if self.message:
            return("here's MyError exception with message:  {0}".format(self.message))
        else:
            return ("here's a MyError exception")

raise MyError

raise MyError('Houston, we have a problem')
