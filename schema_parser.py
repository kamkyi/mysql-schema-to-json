import sqlparse
import json
import re

def parse_backup_sql(file_path):
    with open(file_path, 'r') as f:
        sql = f.read()

    # Split SQL into individual statements
    statements = sqlparse.split(sql)
    tables = {}
    relationships = []

    for stmt in statements:
        stmt_clean = stmt.strip()
        if stmt_clean.upper().startswith("CREATE TABLE"):
            parsed = sqlparse.parse(stmt_clean)[0]
            tokens = [token for token in parsed.tokens if not token.is_whitespace]

            # Extract table name
            table_name = None
            for token in tokens:
                if token.ttype is None and token.get_name():
                    table_name = token.get_name()
                    break
            if not table_name:
                continue

            # Extract column and foreign key info
            columns = []
            fk_pattern = re.compile(
                r'FOREIGN KEY\s+\((.*?)\)\s+REFERENCES\s+`?(\w+)`?\s+\(`?(\w+)`?\)', re.IGNORECASE)

            column_lines = stmt_clean.splitlines()
            for line in column_lines:
                line = line.strip().rstrip(',').rstrip()
                if line.upper().startswith('FOREIGN KEY'):
                    match = fk_pattern.search(line)
                    if match:
                        fk_col, ref_table, ref_col = match.groups()
                        relationships.append({
                            "table": table_name,
                            "column": fk_col.strip('` '),
                            "references_table": ref_table,
                            "references_column": ref_col
                        })
                elif '`' in line and 'CREATE TABLE' not in line:
                    parts = line.split()
                    if len(parts) >= 2:
                        col_name = parts[0].strip('`')
                        col_type = parts[1]
                        columns.append({
                            "name": col_name,
                            "type": col_type
                        })

            tables[table_name] = columns

    return {
        "tables": tables,
        "relationships": relationships
    }


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python schema_parser.py path/to/backup.sql")
        sys.exit(1)

    backup_file = sys.argv[1]
    result = parse_backup_sql(backup_file)

    with open("mysqlrelationship.json", "w") as f:
        json.dump(result, f, indent=4)

    print("✅ Generated mysqlrelationship.json")
