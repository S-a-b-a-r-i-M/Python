import re 

def extract_year(date) -> int:
        if isinstance(date, int):
            return date
        patterns = [
            r"\d{4}",  # Matches 'YYYY'
            # r"\d{1,2}/\d{4}",  # Matches 'M/YYYY' or 'MM/YYYY'
            # r"\d{1,2}-\d{4}",  # Matches 'M-YYYY' or 'MM-YYYY'
            # r"[a-zA-Z]{3} \d{4}",  # Matches 'Mon YYYY' (e.g., 'Jul 2015')
        ]
        try:
            for pattern in patterns:
                match = re.search(pattern, date)
                if match:
                    try:
                        return str(int(match.group()))
                    except ValueError:
                        continue
            return None
        except Exception as e:
            print(e)
            return

print(extract_year('may 2002'))