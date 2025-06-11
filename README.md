# 🗂️ MySQL Schema to JSON

A Python script that parses a MySQL `.sql` dump file and extracts **table structures** and **foreign key relationships** into a clean, readable `JSON` format — without needing to import it into a running MySQL server.

## 🚀 Features

- Parses `CREATE TABLE` and `FOREIGN KEY` definitions
- Extracts column names, data types, and constraints
- Captures table relationships through foreign keys
- Works directly with `.sql` dump files - no database connection required
- Identifies primary keys, unique constraints, and indexes

## 📦 Requirements

- Python 3.6+
- [`sqlparse`](https://pypi.org/project/sqlparse/)

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🧪 Setting Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 📁 Usage

1. Place your MySQL dump file (e.g., `backup.sql`) in the same folder.
2. Run the script:

```bash
python schema_parser.py backup.sql
```

3. Output:

```bash
✅ Generated mysqlrelationship.json
```

## 📄 Output Format

The generated `mysqlrelationship.json` contains a detailed representation of your database schema:

```json
{
  "tables": {
    "table_name": [
      { "name": "column_name", "type": "data_type" },
      { "name": "PRIMARY", "type": "KEY" },
      { "name": "KEY", "type": "`foreign_key_constraint`" },
      { "name": "CONSTRAINT", "type": "`constraint_definition`" }
    ]
  },
  "relationships": [
    {
      "table": "table_name",
      "column": "column_name",
      "references_table": "referenced_table",
      "references_column": "referenced_column"
    }
  ]
}
```

## 🛠️ File Structure

```
mysql-schema-to-json/
├── schema_parser.py        # Main parser script
├── mysqlrelationship.json  # Output file (generated)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── backup.sql              # Your MySQL dump file (not included)
```

## 📌 Notes

- The script extracts table definitions, columns, keys, and constraints
- Special handling for foreign key relationships to build the relationships array
- Works with standard MySQL dump files containing CREATE TABLE statements
- Parses schema only - data rows are ignored

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify.

## 👨‍💻 Author

Made with ❤️ by Wai Hyn Htun
GitHub: [@kamkyi](https://github.com/kamkyi)
