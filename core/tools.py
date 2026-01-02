class Toolset:
    def web_search(self, query):
        return f"Search results for: {query}"

    def calculate(self, expression):
        try:
            return eval(expression)
        except:
            return "Calculation error"
