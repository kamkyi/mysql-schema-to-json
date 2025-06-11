````markdown
# 🗂️ MySQL Schema to JSON

A Python script that parses a MySQL `.sql` dump file and extracts **table structures** and **foreign key relationships** into a clean, readable `JSON` format — without needing to import it into a running MySQL server.

## 🚀 Features

- Parses `CREATE TABLE` and `FOREIGN KEY` definitions
- Outputs:
  - Table names
  - Column names and types
  - Foreign key relationships
- Requires only the `.sql` dump file (no need to connect to MySQL)

---

## 📦 Requirements

- Python 3.6+
- [`sqlparse`](https://pypi.org/project/sqlparse/)

Install dependencies:

```bash
pip install -r requirements.txt
```
````

---

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

The generated file `mysqlrelationship.json` will look like this:

```json
{
  "tables": {
    "users": [
      { "name": "id", "type": "INT" },
      { "name": "email", "type": "VARCHAR(255)" }
    ],
    "orders": [
      { "name": "id", "type": "INT" },
      { "name": "user_id", "type": "INT" }
    ]
  },
  "relationships": [
    {
      "table": "orders",
      "column": "user_id",
      "references_table": "users",
      "references_column": "id"
    }
  ]
}
```

---

## 🛠️ File Structure

```
mysql-schema-to-json/
├── schema_parser.py        # Main script
├── requirements.txt        # Dependencies
├── README.md               # Project docs
└── backup.sql              # (Your .sql file - not included in repo)
```

---

## 📌 Notes

- The script assumes the `.sql` file contains standard MySQL `CREATE TABLE` and `FOREIGN KEY` syntax.
- Only schema is parsed — data is ignored.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify.

---

## 👨‍💻 Author

Made with ❤️ by \[Wai Hyn Htun]
GitHub: [@kamkyi](https://github.com/kamkyi)
