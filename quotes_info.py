class QuotesInfo:
    num_quotes = 0
    def __init__(self, name, quote):
        self.name = name
        self.quote = quote
        QuotesInfo.num_quotes += 1