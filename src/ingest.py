from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def main():
    print("AI knowledge - Document Ingestion")
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Raw documents directory:{RAW_DATA_DIR}")
    

    if not RAW_DATA_DIR.exists():
         print("Error: Raw documents directory does not exist.")
         return

    print("Raw documents directory is ready.")
pdf_files = list(RAW_DATA_DIR.glob("*.pdf"))

print(f"PDF files found: {len(pdf_files)}")

for pdf_file in pdf_files:
    print(pdf_file.name)

if __name__ == "__main__":
    main()